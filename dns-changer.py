from os import system
from termcolor import colored
from pyfiglet import figlet_format
print(colored(figlet_format("dns changer", justify="center"), "green"))

dns_list = {
    'google' : '8.8.8.8',
    'cisco' :'4.2.2.4',
    'shekan' : '185.51.200.2',
    'shekan2' : "178.22.122.100",
}
for name in dns_list:
    print(f"- {name} \n ")

ask = input("set dns or set just one dns (recommended for shekan) or back to default: (s/j/b) \n")

if ask[0] == 's':
    print("for set dns in list type ur dns by name")
    dns = input("type ur dns : \n")
    if '.' in dns:
        system(f'echo nameserver  {dns} | sudo tee -a /etc/resolv.conf >> /dev/null')
        print(f"dns {dns} added")
    elif dns in dns_list:
        system(f'echo nameserver  {dns_list[dns]} | sudo tee -a /etc/resolv.conf >> /dev/null')
        print(f"dns {dns} added")
    else:
        print("Invalid dns")
elif ask[0] == 'j':
    print("for set dns in list type ur dns by name")
    dns = input("type ur dns : \n")
    if '.' in dns:
        system(f'echo nameserver  {dns} | sudo tee /etc/resolv.conf >> /dev/null')
        print(f"dns changed to {dns}")
    elif dns in dns_list:
        system(f'echo nameserver  {dns_list[dns]} | sudo tee /etc/resolv.conf >> /dev/null')
        print(f"dns changed to {dns}")
    else:
        print("Invalid dns")

elif ask[0] == 'b':
    print("restarting ...")
    system("sudo systemctl restart NetworkManager")
