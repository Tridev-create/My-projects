import requests
import json
from sys import argv

while True:
    print('')
    Ans = float(input('Bitcoins: '))
    print('EUR or USD???')
    Currency = str(input('Currency: '))


    try:
            Get = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            json.dumps(Get.json(), indent=2)
            Data = Get.json()
            US = Data['bpi']['USD']['rate']
            EU = Data['bpi']['EUR']['rate']
            Time = Data['time']['updated']
            US_re = US.replace(",", "")
            US_float = float(US_re)
            EU_re = EU.replace(",", "")
            EU_float = float(EU_re)

            if Currency == 'USD' or Currency == 'usd':
                Summary_US = US_float * Ans
                print('')
                print(f"Price is >> ${Summary_US:,.4f} << updated at {Time}")
                print('')
            elif Currency == 'EUR' or Currency == 'eur':
                Summary_EU = EU_float * Ans
                print('')
                print(f"Price is >> €{Summary_EU:,.4f} << updated at {Time}")
                print('')


    except requests.RequestException:
        print('')
        pass
    except TypeError:
        print('Only number')
        pass
    except ValueError:
        print('Please enter again')
        pass
