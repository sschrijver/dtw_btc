# Dynamic Time Warping (DTW) on close prices BTC

Based on: Pattern Extraction in Stock Market data by Suresh Rajagopal  
Link: cs.uccs.edu/~jkalita/work/StudentResearch/RajagopalSureshMSProject2016.pdf

Should definitely be revisited! Current included patterns:  

- Head and Shoulders
- Head and Shoulders Reversed/Inversed
- Triple Top Rectangle

## Output (create a data folder inside the project root folder):

```
pattern,            start_window,       start_date,     end_window,     end_date,       distance
HeadAndShoulders,   392,                2020-01-28,     398,            2020-02-03,     3.696194635059329
HeadAndShoulders,   298,                2019-10-26,     304,            2019-11-01,     3.8192712918524414
HeadAndShoulders,   30,                 2019-01-31,     36,             2019-02-06,     4.479216058163451
HeadAndShoulders,   64,                 2019-03-06,     70,             2019-03-12,     4.532003859761982
HeadAndShoulders,   311,                2019-11-08,     317,            2019-11-14,     4.533216900651558
```

Where pattern, start date, end date and distance are the most important

```
pattern             start_date      end_date        distance
HeadAndShoulders    2020-01-28      2020-02-03      3.696194635059329
```


## How to run
Make sure you've installed poetry. Within the project folder run:

```
poetry shell
```

```
poetry install
```

```
poetry run python src/dtw/main.py
```
