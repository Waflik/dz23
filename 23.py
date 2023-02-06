class Fridge:
    COUNT = 0
    def __init__(self, name="", amount=int, quality=""):
        self.name = name
        self.amount = amount
        self.quality = quality
    
    def open_fridge(self):
        Fridge.COUNT+=1
        return f'{Fridge.COUNT}) Наименование: {self.name}. Количество: {self.amount}. Состояние: {self.quality}'

banana = Fridge('Банан', 3, 'Спелый')
milk = Fridge('Молоко', 1, 'Прокисло')
beer = Fridge('Пивко', 5, 'Выпей меня!')

print(Fridge.__dict__)

print(Fridge.open_fridge(banana))
print(Fridge.open_fridge(milk))
print(Fridge.open_fridge(beer))
