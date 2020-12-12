"""
    Tipe data dictionary menghubungkan KEY dan VALUE
    KVP = Key Value Pair
    Dictionary = kamus
"""

# kamus_ind_eng = {'persegi': 'square', 'lingkaran': 'circle', 'segitiga': 'triangle', 'segienam': 'hexagon'}

kamus_ind_eng = {}
kamus_ind_eng['persegi'] = 'square'
kamus_ind_eng['lingkaran'] = 'circle'
kamus_ind_eng['segitiga'] = 'triangle'
kamus_ind_eng['segienam'] = 'hexagon'

print(kamus_ind_eng['segitiga'])


print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}

print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")