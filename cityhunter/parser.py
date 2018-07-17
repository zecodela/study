
import sys
import pandas as pd 
import re

def GroupByOrderId(inputfile):
    #print("GroupByOrderId")
    #Load from csv
    df = pd.read_csv(inputfile)
    print ("Select relevant columns")
    selecteddf = df.loc[:,['CustomerInfo','StockCode','BuySell','AccountID','TradePrice','TradeSize']]
    print("Add Consideration field")
    selecteddf['Consideration'] = selecteddf['TradeSize'] * selecteddf['TradePrice']
    #print(selecteddf.columns)
    print("Group by fields (show in report)")
    gpdf = selecteddf.groupby(['CustomerInfo','StockCode','BuySell'])
    print("Aggregate by sum and count")
    agggpdf = gpdf.agg({'TradePrice':'count','TradeSize':'sum','Consideration':'sum'})    
    print("Rename")
    sumgpdf = agggpdf.rename(columns={'TradePrice':'TradeCount'})
    #print(sumgpdf.columns)
    print("Add new field AvgPX")
    sumgpdf['AvgPx'] = sumgpdf['Consideration'] / sumgpdf['TradeSize']
    #print(sumgpdf.columns)
    print("Write to csv...")
    outfile = inputfile.split('.')[0] +'_OrderFile.csv'
    print("output file: " + outfile)
    sumgpdf.to_csv(outfile,sep=',')
    return


def Find(pat, text):
	results = re.findall(pat, text)
	for result in results:
		print (result)
	#for i, val in enumerate(strlist):
	#    print i, val

def Split(pat, text):
	print(re.split(pat, text))


def run():
	#Find("data=.*", "name=\"jim lo\" data=cat")
	file = open("output.txt", "r")
	txt = file.readline()
	txt.decode('utf8')
	Find("(title=\")(.*)(\"|\s)", txt)

	#encoded = '\xe4\xbb\x8a\xe5\xa4\xa9\xe5\xa4\xa9\xe6\xb0\xa3\xe7\x9c\x9f\xe5\xa5\xbd'
	#msg = encoded.decode('utf8')
	#print msg

	
if __name__ == '__main__':
	run()