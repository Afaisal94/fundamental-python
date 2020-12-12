# SINTAKS DASAR PYTHON
# SEQUENTIAL = Eksekusi kode berurutan
print('Hello World!')
print('by Faisal')
print('Tanggal 12 Desember 2020')
print('-' * 20)


# 2. Percabangan(branching)  = eksekusi terpilih
# Membuat data / variabel

data = True

if data:
 print('Done')
 print('-' * 20)
else:
 print('NOT COMPLETE')
 print('-' * 20)

# 3. Perulangan(looping)
shape = 4

# perulangan dimulai dari 0
for shape in range(1, shape+1):
    # f = fungsi string terbaru di python untuk menysisipkan variable kedalam teks
    print(f'This is shape {shape}')