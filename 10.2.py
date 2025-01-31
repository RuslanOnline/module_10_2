from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        enemies_power = 100
        num_days = 0
        print(f'{self.name}, на нас напали!')
        for i in range(enemies_power):
            if enemies_power > 0:
                enemies_power -= self.power
                num_days += 1
                sleep(1)
                print(f'{self.name} сражается {num_days} день(дня)..., осталось {enemies_power} войнов.')
                if enemies_power <= 0:
                    print(f'{self.name} одержал победу спустя {num_days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')




