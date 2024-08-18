from bs4 import BeautifulSoup
import requests
import time
import re
import pandas as pd

nifty_50_mapping = {
    r'adani ent': 'ADANIENT',
    r'adanient': 'ADANIENT',
    r'adani enterprises': 'ADANIENT',
    r'adani': 'ADANIENT',
    r'adani ports': 'ADANIPORTS',
    r'adaniports': 'ADANIPORTS',
    r'apollo hospitals': 'APOLLOHOSP',
    r'apollohosp': 'APOLLOHOSP',
    r'apollo hosp': 'APOLLOHOSP',
    r'asian paints': 'ASIANPAINT',
    r'asian paint': 'ASIANPAINT',
    r'asianpaint': 'ASIANPAINT',
    r'asianpaints': 'ASIANPAINT',
    r'axis bank': 'AXISBANK',
    r'axisbank': 'AXISBANK',
    r'axis': 'AXISBANK',
    r'bajaj-auto': 'BAJAJ-AUTO',
    r'bajaj auto': 'BAJAJ-AUTO',
    r'bajajauto': 'BAJAJ-AUTO',
    r'bajaj finance': 'BAJFINANCE',
    r'bajajfinance': 'BAJFINANCE',
    r'bajaj fin': 'BAJFINANCE',
    r'bajajfin': 'BAJFINANCE',
    r'bajaj finserv': 'BAJAJFINSV',
    r'bajaj finsv': 'BAJAJFINSV',
    r'bajajfinsv': 'BAJAJFINSV',
    r'bpcl': 'BPCL',
    r'bharti airtel': 'BHARTIARTL',
    r'bhartiairtel': 'BHARTIARTL',
    r'airtel': 'BHARTIARTL',
    r'britannia': 'BRITANNIA',
    r'cipla': 'CIPLA',
    r'coal india': 'COALINDIA',
    r'coalindia': 'COALINDIA',
    r'divis lab': 'DIVISLAB',
    r'divislab': 'DIVISLAB',
    r'drreddy': 'DRREDDY',
    r'dr reddy': 'DRREDDY',
    r'dr reddy\'s': 'DRREDDY',
    r'drreddy\'s': 'DRREDDY',
    r'eichermot': 'EICHERMOT',
    r'eicher motors': 'EICHERMOT',
    r'eicher motor': 'EICHERMOT',
    r'grasim': 'GRASIM',
    r'hcltech': 'HCLTECH',
    r'hcl tech': 'HCLTECH',
    r'hdfc bank': 'HDFCBANK',
    r'hdfcbank': 'HDFCBANK',
    r'hdfc life': 'HDFCLIFE',
    r'hdfclife': 'HDFCLIFE',
    r'heromotoco': 'HEROMOTOCO',
    r'hero moto': 'HEROMOTOCO',
    r'heromoto co': 'HEROMOTOCO',
    r'heromoto corp': 'HEROMOTOCO',
    r'hindalco': 'HINDALCO',
    r'hindustan unilever': 'HINDUNILVR',
    r'hindunilvr': 'HINDUNILVR',
    r'icicibank': 'ICICIBANK',
    r'icici bank': 'ICICIBANK',
    r'itc': 'ITC',
    r'indusind bank': 'INDUSINDBK',
    r'indusindbank': 'INDUSINDBK',
    r'infosys': 'INFY',
    r'infy': 'INFY',
    r'jswsteel': 'JSWSTEEL',
    r'jsw steel': 'JSWSTEEL',
    r'ltim': 'LTIM',
    r'ltim mindtree': 'LTIM',
    r'mindtree': 'LTIM',
    r'kotakbank': 'KOTAKBANK',
    r'kotak bank': 'KOTAKBANK',
    r'lt': 'LT',
    r'larsen': 'LT',
    r'm&m': 'M&M',
    r'maruti': 'MARUTI',
    r'ntpc': 'NTPC',
    r'nestleind': 'NESTLEIND',
    r'nestle ind': 'NESTLEIND',
    r'nestle': 'NESTLEIND',
    r'ongc': 'ONGC',
    r'powergrid': 'POWERGRID',
    r'reliance': 'RELIANCE',
    r'ril': 'RELIANCE',
    r'sbi life': 'SBILIFE',
    r'sbilife': 'SBILIFE',
    r'shriramfin': 'SHRIRAMFIN',
    r'shriram fin': 'SHRIRAMFIN',
    r'shriram finance': 'SHRIRAMFIN',
    r'sbi': 'SBIN',
    r'sbin': 'SBIN',
    r'sunpharma': 'SUNPHARMA',
    r'sun pharma': 'SUNPHARMA',
    r'tcs': 'TCS',
    r'tata consultancy': 'TCS',
    r'tataconsum': 'TATACONSUM',
    r'tata consumer': 'TATACONSUM',
    r'tata consumers': 'TATACONSUM',
    r'tata motors': 'TATAMOTORS',
    r'tatamotors': 'TATAMOTORS',
    r'tata steel': 'TATASTEEL',
    r'tatasteel': 'TATASTEEL',
    r'techm': 'TECHM',
    r'tech mahindra': 'TECHM',
    r'titan': 'TITAN',
    r'ultracemco': 'ULTRACEMCO',
    r'ultra cement': 'ULTRACEMCO',
    r'wipro': 'WIPRO'
}

data = []
html_text=requests.get('https://economictimes.indiatimes.com/archivelist/year-2020,month-1,starttime-43831.cms').text
soup=BeautifulSoup(html_text,'lxml')
date=soup.find('td',class_='contentbox5')
date_f=date.find('b',recursive=False).text
#print(date_f.text)
news_all=soup.find_all('li')
for news in news_all:
    if news.a and news.a.text:
        if 'Most Read' in news.a.text:
            break
        news_li = news.a.text
        for stock,ticker in nifty_50_mapping.items():
            if re.search(r'\b'+re.escape(stock)+r'\b', news_li, re.IGNORECASE):
                #print(news_li)
                data.append([date_f,news_li,ticker])

df=pd.DataFrame(data,columns=['Date','News','Ticker'])
df_unique = df.drop_duplicates()
df_unique.to_csv('nifty_50_news.csv',index=False)
print("Data has been saved to nifty_50_news.csv")





