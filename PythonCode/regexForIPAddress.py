0-9 [0-9]
10-99 [1-9][0-9]
100-199 1[0-9][0-9]
200-249 2[0-4][0-9]
250-255 25[0-5]

import re

public_ip = "256.10.10.10"
my_str = r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
pattern = re.compile(my_str)

if pattern.match(public_ip):
    print("IP Address Valid")
else:
    print("Ip Address Not Valid")

