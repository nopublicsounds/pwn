from pwn import *
s = ssh('random', 'pwnable.kr', 2222, 'guest')

path = './random'
payload = 0x6b8b4567 ^ 0xcafebabe
payload = str(payload)
print(payload)

p = s.run(path)
p.sendline(payload)
p.interactive()