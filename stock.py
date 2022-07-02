class Stock(object):
    def __init__(self):
        self.stock = 0

    def receive_stock(self, value):
        self.stock += value

