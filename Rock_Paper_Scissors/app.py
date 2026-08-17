from pwn import *
from ctypes import CDLL
from ctypes.util import find_library

#p = process('./chall')
p = remote('host3.dreamhack.games', 10635)
libc = CDLL(find_library('c'))
libc.srand(libc.time(0))

move_map = {0: b'P', 1: b'S', 2: b'R'}

for _ in range(10):
    c = libc.rand() % 3
    p.sendlineafter(b'Put your hand out(R, P, S): ', move_map[c])

print(p.recvall().decode())