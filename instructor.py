import subprocess
import json

process = subprocess.Popen(["python3", "executor.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

commands = [
    {"type": "add", "a": 3, "b": 5},
    {"type": "add", "a": 2, "b": 0},
    {"type": "add", "a": 8, "b": 1},
    {"type": "add", "a": 1, "b": 4},
]

for command in commands:
    print("<", command)
    process.stdin.write((json.dumps(command) + "\n").encode())
    process.stdin.flush()
    output = json.loads(process.stdout.readline())
    print(">", output)

process.stdin.close()
process.wait()
