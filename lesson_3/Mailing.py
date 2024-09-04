from Address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_ad = to_address
        self.from_ad = from_address
        self.cost = cost
        self.track = track

#def __str__(self): return (f' отправление {self.to_ad} из {self.from_ad}'
    #                       f' в {self.cost}. стоимость {self.track} рублей.')