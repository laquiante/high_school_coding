import telnetlib
import time

# fuer die PVLAN Demo brauche ich die 10.0.1.200 auf dieser Maschine
switch = '10.0.1.2'
port = '23'

# NX-OS fuer das Labor: no password strength-check
user = 'admin'
password = 'admin' 

# NX-OS fuer das Labor: feature telnet
tn = telnetlib.Telnet(host=switch, port=port)

tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
print("1")
tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')
print("2")
tn.write(b'terminal length 0\n')
print("3")
tn.write('show ip interface mgmt 0\n'.encode())
print("4")
tn.write(b'exit\n')
print("5")

time.sleep(1)
print("6")

output = tn.read_all()
print(type(output))
print("7")

output = output.decode()
print(output)
print("8")
