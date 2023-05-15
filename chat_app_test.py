import requests

print(requests.get("http://127.0.0.1:8000/chat?humen_input=I'm bob").content)
print(requests.get("http://127.0.0.1:8000/chat?humen_input=what's my name?").content)