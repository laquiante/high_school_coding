import time
# $ sudo apt-get update
# $ sudo apt-get install python3-paramiko
import paramiko

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

nx_os_switch = {'hostname': '10.0.1.2', 'port': '22', 'username': 'admin', 'password':'admin'}

ssh_connection.connect(**nx_os_switch, look_for_keys=False, allow_agent=False)

shell = ssh_connection.invoke_shell()

shell.send('terminal length 0\n')
shell.send('show vlan\n')
time.sleep(2)

print(shell.recv(10000).decode('utf-8'))

if ssh_connection.get_transport().is_active() == True:
    print('Die Verbindung wird beendet')
    ssh_connection.close()
