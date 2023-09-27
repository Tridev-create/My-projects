import requests
import json
from sys import argv

Ans = float(argv[1])

try:
    if len(argv) != 2:
        exit('Missing command-line argument')
    else:
        Get = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        json.dumps(Get.json(), indent=2)
        Data = Get.json()
        Price = Data['bpi']['USD']['rate']
        Price_re = Price.replace(",", "")
        Price_float = float(Price_re)
        Summary = Price_float * Ans

        print(f"${Summary:,.4f}")

except requests.RequestException:
    exit('')
