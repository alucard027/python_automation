import paramiko

HOST = '200.106.174.154'
PORT = '22'
USER = 'ubuntu'
SSHKEY = 'E:\Key_pairs\nextcloud_cp.pem'


client = paramiko.SSHClient()
client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
    
client.connect(HOST, PORT, USER, SSHKEY)
    
stdout = client.exec_command('uptime')
   
result = stdout.read().decode()
   
print(result)