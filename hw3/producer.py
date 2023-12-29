#!/usr/bin/python3
import random
import time
import sys
import os


operators = ['+', '-', '*', '/']
n = random.randint(120, 180)

for _ in range(n):
    x = random.randint(1, 9)
    o = random.choice(operators)
    y = random.randint(1, 9)

    print(f"{x} {o} {y}")
    sys.stdout.flush()
    time.sleep(1)

os._exit(0)