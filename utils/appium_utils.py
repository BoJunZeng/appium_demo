import os
import sys
import subprocess
from time import ctime
import time
import socket
from utils.common_utils import Common

root_dir = os.path.dirname(os.path.dirname(__file__))


class AppiumUtils(Common):

    def appium_start(self, _host, _port):
        """
            start an appium server, if you want start any auto test from appium, you need
            start appium server first!
            :param host: the localhost number, eg:127.0.0.1
            :param port: the appium server lisenning port, eg:4723 but can't set 4724, be
            -cause bootstrap-port need set next one by port
            :return:
        """
        print("=======Start appium server[port:%s] at: %s=======" % (str(_port), ctime()))
        bp = str(_port + 1)
        cmd = "appium -a " + str(_host) + " -p " + str(_port) + " -bp " + bp
        print("Cmd:%s" % cmd)
        log_path = os.path.join(root_dir, 'log', 'appium_' + str(_port) + '.log')
        print("Log path:%s" % log_path)
        subprocess.Popen(cmd, shell=True, stdout=open(log_path, 'a'), stderr=subprocess.STDOUT)
        time.sleep(5)
        print("=======Start appium server[port:%s] success!!!=======" % str(_port))

    def start_appium_server(self, _host, _port):
        if self.is_appium_port_idle(_host, _port):
            self.appium_start(_host, _port)
            return True
        else:
            print("=======Start appium server[host:%s/port:%s] fail!!!=======" % (str(_host), str(_port)))
            return False

    def release_appium_server_port(self, _port):
        server_pid = self.get_netstat_pid_by_port(_port)
        if server_pid is not None:
            kill_cmd = "kill " + str(server_pid)
            os.popen(kill_cmd)
            print("Appium server: port=%d/pid=%d kill done ..." % (_port, server_pid))
        else:
            print("Appium server port:%d is idle and available!" % _port)

    def is_appium_port_idle(self, _host, _port):
        s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s_client.connect((_host, _port))
            s_client.shutdown(socket.SHUT_RDWR)
        except OSError:
            print("Appium server port:%d is not be used!" % _port)
            return True
        else:
            print("Appium server port:%d is using!" % _port)
            return False

    def get_netstat_pid_by_port(self, _port):
        pid = None
        cmd = "netstat -nlptu | awk '{print $4,$7}' | grep " + str(_port)
        shell_dict = self.shell_cmd(cmd)
        tag = ":" + str(_port)
        for line in shell_dict['std_out'].split('\n'):
            if tag in line:
                pid = line.split(' ')[1].split('/')[0]
        return int(pid)

    def multi_start_appium_server(self):
        pass

    def multi_connect_device(self):
        pass


