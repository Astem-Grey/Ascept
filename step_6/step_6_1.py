import time

import datetime
class Trafficlight:

        def __init__(self):
            self.color = {"Красный": 7, "Желтый": 2, "Зеленый": 10}

        def running(self):
            y = 0
            while True:
                y += 1
                for key in self.color:
                    print(key)
                    time.sleep(self.color.get(key))
                if y > 10000000:
                    print('Светофор закрывается на тех работы')
                    break



svet = Trafficlight()
print(svet.running())

