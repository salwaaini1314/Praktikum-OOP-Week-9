class Calon_Siswa:
    tahun_sekarang = 2025
    passing_grade = 75  

    def __init__(self, nama, tahun_lahir, nilai_rapor, nilai_tes):
        self.nama = nama
        self.tahun_lahir = tahun_lahir
        self.nilai_rapor = nilai_rapor
        self.nilai_tes = nilai_tes

    @property
    def umur(self):
        return Calon_Siswa.tahun_sekarang - self.tahun_lahir

    @classmethod
    def perhitungan_nilai_akhir(cls, nilai_rapor, nilai_tes):
        return (0.6 * nilai_rapor) + (0.4 * nilai_tes)

    @staticmethod
    def cek_penerimaan(nilai_akhir):
        if nilai_akhir >= Calon_Siswa.passing_grade:
            return "DITERIMA"
        else:
            return "TIDAK DITERIMA"
    
murid1 = Calon_Siswa("Salwa Nur Aini", 2010, 90, 84)

print(f"\n----- Pengumuman Hasil Seleksi Peserta Didik Baru SMA Negeri 1 -----")
print(f"\nNama Lengkap : {murid1.nama}")
print(f"Umur         : {murid1.umur} tahun")
print(f"Nilai Rapor  : {murid1.nilai_rapor}")
print(f"Nilai Tes    : {murid1.nilai_tes}")
nilai_akhir = Calon_Siswa.perhitungan_nilai_akhir(murid1.nilai_rapor, murid1.nilai_tes)
print(f"\nNilai Akhir  : {nilai_akhir:.2f}")
print(f"Status Penerimaan  : {Calon_Siswa.cek_penerimaan(nilai_akhir)}")
