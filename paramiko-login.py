import paramiko


def login(hostname, username, passwd, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=passwd, port=port)
    channel = ssh.invoke_shell()
    return channel
