from sys import argv

def check_ip_addresses(arg):
    print(argv)
    good_ip = open('good_ip.txt', 'r')
    bad_ip = open('bad_ip.txt', 'r')
    
    good_ip.close()
    bad_ip.close()
    return(0)

check_ip_addresses(argv.pop(0))