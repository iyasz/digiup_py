class Animal(object):
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def tampil(self):
      print('Nama = ',self.name, 'Umur = ', self.age)