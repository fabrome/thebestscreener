{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import yfinance as yf\
\
# D\'e9finition des crit\'e8res de s\'e9lection\
min_revenue_growth_rate = 0.1  # taux de croissance du chiffre d'affaires minimum de 10%\
min_earnings_growth_rate = 0.15  # taux de croissance des b\'e9n\'e9fices minimum de 15%\
min_future_growth_rate = 0.2  # potentiel de croissance future minimum de 20%\
min_ROE = 0.15  # Retour sur les capitaux propres minimum de 15%\
max_debt_equity_ratio = 1.5  # ratio d'endettement maximum de 1.5\
min_cash_ratio = 0.1  # ratio de tr\'e9sorerie minimum de 10%\
\
# R\'e9cup\'e9ration des donn\'e9es des entreprises\
tickers = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'FB', 'NVDA', 'TSLA', 'JPM', 'BAC', 'V', 'MA']\
financial_data = yf.download(tickers, period='max')\
\
# Calcul des crit\'e8res de s\'e9lection\
revenue_growth_rate = financial_data['Revenue'].pct_change().mean()\
earnings_growth_rate = financial_data['Net Income'].pct_change().mean()\
future_growth_rate = revenue_growth_rate * (1 + min_future_growth_rate)\
ROE = financial_data['Net Income'] / financial_data['Total Equity']\
debt_equity_ratio = financial_data['Total Debt'] / financial_data['Total Equity']\
cash_ratio = financial_data['Cash'] / financial_data['Total Assets']\
\
# Filtrage des entreprises r\'e9pondant aux crit\'e8res de s\'e9lection\
selected_companies = financial_data[(revenue_growth_rate >= min_revenue_growth_rate)\
                                    & (earnings_growth_rate >= min_earnings_growth_rate)\
                                    & (future_growth_rate >= revenue_growth_rate + min_future_growth_rate)\
                                    & (ROE >= min_ROE)\
                                    & (debt_equity_ratio <= max_debt_equity_ratio)\
                                    & (cash_ratio >= min_cash_ratio)]\
}