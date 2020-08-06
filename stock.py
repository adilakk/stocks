import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = '909IARO1RPRAPPSR'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MRNA', interval = '1min', outputsize = 'full')
print(data)

close_data = data['4. close']
percentage_change = close_data.pct_change()

print(percentage_change)

last_change = percentage_change[-1]

if abs(last_change) > 0.01:
    print("MRNA Alert:" + str(last_change))
