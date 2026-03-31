import threading
import time

class Supplier():
    def __init__(self, name, workers,):
        self.name = name
        self.workers = workers
        self.supply = 5
        self.thread = threading.Thread(target=self.produce, kwargs={"delay": 2})
        self.productionRate=0
    def produce(self):

        self.produce()

    def getSupply(self):
        return self.supply
    def getProductionRate(self):
        return self.productionRate
    
    def __str__(self):
        return f"{self.name} production rate:"+str(self.productionRate)
