
import sys
import pandas as pd 

def GroupByOrderId():
    df = pd.read_csv("25_Trade_Information_20180626.csv")
    #print(df.head())
    selecteddf = df
    gpdf = df.groupby(['CustomerInfo','StockCode','BuySell'])
    print(gpdf.sum())
    return

def Testing():
    df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
        'foo', 'bar', 'foo', 'foo'],
        'B' : ['one', 'one', 'two', 'three',
        'two', 'two', 'one', 'three'],
        'C' : 1234,
        'D' : 3210})
    print(df.to_string())
    return
	

def main():
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored
    # file_parser(sys.argv[1],sys.argv[2])
    # file_parser2(sys.argv[1],sys.argv[2])
    # test_class()
    # Testing()
    GroupByOrderId()
    print( "Hello there...." )
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
    