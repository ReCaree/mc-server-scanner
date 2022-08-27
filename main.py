import random
import time
import masscan

A = list(range(1,0xff))
B = list(range(1,0xff))
random.shuffle(A)
random.shuffle(B)
ip_ranges = []

for a in A:
  for b in B:
    ip_range = f"{a}.{b}.0.0/16"
    ip_ranges.append(ip_range)

while True:
  random.shuffle(ip_ranges)
  for ip_range in ip_ranges:
    print(ip_range)
    try:
      mas = masscan.PortScanner()
      mas.scan(ip_range, ports='25565', arguments='--max-rate 1000')
      delay = 5000
      for ip in mas.scan_result['scan']:
        host = mas.scan_result['scan'][ip]
        print(f"{ip} {host}")
        # if 'tcp' in host and 25565 in host['tcp']:
        #   server = MinecraftServer.lookup()
    except masscan.NetworkConnectionError:
      print(f"{ip_range} NetworkConnectionError")
      time.sleep(30)
    print("done scanning")