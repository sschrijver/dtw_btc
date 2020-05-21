from cryptory import Cryptory
import pandas as pd
from fastdtw import fastdtw

from dtw.templates import HeadAndShoulders, HeadAndShouldersReverse, TripleTopRectangle
from dtw.utils import normalize, denormalize

cryptory_from_date = Cryptory(from_date="2019-01-01")

history_price_btc = cryptory_from_date.extract_coinmarketcap("bitcoin").sort_values(by=['date'])

list_of_dates = list(history_price_btc['date'])
list_of_closes = list(history_price_btc['close'])

len_list_of_closes = len(list_of_closes)

patterns = [
    HeadAndShoulders(),
    HeadAndShouldersReverse(),
    TripleTopRectangle()
]

calculations = []

for i, pattern in enumerate(patterns):
    len_template = len(pattern.get_pattern())

    window_size = len_template
    while window_size < len_list_of_closes:
        start_window: int = 0
        end_window: int = window_size - 1

        while end_window < len_list_of_closes:
            window = list_of_closes[start_window:end_window]
            minimum_close = min(window)
            maximum_close = max(window)

            normalized_data = [normalize(close_price, minimum_close, maximum_close) for close_price
                               in
                               window]

            minimum_value_pattern, maximum_value_pattern = pattern.get_min_max()

            denormalized_data_template = [
                denormalize(normalized_close_price, minimum_value_pattern, maximum_value_pattern)
                for
                normalized_close_price in normalized_data]

            distance, path = fastdtw(denormalized_data_template, pattern.get_pattern())

            calculations.append(
                {
                    "pattern": pattern.__class__.__name__,
                    "start_window": start_window,
                    "start_date": list_of_dates[start_window],
                    "end_window": end_window,
                    "end_date": list_of_dates[end_window],
                    "distance": distance
                })

            start_window = start_window + 1
            end_window = end_window + 1
        window_size = window_size + len_template

calculations_df = pd.DataFrame(calculations).sort_values(by=['distance'])
csv = calculations_df.to_csv('data/output.csv', index=False)

a = 1
