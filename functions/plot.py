import plotly.express as px
from plotly.graph_objects import Figure
from functions.download_data import download_data

def plot_history(ticker:str) -> Figure:
    """
    Plot historical dataa from yahoo finance.

    Args:
        ticker (str): The ticker.
    """

    df = download_data(ticker)
    fig = px.line(
        df,
        x = 'Date',
        y = 'Close',
        title = f'{ticker} Stock Price'
    )
    return fig
