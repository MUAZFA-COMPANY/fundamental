data = {
    'tanggal': '2020-10-20',
    'daftar_gojek': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}

print(f"Driver terdekat berjarak {data['daftar_gojek'][0]['jarak']} meter")