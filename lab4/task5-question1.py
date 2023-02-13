from netmiko import Netmiko
devices = [{"device_type": "cisco_ios",
 "ip": "192.168.1.101",
 "username": "student",
 "password": "Meilab123",
 "port": "22",}]
ip = '1.1.1.1 255.255.255.255'
loopback_config = ["interface loopback 1",
 f"ip address {ip}",f"no shut"]
 
for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(loopback_config)
    print(output)
    net_connect.disconnect()

