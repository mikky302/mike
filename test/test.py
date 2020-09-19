data= {
    'listofitems' : [ 'Sugar','Bread (sliced)','Bread (unsliced)','Egg','Three crown (tin)','Peak milk (tin)','Peak milk (sachet)','bournvita (sachet)','Milo (tin)','Peak milk (Large Sachet)','Milo (Large Sachet)','Bournvita (Large Sachet)','Custard (small sachet)','Corn flakes (small sachet)','Golden morn (small sachet)','Detergent (small Wawu)','Detergent (small Aerial)','Detergent (Big Wawu)','Detergent (Big Aerial)','Corn flakes (big sachet)','Golden morn (Large sachet)','Sprite (small)','Pepsi (small)','Fanta (small)','Lacasera (small)','Sprite (big)','Pepsi (big)','Fanta (big)','Lacasera (big)','Coke (big)'],
    'priceofitems' : [ 131 ,311,229,545,201,230,791,611,367,889,934,758,383,647,121,198,354,323,222,341,458,134,674,757,127,956,374,267,786,546],
    'avabilityofitems' : [50,200,150,50,150,120,50,50,500,700,700,100,200,150,100,120,115,200,250,750,650,80,80,80,80,150,150,150,150,150]
    }
import pandas as pd
df = pd.DataFrame(data )
#to add new items
#new_row = pd.Series({
#     'listofitems' : 'Klin',
#     'priceofitems' : 131,
#     'avabilityofitems' : 21
#   })
#to change  price
#df.loc[2, 'priceofitems']= 1
#to change avability
#df.loc[2, 'avabilityofitems']= 1
#to delete items
#df.drop(0, axis = 0, inplace = True)
#df = df.append(new_row, ignore_index = True)
print(df)
nameofBuyer = str(input('What is your Name:'))
items= str(input('Name of Item:'))
quantitys = input('Quantity Of Item:')

i= str(input('Do You Need Another Item(Yes/No):'))
j = int(input('How Many More items Do You Need:'))
if i == 'Yes':
    for i in range(j):
         item = str(input('Name fo Item:'))
         quantity = input('Quantity Of Item:')
else:
    pass
x = str(input('Do You Need Receipt(Yes/No):'))
if x == 'Yes':
    print('Please patiently wait while your receipt is being generated')

#seller should run the receipt code
