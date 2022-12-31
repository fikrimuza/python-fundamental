'''
Program perulangan membaca buku dengan while
'''

book_count = 10
print('Perintah ibu,"Baca semua bukumu"')
read_count = 0

understoof_count = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {understoof_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understoof_count == 5:
        print(f'Buku ke {understoof_count + 1} belum paham')
    else:
        understoof_count = understoof_count + 1
        print(f'Buku ke {understoof_count} sudah dibaca dan dipahami')

print(f'Jumlah buku yang sudah dibaca {understoof_count}')

if understoof_count == book_count:
    print('"Bu, seuma buku sudah di baca dan dipahami')
else:
    print(f'"Bu, tidak semua buku bisa saya pahami,'
          f' budi hanya memahami {understoof_count} buku')
