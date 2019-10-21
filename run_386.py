import os, sys
import subprocess
import time



python_path = sys.path[1] + r'/venv/bin/python3.6'

scripts = [
        sys.path[1] + r'/TESTS/google.py',
        sys.path[1] + r'/TESTS/yahoo.py',
        ]
p = []
def start():
    for i in range(len(scripts)):
        print(i)
        print(scripts[i])
        p.insert(i,subprocess.Popen([python_path,scripts[i]]))
        print(p)
        time.sleep(10)

def check():
    for i in range(len(scripts)):
        print('################')
        print(p[i].poll())
        if p[i].poll() is not None:
            try:
                print('killed')

                p[i].kill()
            except Exception as err:
                print(err)
            p[i] = subprocess.Popen([python_path,scripts[i]])
        else:
            print('status ok')
            pass
start()
while True:
    check()
    time.sleep(6)


