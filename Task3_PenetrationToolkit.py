#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

# Check host
def check_host(target):
    try:
        ip = socket.gethostbyname(target)
        print("Host is alive. IP:", ip)
    except:
        print("Host not reachable")

# Port scanning
def port_scan(target, ports):
    print("\nScanning Ports...")
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
            banner_grab(target, port)
        
        s.close()

# Banner grabbing
def banner_grab(target, port):
    try:
        s = socket.socket()
        s.connect((target, port))
        banner = s.recv(1024)
        print(f"Banner from port {port}: {banner.decode().strip()}")
        s.close()
    except:
        print(f"No banner on port {port}")

# Main
print("=== Penetration Testing Toolkit ===")

target = input("Enter target (example: scanme.nmap.org): ")

check_host(target)

common_ports = [21, 22, 23, 25, 80, 443]
port_scan(target, common_ports)

print("\nScan Completed.")


# In[ ]:




