import requests

proxies = {
        'https': 'http://59.15.154.69:13128'
}


response = requests.get("https://ipinfo.io/json", proxies=proxies)

# print(response.text)
print(response.json()['country'])
print(response.json()['region'])



