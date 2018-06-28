
import sys
import pandas as pd 

def GroupByOrderID():
	df = pd.read_csv("trade_file.csv")
	print(df.info())
	#print (df.head())
	#print (df.index)
	#df.set_index('symbol')
	#print (df.columns)
	#print (df.describe())
	grouped = df.groupby(['orderID'])	
	print(grouped.sum())
	return

def GroupByOrderId():
    #Load from csv
    df = pd.read_csv("25_Trade_Information_20180626.csv")
    #Select relevant columns
    selecteddf = df.loc[:,['CustomerInfo','StockCode','BuySell','TradePrice','TradeSize']]
    #Add Consideration field
    #df['Consideration'] = df
    #Group by fields (show in report)
    gpdf = selecteddf.groupby(['CustomerInfo','StockCode','BuySell'])
    print(gpdf.sum())
    return


def GroupByOrderID2():
	ipl_data = {'orderID': ['a001','a001','a001','a002','a002'],
				'tradePx': ['100.1','100.15','100.2','20.0','20.1'],
				'tradeVol': ['10000','1000','100','2000','3000'],
				"symbol": ['1.hk','1.hk','1.hk','2.hk','2.hk'],
				"side": ['b','b','b','s','s']}
	df = pd.DataFrame(ipl_data)
	print (df)			
 	print (df.groupby(['orderID','symbol','side']).groups)
 	return

def run():
	GroupByOrderId()
	print("this is the end...")
if __name__ == '__main__':
	run()