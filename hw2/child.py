#!/usr/bin/python3
import os
import sys
import time
import random


pid = os.getpid()
parent_pid = os.getppid()

print(f'Child[{pid}]: I am started. My PID {pid}. Parent PID {parent_pid}')

s = int(sys.argv[1])
time.sleep(s)

print(f'Child[{pid}]: I am ended. My PID {pid}. Parent PID {parent_pid}')

status = random.choice([0, 1])
os._exit(status)