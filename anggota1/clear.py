# clear.py
# Modul fitur Clear (C) dan All Clear (AC)

import memory

last_result = 0


def set_last_result(value):
    """Update last_result, dipanggil setelah operasi hitung"""
    global last_result
    last_result = value
    return last_result

def get_last_result():
    """Ambil nilai last_result"""
    return last_result

def clear():
    """Reset hasil terakhir jadi 0 (C)"""
    global last_result
    last_result = 0
    return last_result

def all_clear():
    """Reset semua: hasil terakhir dan memori (AC)"""
    global last_result
    last_result = 0
    memory.memory_clear()
    return last_result, memory.memory
