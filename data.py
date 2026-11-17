import pandas as pd
# Membuat tabel data sederhana
data = {
    'menu': ['Kopi Susu', 'Teh Manis', 'Roti Bakar'],
    'harga': [18000, 10000, 25000],
    'terjual': [120, 80, 45]
}

df = pd.DataFrame(data)
print(df)
# Hanya ingin melihat menu yang harganya di atas 15000
menu_mahal = df[df['harga'] > 15000]
print(menu_mahal)
