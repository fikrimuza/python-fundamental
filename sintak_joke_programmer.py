'''
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kalli selama/sampai kondisi terpenuhi
'''

# Skuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika telor, beli 6"')
print('Maka Budi berangkat ketoko')
print('dan mulai berbelanja')

#Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f'Jumlah botol susu {jumlah_botol_susu} btl')
print(f'Jumlah telur {jumlah_telur} butir')

if jumlah_botol_susu > 0:
    print('Budi mengecek harganya, dan ternyata uang cukup')
    if jumlah_telur == 0:
        print('Budi membeli 1 botol susu')
    else:
        print('Budi membeli 6 botol susu')
else:
    print('Budi tidak jadi membeli 1 botol susu')

print('Budi pulang kerumah')
print('Menyampaikan hasil kepada ibu')