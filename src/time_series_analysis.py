import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, kpss

def plot_price_series(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Price'])
    plt.title("Brent Oil Price (USD/barrel)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def adf_test(series):
    result = adfuller(series)
    return {"ADF Statistic": result[0], "p-value": result[1]}

def kpss_test(series):
    statistic, p_value, _, _ = kpss(series, regression='c', nlags="auto")
    return {"KPSS Statistic": statistic, "p-value": p_value}
