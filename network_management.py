# Paramiko, Netmiko and NAPALM → used in Python network automation

# Paramiko code
#show_cisco_int_pmk.py
import paramiko
host='HOST_ID'
port=22
username='xxx'
password='xxxxxx'
#cisco ios command to get a list of IP interfaces
cmd= 'show ip int brief \n'
def main():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.
        AutoAddPolicy())
        ssh.connect(host, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        output_lines = stdout.readlines()
        response = ''.join(output_lines)
        print(response)
    finally:
        ssh.close()
if __name__ == '__main__':
    main()