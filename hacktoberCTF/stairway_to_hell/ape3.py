#!/usr/bin/env python3

from pwn import log
from pwnlib.tubes.process import process


def stairway(start_number: int, max_rows: int) -> None:
    number = start_number
    rows = 0
    message = ""
    while rows != max_rows:
        rows += 1

        for _ in range(rows):
            message += f"{number} "
            number += 1

    log.info(f"Sending message: '{message.rstrip()}'")
    sh = process("/bin/bash")
    sh.sendline(f"echo '{message.rstrip()}' | nc env2.hacktober.io 5001")

    log.info(sh.recvline().decode("latin-1"))
    log.info(sh.recvline().decode("latin-1"))
    log.info(sh.recvline().decode("latin-1"))
    log.info(sh.recvline().decode("latin-1"))
    sh.close()


if __name__ == "__main__":
    stairway(666, 30)