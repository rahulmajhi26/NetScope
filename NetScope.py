#!/usr/bin/env python3

import ipaddress
import socket
import os

def reverse_dns_lookup(ip):
    try:
        return socket.gethostbyaddr(str(ip))[0]
    except socket.herror:
        return "No PTR Record"

def export_to_file(ip_data, filename="ip_output.txt"):
    with open(filename, 'w') as f:
        for ip, dns in ip_data:
            f.write(f"{ip} - {dns}\n")
    print(f"\n✅ Output saved to {filename}")

def process_ips(ip_list, do_dns=False, export=False):
    ip_data = []
    for ip in ip_list:
        if do_dns:
            dns = reverse_dns_lookup(ip)
            print(f"{ip} - {dns}")
            ip_data.append((ip, dns))
        else:
            print(ip)
            ip_data.append((ip, ""))
    if export:
        export_to_file(ip_data)

def main():
    print("=== IP CIDR / Range Scanner with DNS & Export ===\n")
    user_input = input("Enter IP CIDR or IP Range (e.g., 192.168.1.0/24 or 192.168.1.1-192.168.1.10): ").strip()
    enable_dns = input("Do reverse DNS lookup? (y/n): ").strip().lower() == 'y'
    enable_export = input("Export results to a file? (y/n): ").strip().lower() == 'y'

    ip_list = []

    # CIDR block
    if "/" in user_input:
        try:
            network = ipaddress.ip_network(user_input, strict=False)
            ip_list = list(network.hosts())
        except ValueError as e:
            print(f"❌ Error: {e}")
            return

    # IP range
    elif "-" in user_input:
        try:
            start_ip, end_ip = user_input.split("-")
            start = ipaddress.IPv4Address(start_ip.strip())
            end = ipaddress.IPv4Address(end_ip.strip())

            if start > end:
                print("❌ Error: Start IP must be less than End IP.")
                return

            ip_list = [ipaddress.IPv4Address(ip) for ip in range(int(start), int(end) + 1)]
        except ValueError as e:
            print(f"❌ Error: {e}")
            return
    else:
        print("❌ Invalid format. Use CIDR (e.g., 192.168.1.0/24) or IP range (e.g., 192.168.1.1-192.168.1.10).")
        return

    print(f"\n🔢 Total IPs: {len(ip_list)}\n")
    process_ips(ip_list, do_dns=enable_dns, export=enable_export)

if __name__ == "__main__":
    main()
