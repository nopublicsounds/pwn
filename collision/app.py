from pwn import *
s = ssh('col', 'pwnable.kr', 2222, 'guest')

path = './col'
arg = p32(0x01111111) * 4 + p32(0x1d98c5a8)
payload = [path, arg]

p = s.run(payload)
p.interactive()