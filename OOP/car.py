class Car:
    def __init__(self, maker, model, year, color, for_sale):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the  {self.year} {self.color} {self.maker} {self.model}.")  # Fixed: self.maker

    def stop(self):
        print(f"You stopped the {self.maker} {self.color} {self.model}.")   # Fixed: self.maker

    def sale(self):
        if self.for_sale:
            print("ON SALE!!")
        else:
            print("NOT ON SALE.")
