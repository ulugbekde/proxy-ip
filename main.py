import requests
import random

def get_random_proxy():
    response = """
37.187.109.70:10111
67.43.227.227:16271
67.43.227.227:13973
67.43.228.253:20409
67.43.228.253:22397
72.10.164.178:10689
72.10.160.171:3011
72.10.164.178:33089
72.10.164.178:25833
72.10.164.178:32665
77.55.213.249:3128
1.52.48.25:11111
4.155.2.13:9480
67.43.227.227:3287
67.43.236.20:12953
72.10.160.92:7285
72.10.160.93:3297
72.10.164.178:26311
177.37.217.45:8080
8.219.97.248:80
67.43.236.20:17247
103.122.60.245:8080
181.115.93.77:999
20.235.159.154:80
210.79.146.222:8085
47.243.166.133:18080
45.228.233.94:999
67.43.228.253:10879
72.10.164.178:18591
103.146.185.139:1111
154.73.29.161:8080
189.240.60.163:9090
23.134.91.47:3128
85.209.153.173:4444
85.209.153.173:5678
85.209.153.175:3128
161.34.40.116:3128
189.240.60.168:9090
213.230.124.108:8088
89.35.237.187:80
109.108.107.122:8080
187.251.230.10:3128
85.209.153.175:5678
85.209.153.175:80
85.209.153.175:4153
103.155.62.158:8080
109.72.232.217:8080
183.242.69.118:3218
66.54.106.56:8104
85.209.153.175:999
89.35.237.187:4444
160.86.242.23:8080
190.26.255.30:999
89.35.237.187:3128
119.252.167.130:41890
89.35.237.187:999
161.34.40.36:3128
122.3.41.154:8090
35.185.196.38:3128
189.240.60.169:9090
185.191.236.162:3128
89.35.237.187:4145
51.158.169.52:29976
122.155.165.191:3128
103.19.59.19:8080
67.206.213.202:3120
189.240.60.166:9090"""
    proxies = response.split("\n")
    proxy = random.choice(proxies)
    return {"http": proxy, "https": proxy}

def search_proxy():
    while True:
        proxies = get_random_proxy()
        try:
            response = requests.get("http://api.myip.com/", proxies=proxies, timeout=5)
            return (response.json())
        except requests.exceptions.RequestException as e:
            pass
        
print(search_proxy())