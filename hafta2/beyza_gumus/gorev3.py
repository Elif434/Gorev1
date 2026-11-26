import random
import os #klasör açmak için

os.makedirs("Veriler", exist_ok = True)

class MesafeSensoru:
  def __init__(self):
    self.okumalar = []

  def oku(self):
    deger = random.uniform(10,200)
    self.okumalar.append(deger)

    dosya = open("Veriler/sensor_log.csv", "a")
    dosya.write(f"{deger}\n")
    dosya.close()

    return deger
  def ortalama(self):
    son_bes_sayi = self.okumalar[-5:]
    toplam = 0
    for sayi in son_bes_sayi:
      toplam+= sayi
      return toplam / len(son_bes_sayi)

sensor = MesafeSensoru()

print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())


print("Son 5 okuma ortalaması:", sensor.ortalama())

