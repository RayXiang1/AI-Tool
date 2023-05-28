import requests

print(requests.get("http://127.0.0.1:8000/address/resolver?raw_address=广东省东莞市沙田镇东莞保税物流中心临海北路70号大华1号仓").content)
# print(requests.get("http://127.0.0.1:8000/chat?humen_input=what's my name?").content)
# print(requests.get("http://10.255.134.200:8085/chat?humen_input=I'm bob").content)