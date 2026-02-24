# memory.py
# Modul fitur Tombol Memori (M+, M-, MR, MC)

memory = 0


def memory_add(value):
    """Tambah value ke memori (M+)"""
    global memory
    memory = memory + value
    return memory

def memory_subtract(value):
    """Kurang value dari memori (M-)"""
    global memory
    memory = memory - value
    return memory

def memory_recall():
    """Ambil nilai memori sekarang (MR)"""
    return memory

def memory_clear():
    """Reset memori jadi 0 (MC)"""
    global memory
    memory = 0
    return memory
