from cryptory import Cryptory
import pandas as pd
from dtaidistance import dtw
import matplotlib.pyplot as plt
from dtaidistance import dtw_visualisation as dtwvis
from dtw_btc.templates import HeadAndShouldersTop, HeadAndShouldersBottom, TripleTopReversal, \
    DoubleTopReversal, FallingWedge, DoubleBottomReversal, RisingWedge, TripleBottomReversal, \
    BumpAndRunReversal, SymmetricalTriangle
from dtw_btc.utils import normalize, denormalize, normalize_function_paper

cryptory_from_date = Cryptory(from_date="2020-05-01")

history_price_btc = cryptory_from_date.extract_coinmarketcap("bitcoin").sort_values(by=['date'])

list_of_dates = list(history_price_btc['date'])
list_of_closes = list(history_price_btc['close'])

len_list_of_closes = len(list_of_closes)

patterns = [
    HeadAndShouldersTop(),
    HeadAndShouldersBottom(),
    TripleTopReversal(),
    DoubleTopReversal(),
    DoubleBottomReversal(),
    FallingWedge(),
    RisingWedge(),
    TripleBottomReversal(),
    BumpAndRunReversal(),
    SymmetricalTriangle()
]


def _get_min_max_close(window):
    return min(window), max(window)


def _calculate_dtw_over_time_window(window,
                                    minimum_close,
                                    maximum_close,
                                    pattern,
                                    start_window,
                                    end_window,
                                    threshold):
    calculations = []

    minimum_value_pattern, maximum_value_pattern = pattern.get_min_max()

    normalized_data = [
        normalize_function_paper(close_price, minimum_close, maximum_close, minimum_value_pattern,
                                 maximum_value_pattern) for close_price in window]
    # distance, path = fastdtw(normalized_data, pattern.get_pattern(), dist=euclidean)
    # alignment = dtw(normalized_data, pattern.get_pattern(), keep_internals=True)

    distance = dtw.distance(normalized_data, pattern.get_pattern())
    path = dtw.warping_path(normalized_data, pattern.get_pattern())

    if distance < threshold:

        calculations.append(
            {
                "pattern_name": pattern.__class__.__name__,
                "start_window": start_window,
                "start_date": list_of_dates[start_window],
                "end_window": end_window,
                "end_date": list_of_dates[end_window],
                "distance": distance,
                "path": path,
                "normalized_data": normalized_data,
                "pattern": pattern.get_pattern()
            })

    return calculations


def main():
    all_calculations = []

    for pattern in patterns:
        len_template = len(pattern.get_pattern())

        window_size = len_template
        while window_size < len_list_of_closes:
            start_window: int = 0
            end_window: int = window_size  # not -1 because thts not how array[x:y] works

            while end_window < len_list_of_closes:
                window = list_of_closes[start_window:end_window]
                minimum_close, maximum_close = _get_min_max_close(window)

                window_calculations = _calculate_dtw_over_time_window(
                    window=window,
                    minimum_close=minimum_close,
                    maximum_close=maximum_close,
                    pattern=pattern,
                    start_window=start_window,
                    end_window=end_window,
                    threshold=5)

                if window_calculations:
                    all_calculations = all_calculations + window_calculations

                start_window = start_window + 1
                end_window = end_window + 1
            window_size = window_size + len_template

    all_calculations_df = pd.DataFrame(all_calculations).sort_values(by=['distance'])
    csv = all_calculations_df.to_csv('data/output.csv', index=False)

    for i, row in all_calculations_df.iterrows():
        window = history_price_btc[(history_price_btc['date'] >= row['start_date']) & (
                history_price_btc['date'] <= row['end_date'])]

        plot_fig = window.plot(x='date', y='close').get_figure()
        plot_fig.savefig(
            f'data/imgs/{row["start_date"]}-{row["end_date"]}-{row["pattern_name"]}.png')
        plt.close(plot_fig)

        dtwvis.plot_warping(row['normalized_data'], row['pattern'], row['path'],
                            filename=f'data/imgs/{row["start_date"]}-{row["end_date"]}-{row["pattern_name"]}-dtw.png')


if __name__ == "__main__":
    main()
