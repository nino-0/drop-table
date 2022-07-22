from pynput import mouse

from drop_sistem import DropSistem


class App:
    def __init__(self) -> None:
        self.dpSistem = DropSistem()
        self.count = 0


    def on_click(self,x, y, button, pressed):
        
        if pressed:
            print(self.dpSistem.dropItem()," tentativa de numero: ",self.count)
            self.count += 1
        if self.count >= 100:
            self.count = 0
    def start(self):

        # Collect events until released
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

        # ...or, in a non-blocking fashion:
        listener = mouse.Listener(on_click=self.on_click)
        listener.start()