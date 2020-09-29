from numpy import corrcoef
from pandas_datareader import data
import math

from .prediction import make_prediction

def rmt_data(stock_id,stock_id2,date,date2):
    panel_data = data.DataReader(stock_id, 'yahoo', date, date2)
    close = panel_data['Close']
    panel_data2 = data.DataReader(stock_id2, 'yahoo', date, date2)
    close2 = panel_data2['Close']
    correlation(close,close2)

def correlation(close,close2):
    correlation_set = []
    correlation_degree = 5
    for i in range(4, correlation_degree + 1):
        print("Correlation degree = ", i)
        for j in range(len(close) - i + 1):
            corr = corrcoef(close[j:j + i], close2[j:j + i])[0][1]
            if not math.isnan(corr):
                correlation_set.append(corr)
    make_prediction(correlation_set)
