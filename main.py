import requests

try:

    r = requests.get("https://goog le.com")
    print(r.status_code)

    if r.status_code == 200:
        print(r.text)

except Exception as e:
    print("ada error", e)