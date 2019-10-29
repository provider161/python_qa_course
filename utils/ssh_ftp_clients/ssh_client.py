"""
SSH client for connection and tuning linux system
"""


from paramiko import SSHClient
import paramiko


class Client(SSHClient):

    host = '127.0.0.1'
    user = 'provider'
    password = 'provider'
    port = 3022

    def __init__(self):
        super().__init__()
        super().set_missing_host_key_policy(paramiko.AutoAddPolicy)
        super().connect(hostname=self.host, port=self.port, username=self.user, password=self.password)

    def install_ftp_service(self):
        stdin, stdout, stderr = super().exec_command('sudo apt-get install vsftpd')
        data = stdout.read() + stderr.read()
        print(data.decode("utf-8"))
        stdin, stdout, stderr = super().exec_command('systemctl start vsftpd')
        data = stdout.read() + stderr.read()
        print(data.decode("utf-8"))
        stdin, stdout, stderr = super().exec_command('systemctl enable vsftpd')
        data = stdout.read() + stderr.read()
        print(data.decode("utf-8"))

    def __del__(self):
        super().close()


client = Client()
client.install_ftp_service()
