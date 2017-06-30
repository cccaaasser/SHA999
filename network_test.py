import os
import socket


def menu():
    print("====================Choose function====================")
    print("[1] Check host status")
    print("[2] Check local IP")
    print("[3] Port Scanner")
    print("[4] DNS lookup")
    print("[5] Ping")
    print("[E]xit")


def check_host():
    host = input("Host: ")
    response = os.system("ping -n 1 " + host)

    if response == 0:
        print("\n\nHost is up!")
        input("\n\nPlease enter to return to menu...")
    else:
        print("\n\nHost is down!")
        input("\n\nPlease enter to return to menu...")
    return


def check_ip():
    ip = socket.gethostbyname(socket.getfqdn())
    print("\n\nYour IP: " + ip)
    input("\n\nPlease enter to return to menu...")
    return


def dns_lookup():
    dns = input("Host: ")
    addr = socket.gethostbyname(dns)

    print(dns + ": " + addr)
    input("\n\nPlease enter to return to menu...")
    return


def port_scanner():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = input("Enter host: ")
    print("\n\nWaiting...")

    def pscan(port):
        try:
            s.connect((server, port))
            return True
        except:
            return False

    for x in range(0, 1024):
        if pscan(x):
            print("\n\nPort", x, "is open")

    print("\n\nReturn to menu...")
    return


def ping():
    host = input("Host: ")
    times = 4
    times = int(input("How many times?: "))
    cmd = 'ping -n ' + str(times) + " " + host
    ping = "".join(os.popen(cmd).readlines())
    print(ping)

    input("\n\nReturn to menu...")
    return


print("              ======================================")
print("              ==                                  ==")
print("              ==  Welcome to network tools V 0.1  ==")
print("              ==                                  ==")
print("              ======================================")
print("By SHA999")
print("Date: 29/06/2017")
print("\n\n\n")
ans = True
while ans:
    menu()

    choose = input("\nChoose menu: ")
    if choose == "1":
        check_host()
    elif choose == "2":
        check_ip()
    elif choose == "3":
        port_scanner()
    elif choose == "4":
        dns_lookup()
    elif choose == "5":
        ping()
    elif choose == "e" or choose == 'E':
        print("\n\nGood Bye!")
        ans = False
    else:
        print("\n\nTry again...");
