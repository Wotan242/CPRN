import getloopback as GL
import generatebgp as GB
import netmiko
import time

ip_nx = ['10.0.0.100']

ip_iosxe = ['10.0.0.101', '10.0.0.102']

lp_nx = []

for ip in ip_nx:
    lp_nx.append(GL.nxos(ip, 'student', 'L1nux_dc'))
    
lp_iosxe = []

for ip in ip_iosxe:
    lp_iosxe.append(GL.iosxe(ip, 'student', 'L1nux_dc'))
    
print(lp_nx , lp_iosxe)

lp_all = lp_nx + lp_iosxe

print(lp_all)


for loop in lp_nx:
    bgp_nx = GB.nxos('65000' , loop , lp_all)
    session_nx = netmiko.ConnectHandler(ip = ip_nx[lp_nx.index(loop)] , 
                                 username = 'student' , 
                                 password = 'L1nux_dc' , 
                                 device_type = "cisco_nxos")
    session_nx.send_config_set(config_commands = 'feature bgp')
    session_nx.send_config_set(config_commands = bgp_nx)
    time.sleep(3)
    print(session_nx.send_command('show bgp ipv4 unicast summary'))
    session_nx.disconnect()
    
   
for loop in lp_iosxe:
    bgp_iosxe = GB.iosxe('65000' , loop , lp_all)
    session_iosxe = netmiko.ConnectHandler(ip = ip_iosxe[lp_iosxe.index(loop)] , 
                                 username = 'student' , 
                                 password = 'L1nux_dc' , 
                                 device_type = "cisco_ios")
    session_iosxe.send_config_set(config_commands = bgp_iosxe)
    time.sleep(3)
    print(session_iosxe.send_command('show bgp ipv4 unicast summary'))
    session_iosxe.disconnect()


