class Product(object):
    def __init__(self, price, name, weight, brand,cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    # def __init__(self, price, name, weight, brand,cost,status):
    #     self.price = price
    #     self.name = name
    #     self.weight = weight
    #     self.brand = brand
    #     self.cost = cost
    #     self.status = status
    def sell(self):
        self.status = "sold"
    def addTax(self,tax):
        #the price of the item including sales tax
        total = round(self.price * (1+tax),2)
        return total
    def Return(self,reason):
        if self.status != "sold":
            print "Item cannot be returned without being sold first"
            return self
        #If the item is being returned because it is defective change status to defective and change price to 0.
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in the box":#If it is being returned in the box, like new mark it as for sale.
            self.status = "for sale"
        elif reason == "open box":#If the box has been opened set status to used and apply a 20% discount.
            self.status = "used"
            self.price = round(self.price*.8,2)
        else:
            print "Status unchanged!!"
            print "Please reuse function Return() and use one of the following options:"
            print "defective, in the box, open box"
        return self
    def display_info(self):
        print "Price: ${}".format(self.price)
        print "Item Name: {}".format(self.name)
        print "Weight: {}oz".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Cost: ${}".format(self.cost)
        print "Status: {}".format(self.status)
        return self
python = Product(15.99,'Python','100','Langs',0)
bill = python.addTax(.07)
print "$" + str(bill)
python.sell()
python.Return("in the box")
python.display_info()
java = Product(100,'Java','100','Langs',0)
flask = Product(5,'Flask','100','environs',0)
django = Product(250,'Django','100','webpage',0)