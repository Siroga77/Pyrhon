import socket
from datetime import datetime
from colorama import Fore, init

init()

print(f'''{Fore.LIGHTRED_EX}
Turbo_scanner 0.2.0
''')

print(f"{Fore.LIGHTCYAN_EX}[#=>] Coded by Siroga Matsei\n")

addr = input("Enter address of site: ")
ip = socket.gethostbyname(addr)
print("Site iP is: ", ip , "\n")

start = datetime.now()
ports_services = {20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
                  115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP", 179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
                  514: "SYSLOG", 515: "PRINTER", 993: "IMAPS", 995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
                  1433: "SQL Server", 1723: "PPTP", 3128: "HTTP", 3268: "LDAP", 3306: "MySQL", 3389: "RDP",
                  5432: "PostgreSQL", 5060: "SIP", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin"}

print(f"{Fore.LIGHTYELLOW_EX}")
ip = input("Site Name / IP Address: ")
print(f"{Fore.LIGHTGREEN_EX}IP address:", socket.gethostbyname(ip), "\n")
print(f"{Fore.LIGHTRED_EX}<===============>\n")
print(f"{Fore.WHITE}Loading Ports...")
print(f"{Fore.LIGHTGREEN_EX}##################")
for port in ports_services:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((ip, port))
    except socket.error:
        pass
    else:
        print(
            f"{ip} {str(port)} {Fore.LIGHTGREEN_EX}is open/{ports_services[port]}")
        s.close()

print(f"{Fore.LIGHTGREEN_EX}##################")
ends = datetime.now()
print(f"{Fore.LIGHTRED_EX}" + "<Time:{}>".format(ends - start))

print(f"{Fore.MAGENTA}Scan completed!")
input("Press Enter to the exit....")
