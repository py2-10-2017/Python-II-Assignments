class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status="For sale!"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "Sold!"
        return self

    def add_tax(self, tax):
        return self.price + self.tax * self.price
        return self

    def exchange(self, reason):
        if reason == "Defective":
            self.status = reason
            self.price = 0

        elif reason == "in box":
            self.status = "For sale!"
            return self

        elif reason == "open box":
            self.status = "Used"
            self.price = self.price - (.20 * self.price)

        return self


    def display_info(self):
        print "Price: $" + str(self.price)
        print "Item: " + str(self.item_name)
        print "Weight: " + str(self.weight) + " lbs."
        print "Brand: " + str(self.brand)
        print "Cost: $" + str(self.cost)
        print "Status: " + str(self.status)
        return self

product1 = Product(35.00, "Fitted Hat", .7, "New Era", 13.49)
print product1.display_info().exchange("open box").display_info()
