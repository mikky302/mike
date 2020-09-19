#note seller should fill the below before running the program
name = ["Omonije Micheal"]
item = ["coke", "cheese", "cake"]#seller should input the names of items bought by the buyer
numberofitems = 3
quantity = [3, 1, 5]#seller should input the quantities of item
price = [50, 70, 100]#seller should input the price of item

myFile = open('Receipt.txt','w')
myFile.write("Name:")
for p in range(0, len(name)):
    myFile.write(name[p]+'\n')
myFile.write("--------------------------------------\n")
myFile.write("ITEM\tQUANTITY\tPRICE\n")
myFile.write("--------------------------------------\n")

for i in range (0,len(item)):
    myFile.write(item[i]+'\t\t')
    myFile.write(str(quantity[i])+'\t')
    myFile.write(str(price[i])+'\n')
myFile.write("--------------------------------------\n")

total = 0
for j in range (0,len(item)):
    temp = (quantity[j])*(price[j])
    total = total+temp
myFile.write('\t\tTotal\t'+str(total)+'\n')
myFile.write("--------------------------------------\n")
Vat = 0
MTotal = 0
#if items is less than 5 remove the # in front of the code below
if numberofitems < 5 :
    vats = (total*20)/100.0
    Vat = Vat+vats
    MTotal = vats + total
if numberofitems > 10:
    vats = (total*30)/100.0
    Vat = Vat+vats
    MTotal = vats + total - 800
myFile.write("\t\tVat:\t"+str(vats)+'\n')
myFile.write("--------------------------------------\n")
myFile.write("\t\tMTotal:\t"+str(MTotal)+'\n')
myFile.write("--------------------------------------\n")
myFile.close()
with open('Receipt.txt','r') as f:
    f_content = f.read()
    print(f_content)
