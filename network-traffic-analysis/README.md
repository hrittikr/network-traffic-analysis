# Network Traffic Capture and Analysis

Cyber Analytics project (HCLTech training, Project No. 2). Traffic was captured in an authorized lab (Kali Linux VM on VMware, NAT network) with Wireshark and analyzed to identify protocols, endpoints and communication patterns.

## What this project does

- Runs a small Flask login app over plain HTTP (dummy credentials only)
- Captures its traffic on the loopback interface and shows that credentials travel in clear text
- Captures internet traffic (ICMP, DNS, HTTP) on `eth0` using `ping`, `nslookup` and `curl`
- Summarizes findings and recommends fixes (HTTPS, encrypted DNS, monitoring)

## Lab setup

| Item | Details |
|---|---|
| OS | Kali Linux (VMware Workstation, NAT) |
| Tools | Wireshark, tshark, capinfos, ping, nslookup, curl |
| App | Flask (Python 3) on 127.0.0.1:5000 |

## Key results

- Login capture: 47 packets, 7 HTTP packets, 2 POST requests
- Credentials visible in Follow HTTP Stream: `username=admin&password=test123`
- Ping to google.com: 4/4 received, 0% loss, avg 8.683 ms
- DNS: example.com resolved via 192.168.246.2 (2 IPv4 + 1 IPv6 records)

## Repository structure

```
network-traffic-analysis/
├── README.md
├── app/app.py
├── capture/login_traffic.pcapng
├── screenshots/        (01 to 10)
└── report/             (PDF report)
```

## How to reproduce

```bash
python3 app/app.py                      # start the demo app
sudo tshark -i lo -f "tcp port 5000" -w capture/login_traffic.pcapng
# open http://127.0.0.1:5000 in a browser and log in, then press Ctrl+C
tshark -r capture/login_traffic.pcapng -q -z io,phs
```

## Disclaimer

All captures were done only on my own virtual machine in an isolated lab. Credentials shown are dummy values created for this demo.
