mesafeler = [4,1,5,8,14,18,25,28,39,45,458,252,59,766,361,78,973,85,88,100]

def en_buyuk_deger(veriler):
  en_buyuk = veriler[0]
  for sayi in veriler:
      if sayi> en_buyuk:
       en_buyuk = sayi 
  return en_buyuk

def en_kucuk_deger(veriler):
  en_kucuk = veriler[0]
  for sayi in veriler:
     if sayi < en_kucuk:
      en_kucuk = sayi
  return en_kucuk

def ortalama_hesapla(veriler):
  toplam = 0
  for sayi in veriler:
    toplam += sayi
  return toplam/ len(veriler)

print("-Ham Veriler-")
print(f"En küçük değer: {en_kucuk_deger(mesafeler)} cm")
print(f"En büyük değer: {en_buyuk_deger(mesafeler)} cm")
print(f"Ortalama değer: {ortalama_hesapla(mesafeler)} cm")

temiz = [ ]
for sayi in mesafeler:
  if 2<= sayi <= 400:
    temiz.append(sayi)

mesafeler = temiz


print("")
print("-Son Veriler-")
print(f"En küçük değer: {en_kucuk_deger(mesafeler)} cm")
print(f"En büyük değer: {en_buyuk_deger(mesafeler)} cm")
print(f"Ortalama değer: {ortalama_hesapla(mesafeler)} cm")
