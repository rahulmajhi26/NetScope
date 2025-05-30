{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1ed1b9d-ab19-4fad-a99c-951f42166b86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== IP CIDR / Range Scanner with DNS & Export ===\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python3\n",
    "\n",
    "import ipaddress\n",
    "import socket\n",
    "import os\n",
    "\n",
    "def reverse_dns_lookup(ip):\n",
    "    try:\n",
    "        return socket.gethostbyaddr(str(ip))[0]\n",
    "    except socket.herror:\n",
    "        return \"No PTR Record\"\n",
    "\n",
    "def export_to_file(ip_data, filename=\"ip_output.txt\"):\n",
    "    with open(filename, 'w') as f:\n",
    "        for ip, dns in ip_data:\n",
    "            f.write(f\"{ip} - {dns}\\n\")\n",
    "    print(f\"\\n✅ Output saved to {filename}\")\n",
    "\n",
    "def process_ips(ip_list, do_dns=False, export=False):\n",
    "    ip_data = []\n",
    "    for ip in ip_list:\n",
    "        if do_dns:\n",
    "            dns = reverse_dns_lookup(ip)\n",
    "            print(f\"{ip} - {dns}\")\n",
    "            ip_data.append((ip, dns))\n",
    "        else:\n",
    "            print(ip)\n",
    "            ip_data.append((ip, \"\"))\n",
    "    if export:\n",
    "        export_to_file(ip_data)\n",
    "\n",
    "def main():\n",
    "    print(\"=== IP CIDR / Range Scanner with DNS & Export ===\\n\")\n",
    "    user_input = input(\"Enter IP CIDR or IP Range (e.g., 192.168.1.0/24 or 192.168.1.1-192.168.1.10): \").strip()\n",
    "    enable_dns = input(\"Do reverse DNS lookup? (y/n): \").strip().lower() == 'y'\n",
    "    enable_export = input(\"Export results to a file? (y/n): \").strip().lower() == 'y'\n",
    "\n",
    "    ip_list = []\n",
    "\n",
    "    # CIDR block\n",
    "    if \"/\" in user_input:\n",
    "        try:\n",
    "            network = ipaddress.ip_network(user_input, strict=False)\n",
    "            ip_list = list(network.hosts())\n",
    "        except ValueError as e:\n",
    "            print(f\"❌ Error: {e}\")\n",
    "            return\n",
    "\n",
    "    # IP range\n",
    "    elif \"-\" in user_input:\n",
    "        try:\n",
    "            start_ip, end_ip = user_input.split(\"-\")\n",
    "            start = ipaddress.IPv4Address(start_ip.strip())\n",
    "            end = ipaddress.IPv4Address(end_ip.strip())\n",
    "\n",
    "            if start > end:\n",
    "                print(\"❌ Error: Start IP must be less than End IP.\")\n",
    "                return\n",
    "\n",
    "            ip_list = [ipaddress.IPv4Address(ip) for ip in range(int(start), int(end) + 1)]\n",
    "        except ValueError as e:\n",
    "            print(f\"❌ Error: {e}\")\n",
    "            return\n",
    "    else:\n",
    "        print(\"❌ Invalid format. Use CIDR (e.g., 192.168.1.0/24) or IP range (e.g., 192.168.1.1-192.168.1.10).\")\n",
    "        return\n",
    "\n",
    "    print(f\"\\n🔢 Total IPs: {len(ip_list)}\\n\")\n",
    "    process_ips(ip_list, do_dns=enable_dns, export=enable_export)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0644c92c-ed49-4e67-b495-1b0092f75fb8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
