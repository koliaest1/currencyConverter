import json
import requests


def main():
    src_currency = input().lower()
    request = f'http://www.floatrates.com/daily/{src_currency}.json'
    r = requests.get(request)
    currencies = json.loads(r.content)
    currencies_count = len(currencies)
    cache = {}
    if src_currency != 'usd':
        usd = currencies['usd']['rate']
        cache['usd'] = usd
    if src_currency != 'eur':
        eur = currencies['eur']['rate']
        cache['eur'] = eur
    while True:
        if currencies_count == 0:
            break
        else:
            req_currency = input().lower()
            if req_currency == '':
                break
            amount = int(input())
            print('Checking the cache...')
            if req_currency in cache:
                converted = round(amount * cache[req_currency], 2)
                print('Oh! It is in the cache!')
                print(f'You received {converted} {req_currency}.')
                currencies_count -= 1
            else:
                currency = currencies[req_currency.lower()]
                converted = round(amount * currency['rate'], 2)
                print('Sorry, but it is not in the cache!')
                print(f'You received {converted} {req_currency}.')
                cache[currency['code'].lower()] = currency['rate']


if __name__ == "__main__":
    main()
