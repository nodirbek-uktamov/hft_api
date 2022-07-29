from huobi import Huobi

ftx = Huobi('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Get all accounts list
accounts = ftx.get_accounts()

if accounts.get('status') == 'ok':
    spot_account = list(filter(lambda i: i['type'] == 'spot', accounts.get('data')))[0]

    ftx.change_account_id(spot_account.get('id'))

# Get symbols list
symbols = ftx.get_symbols()

# Get klines list
klines = ftx.get_klines('btcusdt')

# Get balances
balances = ftx.get_balances()

# Place limit order
limit_order_response = ftx.place_order(
    amount=101,
    symbol='trxusdt',
    price=0.05,
    type='buy-limit'
)

# Place marker order
market_order_response = ftx.place_order(
    amount=1,
    symbol='trxusdt',
    type='buy-market'
)
