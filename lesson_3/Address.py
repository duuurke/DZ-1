class Address:
 
    def __init__(self, index, city, street, house, apartment):
          self.index = index
          self.citi = city
          self.street = street
          self.house = house
          self.apartment = apartment
          
    def __str__(self): return f"{self.index}, {self.citi}, {self.street}, {self.house} - {self.apartment}"