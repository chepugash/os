#!/usr/bin/python3
import os
import signal
import sys


encoding = 'utf-8'
producer_script = './producer.py'
bc = '/usr/bin/bc'

counter = 0


def sigusr1_handler(signum, frame):
    print(f"Produced: {counter}")
    sys.stdout.flush()


signal.signal(signal.SIGUSR1, sigusr1_handler)

p1to0 = os.pipe()
p0to2 = os.pipe()
p2to0 = os.pipe()

p1 = os.fork()

if p1 == 0:
    os.close(p1to0[0])

    os.dup2(p1to0[1], sys.stdout.fileno())
    
    os.execve(producer_script, [producer_script], os.environ)
    os._exit(0)

p2 = os.fork()

if p2 == 0:
    os.close(p0to2[1])
    os.close(p2to0[0])

    os.dup2(p0to2[0], sys.stdin.fileno())
    os.dup2(p2to0[1], sys.stdout.fileno())
    
    os.execve(bc, [bc], os.environ)
    os._exit(0)

os.close(p1to0[1])
os.close(p0to2[0])
os.close(p2to0[1])

while True:
    exp = os.read(p1to0[0], 1024).decode(encoding)
    if not exp:
        break
    
    os.write(p0to2[1], exp.encode(encoding))

    result = os.read(p2to0[0], 1024).decode(encoding)
    
    print(f"{exp.strip()} = {result.strip()}")
    
    counter += 1

os.kill(p1, signal.SIGTERM)
os.kill(p2, signal.SIGTERM)

os._exit(0)