from sys import argv
import subprocess
import ipaddress

def check_if_ip_is_network(ip_address):
    try:
        ipaddress.ip_network(ip_address)
        return True
    except ValueError:
        return False

def check_ip_addresses(args):
    ava = []
    no_ava = []
    args.pop(0)
    for i in args:
        if check_if_ip_is_network(i) == True: 
            result = subprocess.run(['ping', '-c', '3', i], stdout=subprocess.DEVNULL)
            if result.returncode == 0:
                ava.append(i)
            else:
                no_ava.append(i)
        else:
            print('IP address {0} not  correct'.format(i))
    return(ava, no_ava)

a,b = check_ip_addresses(argv)
print(a,b)