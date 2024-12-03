import json

try:
    while True:
        command = json.loads(input())
        if command["type"] == "add":
            response = {"result": command["a"] + command["b"]}
        print(json.dumps(response))
except EOFError:
    pass
