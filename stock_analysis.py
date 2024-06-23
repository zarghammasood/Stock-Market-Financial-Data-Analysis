
import yfinance as yf
import pandas as pd
import psycopg2


def connection_to_postgresql():
    connection = psycopg2.connect(database="stock_data", user="postgres", password="Qwerty_12345", host="localhost", port=5432)
    return connection.cursor()

def get_company_names(company_data):
    return company_data['Security']

def get_tickers(company_data):
    return company_data['Symbol']

def get_sector(company_data):
    return company_data['GICS Sector']

def get_industry(company_data):
    return company_data['GICS Sub-Industry']

def populate_companies_table(list_of_companies,list_of_sector,list_of_industry):
    f = open("insert_command_for_companies_table.sql", "w")
    for i in range(len(list_of_companies)):
        f.write("Insert into companies(name,sector,industry) values('"+list_of_companies[i]+"','"+list_of_sector[i]+"','"+list_of_industry[i]+"');\n")
    f.close()

def populate_stocks_table(list_of_tickers):
    f = open("insert_command_for_stocks_table.sql", "w")
    for i in range(len(list_of_tickers)):
        f.write("Insert into stocks(symbol,company_id) values('"+list_of_tickers[i]+"',"+str(i+1)+");\n")
    f.close()

def get_company_data():
 # Read and print the stock tickers that make up S&P500
    company_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
    return company_data



if __name__ == "__main__":

    cursor=connection_to_postgresql()
    cursor.execute("SELECT * from companies;")
    # Fetch all rows from database
    record = cursor.fetchall()

    # print("Data from Database:- ", record)
    cursor.close()

    company_data=get_company_data()
    list_of_companies=get_company_names(company_data)
    list_of_tickers=get_tickers(company_data)
    list_of_sector=get_sector(company_data)
    list_of_industry=get_industry(company_data)

    # populate_companies_table(list_of_companies,list_of_sector,list_of_industry)

    populate_stocks_table(list_of_tickers)


    # for i in range(len(list_of_companies)):
    #     print(list_of_companies[i],list_of_tickers[i],list_of_industry[i])