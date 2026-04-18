sonlar = [4, 9, 16, 25]
darajalar = [2, 3, 4, 5]
natijalar = [round(son ** (1.0 / daraja), 2) for son, daraja in zip(sonlar, darajalar)]
print(natijalar)
