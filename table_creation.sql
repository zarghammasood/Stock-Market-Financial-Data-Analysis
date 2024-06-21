
-- Create Table companies(
-- 	company_id serial PRIMARY KEY UNIQUE NOT NULL,
-- 	name varchar(200),
-- 	sector varchar(100),
-- 	industry varchar(100)
-- );

-- Create Table Stocks(
-- 	stock_id serial PRIMARY KEY UNIQUE NOT NULL,
-- 	symbol varchar(10) UNIQUE NOT NULL,
-- 	company_id INT REFERENCES companies(company_id)
-- );
-- Create Table stock_price(
-- 	price_id serial PRIMARY KEY UNIQUE NOT NULL,
-- 	stock_id INT REFERENCES stocks(stock_id),
-- 	date timestamp NOT NULL,
-- 	open real NOT NULL,
-- 	close real NOT NULL,
-- 	volume real NOT NULL
	
-- );

-- Create Table dividends(
-- 	dividend_id serial PRIMARY KEY UNIQUE NOT NULL,
-- 	stock_id INT REFERENCES stocks(stock_id),
-- 	date timestamp NOT NULL,
-- 	dividend_amount real NOT NULL
-- );
