# import modules used here -- sys is a very standard one
import sys

def file_parser(filename, orderID):
   f = open(filename, 'rU')
   for line in f:
      #print(line)
      if line.find(orderID) > 0:
         vals = line.split("^")
         if vals[0] == "NewOrder":
            print(line.replace('^','\t'), end=" ")
         elif vals[0] == "Executionreport":
            print(line.replace('^','\t'), end=" ")
         elif vals[0] == "ReplaceOrder":
            orderID = vals[2] #change orderID after amendment
            print(line.replace('^','\t'), end=" ")
   f.close()
   return
def file_parser2(filename, session):   
   f = open(filename, 'rU')
   orders = {}    
   for line in f:		
        #print(line)
        vals = line.split("^")
        if vals[24] == session or vals[25] == session:
           if vals[0] == "NewOrder":
               #NewOrdId, OrdId, OrigOrdId, Symbol, Side, ClientId, LmtPrc, Qty, VolDone, AvgPrc, DayVolDone, DayAvgPrc, NewTimeStamp, UpdateTimeStamp, LastFillTimeStamp, Currency, Sedol, Isin, SecurityName, Exchange, Text, Account)
               order = Order(vals[2],vals[2],vals[3],vals[6],vals[12],vals[4],vals[14],vals[13],0,0,0,0,vals[1],vals[1],0,vals[15],vals[8],vals[7],vals[10],vals[11],vals[30],vals[5])
               orders[vals[2]] = order
               #print(orders[vals[2]].NewOrdId,orders[vals[2]].OrdId,orders[vals[2]].OrigOrdId,orders[vals[2]].Symbol)            
           elif vals[0] == "Executionreport" and vals[23] == "trade":  
               #print(vals[0],'\t',vals[1],'\t',vals[2],'\t',vals[3],'\t',vals[18],'\t',vals[19],'\t',vals[20],'\t',vals[21],'\t',vals[22],'\t',vals[23],'\t',vals[24],'\t',vals[25],'\t',vals[26])                
               if vals[2] in orders: 
                   order = orders[vals[2]]
                   order.Qty =  vals[13]
                   order.LmtPrc =  vals[14]
                   order.VolDone =  vals[20]
                   order.AvgPrc =  vals[21]
                   order.UpdateTimeStamp = vals[1]
                   order.LastFillTimeStamp = vals[1]
           elif vals[0] == "Executionreport" and (vals[23] == "replace" or vals[23] == "cancel"):
               #print(vals[0],'\t',vals[1],'\t',vals[2],'\t',vals[3],'\t',vals[18],'\t',vals[19],'\t',vals[20],'\t',vals[21],'\t',vals[22],'\t',vals[23],'\t',vals[24],'\t',vals[25],'\t',vals[26])                
               if vals[3] in orders:   #use OrgOrdId to find previous order
                   order = orders[vals[3]]
                   order.OrdId = vals[2]
                   order.OrigOrdId = vals[3]
                   order.Qty =  vals[13]
                   order.LmtPrc =  vals[14]
                   order.VolDone =  vals[20]
                   order.AvgPrc =  vals[21]
                   order.Text =  vals[30]
                   order.UpdateTimeStamp = vals[1]
                   orders[vals[2]] = order #assign new Id as key for same record
           elif vals[0] == "Executionreport" and (vals[23] == "doneforday" or vals[23] == "reject"):
               if vals[2] in orders: 
                   order = orders[vals[2]]
                   order.Qty =  vals[13]
                   order.LmtPrc =  vals[14]
                   order.VolDone =  vals[20]
                   order.AvgPrc =  vals[21]
                   order.UpdateTimeStamp = vals[1]
   f.close()
   orders2 = {}    
   for key in orders.keys(): 
      order = orders[key]
      orders2[order.NewOrdId] = order # group the list with NewOrdId      
   print("key | NewOrdId | OrdId | OrigOrdId | Symbol | Side | ClientId | LmtPrc | Qty | VolDone | AvgPrc | DayVolDone | DayAvgPrc | NewTimeStamp | UpdateTimeStamp | LastFillTimeStamp | Currency | Sedol | Isin | SecurityName | Exchange | Text | Account")
   for key in orders2.keys(): 
      order = orders2[key]  
      print(key,'|',order.NewOrdId,'|',order.OrdId,'|',order.OrigOrdId,'|',order.Symbol,'|',order.Side,'|',order.ClientId,'|',order.LmtPrc,'|',order.Qty,'|',order.VolDone,'|',order.AvgPrc,'|',order.DayVolDone,'|',order.DayAvgPrc,'|',order.NewTimeStamp,'|',order.UpdateTimeStamp,'|',order.LastFillTimeStamp,'|',
      order.Currency,'|', order.Sedol,'|', order.Isin,'|', order.SecurityName,'|',order.Exchange,'|',order.Text,'|',order.Account)

   #print(orders.items())
   return
    
def test_class():
    orders = {}
    order = Order(0,0,0,"1.HK",0,0,0,0,0,0,0,0,0,0)
    orders[0] = order
    order = Order(0,0,0,"2.HK",0,0,0,0,0,0,0,0,0,0)
    orders[1] = order
    if 3 in orders:   
        print(orders[3].NewOrdId)
        print(orders[3].OrdId)
        print(orders[3].OrigOrdId)
        print(orders[3].Symbol)
    
class Order:
    NewOrdId = 0
    OrdId = 0
    OrigOrdId = 0
    Symbol = ""
    Side = ""
    ClientId = ""
    LmtPrc = 0
    Qty = 0
    VolDone = 0
    AvgPrc = 0
    DayVolDone = 0
    DayAvgPrc = 0
    NewTimeStamp = 0
    UpdateTimeStamp = 0
    LastFillTimeStamp = 0
    Currency = ""
    Sedol = ""
    Isin = ""
    SecurityName = ""
    Exchange = ""
    Text = ""
    Account = ""
    def __init__(self, NewOrdId, OrdId, OrigOrdId, Symbol, Side, ClientId, LmtPrc, Qty, VolDone, AvgPrc, DayVolDone, DayAvgPrc, NewTimeStamp, UpdateTimeStamp, LastFillTimeStamp, Currency, Sedol, Isin, SecurityName, Exchange, Text, Account):
        self.NewOrdId=NewOrdId
        self.OrdId=OrdId
        self.OrigOrdId=OrigOrdId
        self.Symbol=Symbol
        self.Side=Side
        self.ClientId=ClientId
        self.LmtPrc=LmtPrc
        self.Qty=Qty
        self.VolDone=VolDone
        self.AvgPrc=AvgPrc
        self.DayVolDone=DayVolDone
        self.DayAvgPrc=DayAvgPrc
        self.NewTimeStamp=NewTimeStamp
        self.UpdateTimeStamp=UpdateTimeStamp
        self.LastFillTimeStamp=LastFillTimeStamp
        self.Currency=Currency
        self.Sedol=Sedol
        self.Isin=Isin
        self.SecurityName=SecurityName
        self.Exchange=Exchange
        self.Text=Text
        self.Account=Account
	
# Gather our code in a main() function
def main():    
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored
    #file_parser(sys.argv[1],sys.argv[2])
    file_parser2(sys.argv[1],sys.argv[2])
    #test_class()
    #print( "Hello there" )
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
    