
import sys
import pandas as pd 


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




def run():
    inputfile = sys.argv[1]
    if inputfile != "":
        print("Source file: " + inputfile)
        GroupByOrderId(inputfile)
    else:
        print("No input file provided.")
if __name__ == '__main__':
	run()