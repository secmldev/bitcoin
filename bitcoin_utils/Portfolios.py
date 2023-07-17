import pandas as pd
import matplotlib.pyplot as plt


def create_portfolio(buy_sell):
    positions = buy_sell["buy_sell_signal"].cumsum()
    holdings = positions*buy_sell["Adj Close"]
    cash = -(buy_sell["buy_sell_signal"].values)*buy_sell["Adj Close"]
    cash = cash.cumsum() 
    portfolio = pd.DataFrame({"holdings":holdings , "cash":cash})
    portfolio["Total_value"] = portfolio["holdings"]+portfolio["cash"]
    return portfolio

def Plot_portfolio(data):
    data["Total_value"].plot(figsize = (16,4) , grid = True)
    
    