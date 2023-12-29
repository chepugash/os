#!/usr/bin/python3
import os
import random
import sys


interpreter = '/usr/bin/python3'
child_script = 'child.py'


def start_child():
    child = os.fork()

    if child == 0:
        s = random.randint(5, 10)
        os.execve(interpreter, [interpreter, child_script, str(s)], os.environ)
    else:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {child}')


n = int(sys.argv[1])

for _ in range(n):
    start_child()

c = 0

while c != n:
    child_pid, status = os.wait()

    print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit status {os.WEXITSTATUS(status)}')
    
    if status != 0:
        start_child()
    else:
        c += 1

os._exit(0)