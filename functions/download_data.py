import pandas as pd
import yfinance as yf

def download_data(
        tickers: str,
        multi_level_index = False
) -> pd.DataFrame:
    """
    Download the data from yahoo finance.

    Args:
        tickers (str): The ticker.
        multi_level_index (bool): Remove/include row indexs
    """
    result = yf.download(
    tickers="AAPL",
    multi_level_index= False
).reset_index()

    return result