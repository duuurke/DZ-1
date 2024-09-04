from Address import Address


class Mailing:
    def __init__(self, to_address: Address,
                 from_address: Address, cost, track):
        self.to_ad = to_address
        self.from_ad = from_address
        self.cost = cost
        self.track = track
