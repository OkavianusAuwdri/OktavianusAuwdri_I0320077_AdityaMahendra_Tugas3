# List nama teman sebanyak 10
teman = ['David', 'Louis', 'Kevin', 'Erwin', 'Igen', 'Yoga', 'Kenji', 'Jose', 'Angel', 'Dora']

# Isi indeks nomor 4,6,7
print("Isi list indeks nomor 4: ", teman[4])
print("Isi list indeks nomor 6: ", teman[6])
print("isi list indeks nomor 7: ", teman[7], '\n')

# Ganti nama teman pada indeks 3,5,9
# Saya asumsikan yang dimaksud (3,5,9) itu indeks bukan orang ke- (3,5,9)
teman[3] = 'Maria'
teman[5] = 'Billy'
teman[9] = 'Vito'
print("List nama teman setelah diganti: ", teman, '\n')

# Penambahan 2 nama teman
teman.extend(["Jonathan", "Andrew"])
print("List nama teman setelah ditambahan: ", teman, '\n')

# Menampilkan semua teman dengan perulangan
i = 1
for tmn in teman:
    print(str(i) + '. ' + tmn, '\n')
    i += 1

# Tampilkan panjang list
print("Panjang list teman : ", len(teman))
