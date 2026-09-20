import requests
response = requests.get("http://httpbin.org/get")
print(response.status_code)
print(response.text)
response.close()