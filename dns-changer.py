from os import system
from termcolor import colored
from pyfiglet import figlet_format
print(colored(figlet_format("dns changer", justify="center"), "green"))

ask = input("set dns or back to default: (d/b) \n")
dns_list = {
    'google' : '8.8.8.8',
    'cisco' :'4.2.2.4',
    'shakan' : '185.51.200.2',
}

print("dns : \n1) google \n2) cisco \n3) shekan")

if ask == 'd':
    dns = input("type ur dns : \n")
    if '.' in dns:
        system(f'echo nameserver  {dns} | sudo tee -a /etc/resolv.conf')
    else :
        print("invalid dns")
elif ask == 'b':
    system("sudo systemctl restart NetworkManager")
