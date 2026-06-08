class Address:
    def __init__(self, index, city, street, house, room):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.room = room

    def __str__(self):
        return f'{self.index}, {self.city}, {self.street}, {self.house} - {self.room}'
