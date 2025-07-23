import socket

def scan_ports(target_ip):
    print(f"\n[+] Scanning Target: {target_ip}\n")
    open_ports = []

    for port in range(1, 1025):  # Common ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"testing {target_ip}")
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("[-] No open ports found.")
    else:
        print(f"\n[✓] Total open ports: {len(open_ports)}")

if __name__ == "__main__":
    target = input("Enter Target IP: ")
    scan_ports(target)
