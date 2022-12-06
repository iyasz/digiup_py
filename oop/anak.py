from animal import Animal

class Anak(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age,)
        self.color = color

    def tampil(self):
      print('Nama = ',self.name, 'Umur = ', self.age, 'Warna = ', self.color)    