
import yfinance as yf
import pandas as pd

#get stock tickers
def get_company_data():
 # Read and print the stock tickers that make up S&P500
    company_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
    return company_data



if __name__ == "__main__":
    company_data=get_company_data()
    print(company_data.Symbol[0],company_data.Security[0])