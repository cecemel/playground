import bitstamp.client as bitstamp_client
import getpass
import json
import sys
import time
import datetime


def start():
    print('-'*10 + 'hello day trader ' + '-'*10)
    # today' update
    print('-'*10 + print_dict(get_todays_market_status()) + '-'*10)

    user = getpass.getpass('please provide user: ')
    key = getpass.getpass('please provide key: ')
    secret = getpass.getpass('please provide secret: ')

    print(secret)
    print(key)
    print(user)
    client = init_trading_client(user.strip(), key.strip(), secret.strip())

    print('-' * 10 + 'account status' + '-' * 10)
    print('-' * 10 + print_dict(get_current_account_status(client)) + '-' * 10)

    sell_amount = input('how much BTC do you want to sell today?')
    sell_price = input('At what price? ($)')
    buy_price = input('And your buy price in would be? ($)')

    print('you want to sell: ' + sell_amount + ' BTC at ' + sell_price)
    print("you'll buy in again at " + buy_price)
    ask_user_confirmation()
    short_dict = calculate_short_profit(sell_amount, sell_price, buy_price)
    print_short_profit(short_dict)
    ask_user_confirmation()
    print('placing order')
    order = place_sell_order(client, sell_amount, sell_price)
    wait_for_order_to_fullfill(client, order)
    print('ok, now placing buy order')
    order = place_buy_order(client, short_dict['total_buy_in'], buy_price)
    wait_for_order_to_fullfill(client, order)
    print('ok, yes :-) this should be nice')
    print('exiting')


def get_todays_market_status():
    public_client = bitstamp_client.Public()
    return public_client.ticker()


def init_trading_client(user, key, secret):
    return bitstamp_client.Trading(username = user, key = key, secret = secret)


def get_current_account_status(client):
    return client.account_balance()


def place_sell_order(client, amount, price):
    return client.sell_limit_order(amount, price, base="btc", quote="usd", limit_price=None)


def place_buy_order(client, amount, price):
    return client.buy_limit_order(amount, price, base="btc", quote="usd", limit_price=None)


def wait_for_order_to_fullfill(client, order):
    order_status = 'open'
    counter = 0
    update_after_iteration = 100
    sleep_time = 10

    while order_status != 'finished' :
        order_status = client.order_status(order['id'])['status'].lower()

        if counter % update_after_iteration == 0:
            print('current order status is :' + order_status)
            print('time:' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

        time.sleep(sleep_time)

    print('X' * 10 + 'ORDER COMPLETED' + 'X' * 10)
    print('time: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    print('order: ' + print_dict(order))
    print('X' * 30)


def calculate_short_profit(sell_amount, sell_price, buy_price):
    bitstamp_fee = 0.0026 # note updated it as safety margin and rounding stuff
    sell_amount = float(sell_amount)
    sell_price = float(sell_price)
    buy_price = float(buy_price)

    diff_sell_buy = (1 - sell_amount/buy_price)*100
    total_sell = sell_amount * sell_price - bitstamp_fee * sell_amount * sell_price
    total_buy_in = (total_sell - total_sell * bitstamp_fee)/buy_price

    return {'diff_sell_buy': diff_sell_buy, 'total_sell': total_sell, 'total_buy_in': total_buy_in}


def print_short_profit(short_dict):
    print(10 * '#' + 'To resume, we hope: ' + 10 * '#')
    print('diff between sell and buy: ' + '%.5f' % short_dict['diff_sell_buy'] + '%')
    print('total sell price: ' + str(short_dict['total_sell']) + '$')
    print('total amount buy in: ' + str(short_dict['total_buy_in']) + 'BTC')


def ask_user_confirmation():
    answer = input('please confirm (y/n)...')
    if answer == 'y':
        return
    print('ok, exiting...')
    sys.exit()


def print_dict(dict_instance):
    return json.dumps(dict_instance, indent=4)

if __name__ == "__main__":
    start()