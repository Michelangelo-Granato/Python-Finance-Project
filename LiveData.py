import numpy as np 
import pandas as pandas
#data sources
import yfinance as yf
import alpha_vantage as av

#viz
import plotly.graph_objs as go

data = yf.download(tickers = 'UBER', period='1d', interval='1m')
#int 1minute

print(data)

fig = go.Figure()

#candle chart
fig.add_trace(go.Candlestick(x=data.index,
    open=data['Open'],
    high=data['High'],
    low =data['Low'],
    close=data['Close'],
    name = 'market data'))

#fig.update_layout(
   # title='Uber'
   # yaxis_title ='Stock Price')


fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        button=list([
            dict(count=15,label='15m',step='minute', stepmode='backward'),
            dict(count=45,label='45m',step='minute', stepmode='backward'),
            dict(count=1,label='HTD',step='hour', stepmode='todate'),
            dict(count=2,label='2h',step='hour', stepmode='backward'),
            dict(step = 'all')
        ])
    )
)

fig.show()