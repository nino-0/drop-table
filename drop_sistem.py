
import random

class DropSistem:
    def __init__(self) -> None:
        self.sample_space = 10000
        self.table_of_drops = [{"name":"long sword","drop_rate":9000},{"name":"short sword","drop_rate":999},{"name":"Big sword","drop_rate":1}]
            
    def dropItem(self):
        rand = random.randint(1,self.sample_space)

        for obj in self.table_of_drops:
            if rand <= obj['drop_rate']:
                return obj
            rand = rand - obj['drop_rate']
        
        return {"name":"undefined obj","drop_rate":0}

    