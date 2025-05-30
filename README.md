# NetScope
A powerful Python-based tool for cybersecurity professionals and enthusiasts to extract all hosts from a given IP Range or CIDR block. Includes reverse DNS lookup, export to file, and supports both CIDR and IP-range input formats.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🔎 CIDRSpy

**NetScope** is an advanced Python-based tool designed for cybersecurity professionals, bug bounty hunters, and ethical hackers. It extracts all IP addresses from a given **CIDR block** or **IP range**, supports **reverse DNS lookups**, and allows optional **export to a text file**. Perfect for network reconnaissance and target scoping.

---

## ⚙️ Features

- ✅ Supports **CIDR notation** (e.g., `192.168.0.0/24`)
- ✅ Accepts **IP range** (e.g., `192.168.0.1-192.168.0.10`)
- 🌐 Optional **reverse DNS (PTR) lookup**
- 📝 Optional **export to a `.txt` file**
- 🔐 Built with Python 3 – no external libraries needed
- 💻 Works perfectly on **Kali Linux** and all Unix systems

---

## 🧠 Use Cases

- Network reconnaissance and mapping
- Subnet/IP enumeration during red teaming
- Lab testing and simulations
- Bug bounty scoping (public IP ranges)

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/CIDRSpy.git
cd CIDRSpy
chmod +x ip_range_scanner.py

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


🚀 Usage
Run the tool: ./ip_range_scanner.py



Example session:

=== IP CIDR / Range Scanner with DNS & Export ===

Enter IP CIDR or IP Range (e.g., 192.168.1.0/24 or 192.168.1.1-192.168.1.10): 8.8.8.0/30
Do reverse DNS lookup? (y/n): y
Export results to a file? (y/n): y

🔢 Total IPs: 2

8.8.8.1 - dns.google
8.8.8.2 - No PTR Record

✅ Output saved to ip_output.txt

---------------------------------------------------

🧾 Output
If export is enabled, the output is saved as ip_output.txt:

8.8.8.1 - dns.google
8.8.8.2 - No PTR Record
--------------------------------------------------

🔐 Requirements
Python 3.x

Works out-of-the-box on Kali Linux, Parrot OS, Ubuntu, etc.

-----------------------------------------------------

| Format | Example                    | Description            |
| ------ | -------------------------- | ---------------------- |
| CIDR   | `192.168.0.0/24`           | Lists all usable hosts |
| Range  | `192.168.0.1-192.168.0.20` | Custom IP range scan   |


--------------------------------------------------------

📌 Roadmap (Coming Soon)
1. ICMP ping check for live hosts

2. Multithreaded reverse DNS lookups

3. Export to JSON or CSV formats

4. Hostname filters and tagging

-------------------------------------------------------

📜 License
This project is licensed under the MIT License — free for personal, educational, or commercial use.


🤝 Credits
Developed by Rahul Majhi
Part of the R-Dex Cyber Solution toolkit.
