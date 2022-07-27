import hmac
import time
from requests import Request, Session


class FTX:
    api_key = ''
    secret_key = ''
    sub_account = None
    FTX_REST_API = 'https://ftx.com/api'

    def __init__(self, api_key, secret_key, sub_account=None, FTX_REST_API=None):
        print('init')
        self.api_key = api_key
        self.secret_key = secret_key
        self.sub_account = sub_account

        if FTX_REST_API:
            self.FTX_REST_API = FTX_REST_API

    def send_request(self, endpoint, method, json=None, params=None):
        ts = int(time.time() * 1000)
        request = Request(method, self.FTX_REST_API + endpoint)

        if json:
            request.json = json

        if params:
            request.params = params

        prepared = request.prepare()
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()

        if prepared.body:
            signature_payload += prepared.body

        signature = hmac.new(self.secret_key.encode(), signature_payload, 'sha256').hexdigest()

        prepared.headers['FTX-KEY'] = self.api_key
        prepared.headers['FTX-SIGN'] = signature
        prepared.headers['FTX-TS'] = str(ts)

        if self.sub_account:
            prepared.headers['FTX-SUBACCOUNT'] = self.sub_account

        session = Session()
        response = session.send(prepared)

        return response.json()

    def get_positions(self):
        return self.send_request('/positions?showAvgPrice=true', 'GET')

    def get_account_information(self):
        return self.send_request('/account', 'GET')

    def get_balances(self):
        return self.send_request('/wallet/balances', 'GET')

    def get_open_orders(self):
        return self.send_request('/orders', 'GET')

    def get_orders_history(self, market=None):
        """
        market : None | str
            None - All orders

            "ETH-PERP" - orders of "ETH-PERP" instrument
        """

        return self.send_request(f'/orders/history', 'GET', params={'market': market})

    def get_trigger_orders(self, market=None):
        """
        market : None | str
            None - All trigger orders

            "ETH-PERP" - trigger orders of "ETH-PERP" instrument
        """

        return self.send_request(f'/conditional_orders', 'GET', params={'market': market})

    def get_twap_orders(self, market=None, status=None):
        """
        market : None or str
            None - All TWAP orders

            "ETH-PERP" - TWAP orders of "ETH-PERP" instrument

        status : None or str
            None - All TWAP orders
            "running" - TWAP orders with status running
        """

        return self.send_request(f'/twap_orders', 'GET', params={'market': market, 'status': status})

    def place_order(
            self,
            market: str,
            side: str,
            type: str,
            size: float,
            price: float = None,
            reduceOnly: bool = False,
            ioc: bool = False,
            postOnly: bool = False,
            clientId: str = None,
            rejectOnPriceBand: bool = False,
            rejectAfterTs: int = None
    ):
        """
        :param market: "ETH-PERP" or "ETH-USDT"
        :param side: "buy" or "sell"
        :param price: 0.306525 or None on market
        :param type: "limit" or "market"
        :param size: 31431.05
        :param reduceOnly: True or False
        :param ioc: True or False
        :param postOnly: True or False
        :param clientId: "3005422e-5906-466f-933b-bf28913aa32f" or None
        :param rejectOnPriceBand: True or False
        :param rejectAfterTs: 1234567 or None
        :return:
        {
            'result': {
                'avgFillPrice': None,
                'clientId': None,
                'createdAt': '2022-07-27T05:25:40.531060+00:00',
                'filledSize': 0.0,
                'future': 'TRX-PERP',
                'id': 166473993086,
                'ioc': False,
                'liquidation': None,
                'market': 'TRX-PERP',
                'postOnly': False,
                'price': 0.01,
                'reduceOnly': False,
                'remainingSize': 4.0,
                'side': 'buy',
                'size': 4.0,
                'status': 'new',
                'type': 'limit'
            },
            'success': True
        }

        """

        data = {
            'market': market,
            'side': side,
            'price': price,
            'type': type,
            'size': size,
            'reduceOnly': reduceOnly,
            'ioc': ioc,
            'postOnly': postOnly,
            'clientId': clientId,
            'rejectOnPriceBand': rejectOnPriceBand,
            'rejectAfterTs': rejectAfterTs,
        }

        if type == 'limit' and not price:
            raise Exception('Price is required on limit order')

        response = self.send_request('/orders', 'POST', json=data)
        return response

    def place_trigger_order(self, data):
        response = self.send_request('/conditional_orders', 'POST', json=data)
        return response

    def place_twap_order(self, data):
        response = self.send_request('/twap_orders', 'POST', json=data)
        return response
