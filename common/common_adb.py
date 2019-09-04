import os

class AdbCommon(object):

    def call_adb(self, command, udid=None):
        """
        call adb command by shell if you want control android device by shell cmd.
        :param command: shell command. eg: adb devices/adb reboot ...
        :param udid: select a device to execute this shell command
        :return:
            command execute result
        """
        command_result = ''
        if udid is None:
            command_text = 'adb %s' % command
        else:
            command_text = 'adb -s %s %s' % (udid, command)
        results = os.popen(command_text, "r")
        while True:
            line = results.readline()
            if not line:
                break
            command_result += line
        results.close()
        return command_result

    def attach_devices(self):
        """
        get attached devices list, device status must be online
        :return:
            a list about more attached devices udid
        """
        result = self.call_adb("devices")
        l_devices = list(filter(None, result.partition('\n')[2].replace('\n', '').split('\tdevice')))
        return l_devices

    def is_device_attached(self, udid):
        """
        check select device is attached and on devices list
        :param udid: device id
        :return:
            if True:
                this device was attached and found on attached devices list
            else:
                device not attached
        """
        l_devices = self.attach_devices()
        if len(l_devices) > 0:
            if udid in l_devices:
                return True
        return False

    def reboot(self, option):
        """
        reboot the device
        :param option: can select reboot ways eg:[reboot bootloader, reboot recovery]
        :return:
        """
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    def open_app(self, packageName, activity):
        """
        start an application by (pkg_name/activity_name)
        :param packageName: app package name
        :param activity: app activity name
        :return:
            True: open an application success
            False: open app fail
        """
        self.call_adb("shell am force-stop %s" % packageName)
        result = self.call_adb("shell am start -n %s/%s" % (packageName, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    def adb_push_resource_to_device(self, resource_path, push_to):
        """
        push resource file to device by adb command
        :param resource_path: provide a folder path can load all file to push but if path
            is a file path, only push this file
        :param push_to: a device path to receive
        :return:
            total push device files count
        """
        file_count = 0
        if os.path.isdir(resource_path):
            dir_list = os.listdir(resource_path)
            for f_name in dir_list:
                f_abs_path = os.path.join(resource_path, f_name)
                if os.path.isfile(f_abs_path):
                    self.call_adb("push " + f_abs_path + " " + push_to)
                    file_count += 1
                else:
                    file_count += self.adb_push_resource_to_device(f_abs_path, push_to)
        else:
            self.call_adb("push " + resource_path + " " + push_to)
            file_count += 1
        return file_count



