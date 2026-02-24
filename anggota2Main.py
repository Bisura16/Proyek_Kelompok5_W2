# main.py

# Import modul dari masing-masing folder anggota
from anggota1 import clear, memory
from anggota3.ModulPembagian import bagi
from anggota3.ModulPerkalian import kali
from anggota4.tambah import tambah
from anggota4.kurang import kurang
from anggota5.akarkuadrat import akarkuadrat
from anggota5.persen import persen

def tampilkan_menu():
    print("\n" + "="*30)
    print("KALKULATOR KELOMPOK 5")
    print("="*30)
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Akar Kuadrat (√x)")
    print("6. Persentase (%)")
    print("7. Tampilkan Memori (MR)")
    print("8. Reset Kalkulator (AC)")
    print("9. Keluar")
    print("="*30)

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-9): ")

        if pilihan == '9':
            print("Keluar dari program. Terima kasih!")
            break

        # Menangani fitur Reset dan Memori
        if pilihan == '8':
            clear.all_clear()
            print("[Info] Kalkulator telah di-reset (AC).")
            continue
        
        if pilihan == '7':
            print(f"[Memori] Nilai memori saat ini: {memory.memory_recall()}")
            continue

        # Memastikan pilihan valid sebelum meminta input angka
        if pilihan not in ['1', '2', '3', '4', '5', '6']:
            print("[Error] Pilihan tidak valid. Silakan coba lagi.")
            continue

        try:
            # Operasi yang hanya butuh 1 angka (Akar Kuadrat)
            if pilihan == '5':
                angka = float(input("Masukkan angka: "))
                hasil = akarkuadrat(angka)
                print(f"\n[Hasil] √{angka} = {hasil}")
                clear.set_last_result(hasil)

            # Operasi yang butuh 2 angka
            else:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))

                if pilihan == '1':
                    hasil = tambah(angka1, angka2)
                    print(f"\n[Hasil] {angka1} + {angka2} = {hasil}")
                elif pilihan == '2':
                    hasil = kurang(angka1, angka2)
                    print(f"\n[Hasil] {angka1} - {angka2} = {hasil}")
                elif pilihan == '3':
                    hasil = kali(angka1, angka2)
                    print(f"\n[Hasil] {angka1} * {angka2} = {hasil}")
                elif pilihan == '4':
                    hasil = bagi(angka1, angka2)
                    print(f"\n[Hasil] {angka1} / {angka2} = {hasil}")
                elif pilihan == '6':
                    hasil = persen(angka1, angka2) # Asumsi: angka1 adalah nilai, angka2 adalah total
                    print(f"\n[Hasil] {angka1} adalah {hasil}% dari {angka2}")

                # Simpan hasil terakhir ke modul clear
                clear.set_last_result(hasil)

        except ValueError as e:
            # Menangkap error bawaan Python (salah ketik huruf) DAN error buatan (bagi nol)
            if "could not convert string to float" in str(e):
                print("\n[Error] Harap masukkan angka yang valid, bukan huruf!")
            else:
                print(f"\n[Error] {e}")
        except Exception as e:
            # Menangkap error tak terduga lainnya
            print(f"\n[Error Fatal] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()