class Customer:
    def __init__(self, name, state, city, country):
        self.name = name
        self.customerAddress = self.Address(state, city, country)
    
    class Address:
        def __init__(self, state, city, country):
            self.state = state
            self.city = city
            self.country = country
        
        def display(self):
            print(self.state)
            print(self.city)
            print(self.country)

c1 = Customer('nitin', 'delhi', 'delhi', 'india')
c1.customerAddress.display()