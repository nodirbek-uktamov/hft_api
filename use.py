from pprint import pprint

from ftx import FTX

ftx = FTX('zF8Wk8v_Rquq1OVSn5em_RWWtfiuxCkUzjqZ095s', 'sHFNJpUDYJ7j-hbNO76XMXBwkrUK4-7y9ySIEDp2')
pprint(
    ftx.place_order(
        market='TRX-PERP',
        side="buy",
        type="limit",
        size=4,
        price=0.01
    )
)
