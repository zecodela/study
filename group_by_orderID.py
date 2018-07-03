
import sys
import pandas as pd 


def GroupByOrderId():
    print("GroupByOrderId")
    #Load from csv
    df = pd.read_csv("25_Trade_Information_20180626.csv")
    #Select relevant columns
    selecteddf = df.loc[:,['CustomerInfo','StockCode','BuySell','AccountID','TradePrice','TradeSize']]
    #Add Consideration field
    selecteddf['Consideration'] = selecteddf['TradeSize'] * selecteddf['TradePrice']
    print(selecteddf.columns)
    #Group by fields (show in report)
    gpdf = selecteddf.groupby(['CustomerInfo','StockCode','BuySell'])
    #Aggregate by sum and count
    agggpdf = gpdf.agg({'TradePrice':'count','TradeSize':'sum','Consideration':'sum'})    
    #Rename
    sumgpdf = agggpdf.rename(columns={'TradePrice':'TradeCount'})
    print(sumgpdf.columns)
    #Add new field AvgPX....
    sumgpdf['AvgPx'] = sumgpdf['Consideration'] / sumgpdf['TradeSize']
    print(sumgpdf.columns)
    print("Write to csv")
    sumgpdf.to_csv('20180626_GroupbyOrderId.csv',sep=',')
    return




def run():
	GroupByOrderId()
	print("this is the end...")
if __name__ == '__main__':
	run()