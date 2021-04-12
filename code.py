stock_list={"jio":200,"airtel":400,"vodafone":100}
stock_buyers={"jio":0,"airtel":0,"vodafone":0}
stock_sellers={"jio":0,"airtel":0,"vodafone":0}
stock_amount={"jio":0,"airtel":0,"vodafone":0}
current_price={"jio":200,"airtel":400,"vodafone":100}
cust_details=[["Kajal",3000]]
def Buy(cust_name):
    stock_name = input("Enter stock name")
    number=int(input("Enter no of stocks u want to buy?"))
    l=stock_list.keys()
    if stock_name in l:
        print("Stock Available")
        amount=stock_list.get(stock_name)*number
        for i in cust_details:
            if i[0] == cust_name:
                if i[1]<amount:
                    print("You dont have enough money")
                else:
                    stock_amount[stock_name] = stock_amount[stock_name] + amount
                    buyers = stock_buyers.get(stock_name) + 1
                    stock_buyers[stock_name] = buyers
                    current = stock_list.get(stock_name) + (0.02 * amount)
                    current_price[stock_name] = int(current)
                    for i in cust_details:
                        if i[0] == cust_name:
                            i[1] = i[1] - amount
                    Cust = Customer(cust_name, stock_name, number, i[1])
                    print(Cust)
                    tags = ["Name Of Stock", "Base Price", "Current Price", "No of Buyers", "Total Amount"]
                    l = [list(stock_list.keys()), list(stock_list.values()), list(current_price.values()),
                         list(stock_buyers.values()), list(stock_amount.values())]
                    b = [[], [], []]
                    for i in l:
                        count = 0
                        for j in i:
                            b[count].append(j)
                            count += 1
                    b.append(tags)
                    b.reverse()
                    for row in b:
                        print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))
    else:
        print("Stock Not Available")


def Sell(cust_name):
    for i in cust_details:
        if i[0] == cust_name:
            stock_name = input("Enter stock name")
            number = int(input("Enter no of stocks u want to sell?"))
            l=stock_list.keys()
            if stock_name in l:
                amount=current_price[stock_name]*number
                i[1]=i[1]+amount
                Cust=Customer(cust,stock_name,number,i[1])
                print(Cust)

                amt=stock_amount.get(stock_name)-amount
                stock_amount[stock_name]=stock_amount[stock_name]-amt
                sellers=stock_sellers.get(stock_name)+1
                stock_sellers[stock_name]=sellers
                current=stock_list.get(stock_name)+(0.02*amount)
                current_price[stock_name]=current

                tags = ["Name Of Stock", "Base Price", "Current Price", "No of Buyers", "Total Amount"]
                l = [list(stock_list.keys()), list(stock_list.values()), list(current_price.values()),
                        list(stock_sellers.values()), list(stock_amount.values())]
                b = [[], [], []]
                for i in l:
                    count = 0
                    for j in i:
                        b[count].append(j)
                        count += 1
                b.append(tags)
                b.reverse()
                for row in b:
                    print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))
            else:
                print("Stock not avaialable")



class Customer:
    def __init__(self,cust_name,stock_name,stock_number,amount):
        self.cust_name=cust_name
        self.stock_name=stock_name
        self.stock_number=stock_number
        self.amount=amount

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)







cust=input("Enter User Name")
for i in cust_details:
    if i[0]==cust:
        a = int(input("Enter additional amount u want to invest?"))
        i[1] = i[1] + a

        print("Choice 1:Market Order,Choice 2:Limit Order,Choice 3:Stop Order")
        ch = int(input("Enter Choice"))
        if ch == 1:
            tags = ["Name Of Stock", "Base Price", "Current Price", "No of Buyers", "Total Amount"]
            l = [list(stock_list.keys()), list(stock_list.values()), list(current_price.values()),
                 list(stock_buyers.values()),
                 list(stock_amount.values())]
            b = [[], [], []]
            for i in l:
                count = 0
                for j in i:
                    b[count].append(j)
                    count += 1
            b.append(tags)
            b.reverse()
            for row in b:
                print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))
            print("1:Buy,2:Sell")
            q = int(input("Enter 1 or 2"))
            if q == 1:
                Buy(i[0])
            if q == 2:
                ans = input("Do u have buyed stocks earlier?Yes Or No")
                if ans == "Yes" or "yes":
                    Sell(i[0])
                else:
                    print("You do not have stocks which you want to sell")
    else:
        a=int(input("Enter amount of investment?"))
        cust_details.append([cust,a])
        print("Choice 1:Market Order,Choice 2:Limit Order,Choice 3:Stop Order")
        ch = int(input("Enter Choice"))
        if ch == 1:
            tags = ["Name Of Stock", "Base Price", "Current Price", "No of Buyers", "Total Amount"]
            l = [list(stock_list.keys()), list(stock_list.values()), list(current_price.values()),
                 list(stock_buyers.values()),
                 list(stock_amount.values())]
            b = [[], [], []]
            for i in l:
                count = 0
                for j in i:
                    b[count].append(j)
                    count += 1
            b.append(tags)
            b.reverse()
            for row in b:
                print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))
            print("1:Buy,2:Sell")
            q = int(input("Enter 1 or 2"))
            if q == 1:
                Buy(cust)
            if q == 2:
                ans = input("Do u have buyed stocks earlier?Yes Or No")
                if ans == "Yes" or "yes":
                    Sell(cust)
                else:
                    print("You do not have stocks which you want to sell")
        break
