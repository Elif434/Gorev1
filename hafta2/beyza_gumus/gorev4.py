import random
import os 
import time

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

try:
  while True:
    mesafe = sensor.oku()
     
    if mesafe < 20:
       print(f"{mesafe} cm, DUR")

    if 20 <= mesafe <= 50:
       print(f"{mesafe} cm, YAVASLA")

    if mesafe> 50:
      print(f"{mesafe} cm, ILERI")
  
    time.sleep(0.5)

except KeyboardInterrupt:
  print("Robot durduruldu")

