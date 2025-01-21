my_hex = "0x123456789"
my_hex = my_hex[2:]
print(my_hex)
print([my_hex[i:i+2] for i in range(0,len(my_hex), 2)])
