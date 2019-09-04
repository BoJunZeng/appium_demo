import subprocess
import os


class Common(object):

    def shell_cmd(self, shellcmd):
        dict_shell = {}
        proc = subprocess.Popen(args=shellcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        std_out = proc.communicate()[0].decode("utf-8")
        return_code = proc.returncode
        dict_shell['std_out'] = std_out
        dict_shell['returncode'] = return_code
        return dict_shell



