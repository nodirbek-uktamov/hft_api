# Exchanges
A small library for apis of huobi and ftx.

### Installation
```
pip install 
```

### Get started
There are ony 2 apis available right now Huobi, Ftx


### how to work with Huobi
```Python
from huobi import Huobis

huobi = Huobi('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Get all accounts list
accounts = huobi.get_accounts()

if accounts.get('status') == 'ok':
    spot_account = list(filter(lambda i: i['type'] == 'spot', accounts.get('data')))[0]

    huobi.change_account_id(spot_account.get('id'))

# Get open orders
open_orders = huobi.get_open_orders()

# Cancel order by id
cancel_response = huobi.cancel_order('596827573398451')

# Get symbols list
symbols = huobi.get_symbols()

# Get klines list
klines = huobi.get_klines('btcusdt')

# Get balances
balances = huobi.get_balances()

# Place limit order
limit_order_response = huobi.place_order(
    amount=101,
    symbol='trxusdt',
    price=0.05,
    type='buy-limit'
)

# Place marker order
market_order_response = huobi.place_order(
    amount=1,
    symbol='trxusdt',
    type='buy-market'
)

```

### How to work with FTX
```Python
from ftx import FTX
ftx = FTX('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Get positions list
ftx.get_positions()

# Get account information
ftx.get_account_information()

# Get account balances list
ftx.get_balances()

# Get all open orders
ftx.get_open_orders()

# Get all open orders for "ETH-PERP"
ftx.get_open_orders("ETH-PERP")

# Get orders history
ftx.get_orders_history()

# Get orders history for "ETH-PERP"
ftx.get_orders_history("ETH-PERP")

# Get open trigger orders
ftx.get_trigger_orders()

# Get open trigger orders for "ETH-PERP"
ftx.get_trigger_orders("ETH-PERP")

# Get all twap orders
ftx.get_twap_orders()

# Get all twap orders for "ETH-PERP"
ftx.get_twap_orders("ETH-PERP")

# Get all active twap orders for "ETH-PERP"
ftx.get_twap_orders("ETH-PERP", "running")

# Place limit order
ftx.place_order(
    market="ETH/USDT",
    side='buy',
    type='limit',
    size=1.2,
    price=1498,
    clientId="70bed756-228f-4325-8af4-3a75559cdf30"
)

# Place market order
ftx.place_order(
    market="ETH/USDT",
    side='buy',
    type='market',
    size=1.2,
    clientId="1fcf03f1-b110-46ef-9a07-be4c7c0e3a77"
)

# Place stop loss order:
ftx.place_trigger_order(
    market="ETH/USDT",
    side='sell',
    size=1.2,
    type='stop',
    triggerPrice=100,
)

# Place trailing stop order:
ftx.place_trigger_order(
    market="ETH/USDT",
    side='sell',
    size=1.2,
    type='trailingStop',
    trailValue=-0.05
)

# Place take profit order:
ftx.place_trigger_order(
    market="ETH/USDT",
    side='sell',
    size=1.2,
    type='takeProfit',
    triggerPrice=10000,
)

# Place twap order
ftx.place_twap_order(
    market="ETH/USDT",
    durationSeconds=600,
    size=1,
    side="buy"
)

```
