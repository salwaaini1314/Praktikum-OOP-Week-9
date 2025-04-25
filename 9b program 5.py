from collections import namedtuple

Pet_Hotel = namedtuple('Pet_Hotel', 'no_kamar nama ras umur')

kucing1 = Pet_Hotel('02', 'Tompel', 'Kampung', '2 tahun')
kucing2 = Pet_Hotel('05', 'Louis', 'Mix-Dom', '1 tahun 6 bulan')
kucing3 = Pet_Hotel('07', 'Marko', 'Anggora', '4 tahun')

def tampilkan_data(penghuni):
    print(f"\n----- Identitas Kucing Kamar {penghuni.no_kamar} -----")
    print(f"\nNama    : {penghuni.nama}")
    print(f"Ras     : {penghuni.ras}")
    print(f"Umur    : {penghuni.umur}")

tampilkan_data(kucing1)
tampilkan_data(kucing2)
tampilkan_data(kucing3)
