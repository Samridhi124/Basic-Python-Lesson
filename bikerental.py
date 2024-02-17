'''
display available stocks
request a bike for rent(100 rs-1 qn)
exit'''
class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes:", self.stock)

    def rentForBike(self, q):
        if q <= 0:
            print("Enter a positive value or greater than zero")
        elif q > self.stock:
            print("Enter a value less than the stock")
        else:
            self.stock -= q
            print("Total Prices:", q * 100)
            print("Total Bikes:", self.stock)

obj = BikeShop(100)

while True:
    uc = int(input('''
    1. Display Stocks
    2. Rent a Bike
    3. Exit
                    '''))

    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input("Enter The Qty-----"))
        obj.rentForBike(n)
    else:
        break