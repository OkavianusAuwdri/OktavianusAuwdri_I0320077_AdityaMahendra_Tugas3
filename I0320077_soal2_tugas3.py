# Membuat Dictionary
Biodata={'Nama':'Oktavianus Auwdri', 'Hobi':['Basket', 'Berenang', 'Nonton'], 'Sosial Media':['Instagram', 'Facebook', 'Twitter'], 'Lagu Kesukaan':['Karena Aku Tahu Engkau Begitu', 'Sesuatu di Jogja', 'Kesepian'], 'Makanan Favorit':['Kepiting','Indomie', 'Pizza']}
print("Biodata Awal: ", Biodata, '\n')

# Mengubah salah satu dari 'Hobi' dan 'Sosial Media'
Biodata['Hobi'][1] = 'Main Game'
Biodata['Sosial Media'][1] = 'Tiktok'
print("Setelah salah satu hobi diganti: ", Biodata['Hobi'])
print("Setelah salah satu sosial media diganti: ", Biodata['Sosial Media'], '\n')

# Mengahpus 2 'Makanan Favorit'
del Biodata['Makanan Favorit'][1:3]

# Menambahkan 1 'Hobi'
Biodata['Hobi'].append('Futsal')
print(Biodata)