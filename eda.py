import pandas as pd

earns = pd.read_csv(
    r"C:\Users\mrkka\Desktop\Data\Earnings and qualifications\raw_earnings.csv"
)
quals = pd.read_csv(
    r"C:\Users\mrkka\Desktop\Data\Earnings and qualifications\raw_quals.csv"
)

quals = quals.dropna(subset="OBS_VALUE")

quals.info()
