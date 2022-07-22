
from time import sleep
from drop_sistem import DropSistem


class Run:
    def __init__(self) -> None:
        self.dpSistem = DropSistem()
        self.count = 0
    
    def start(self):
        
        while True:
            self.count += 1
            item = self.dpSistem.dropItem()
            print(item," tentativa: ",self.count)
            if item['drop_rate'] == 1:
                print("DROPOHUUUUUU JAKSDFKAKSÇDFK")
                breakpoint()
            sleep(1)