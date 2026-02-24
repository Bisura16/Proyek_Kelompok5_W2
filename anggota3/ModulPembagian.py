def bagi(a: float, b: float) -> float:
    """
    Mengembalikan hasil pembagian dua angka.
    Akan menampilkan error jika pembagi = 0.
    """
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol.")
    return a / b