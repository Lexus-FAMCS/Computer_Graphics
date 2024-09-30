import tkinter as tk
from tkinter import colorchooser
from colorsys import rgb_to_hsv, hsv_to_rgb, rgb_to_hls, hls_to_rgb


# Преобразование RGB в CMYK
def rgb_to_cmyk(r, g, b):
    r, g, b = [x / 255.0 for x in (r, g, b)]
    k = 1 - max(r, g, b)
    if k == 1:
        return 0, 0, 0, 1
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    return round(c * 100), round(m * 100), round(y * 100), round(k * 100)


# Преобразование CMYK в RGB
def cmyk_to_rgb(c, m, y, k):
    c, m, y, k = [x / 100.0 for x in (c, m, y, k)]
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    return round(r), round(g), round(b)


def update_colors():
    r = int(entry_r.get())
    g = int(entry_g.get())
    b = int(entry_b.get())

    # Обновление CMYK
    c, m, y, k = rgb_to_cmyk(r, g, b)
    entry_cmyk_c.delete(0, tk.END)
    entry_cmyk_c.insert(0, c)
    entry_cmyk_m.delete(0, tk.END)
    entry_cmyk_m.insert(0, m)
    entry_cmyk_y.delete(0, tk.END)
    entry_cmyk_y.insert(0, y)
    entry_cmyk_k.delete(0, tk.END)
    entry_cmyk_k.insert(0, k)

    # Обновление HSV
    h, s, v = rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    entry_hsv_h.delete(0, tk.END)
    entry_hsv_h.insert(0, round(h * 360))
    entry_hsv_s.delete(0, tk.END)
    entry_hsv_s.insert(0, round(s * 100))
    entry_hsv_v.delete(0, tk.END)
    entry_hsv_v.insert(0, round(v * 100))

    # Обновление HLS
    h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    entry_hls_h.delete(0, tk.END)
    entry_hls_h.insert(0, round(h * 360))
    entry_hls_l.delete(0, tk.END)
    entry_hls_l.insert(0, round(l * 100))
    entry_hls_s.delete(0, tk.END)
    entry_hls_s.insert(0, round(s * 100))


# Создание окна
root = tk.Tk()
root.title("Color Converter")

# Поля для RGB
tk.Label(root, text="R").grid(row=0, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=0, column=1)

tk.Label(root, text="G").grid(row=1, column=0)
entry_g = tk.Entry(root)
entry_g.grid(row=1, column=1)

tk.Label(root, text="B").grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)

# Поля для CMYK
tk.Label(root, text="C").grid(row=3, column=0)
entry_cmyk_c = tk.Entry(root)
entry_cmyk_c.grid(row=3, column=1)

tk.Label(root, text="M").grid(row=4, column=0)
entry_cmyk_m = tk.Entry(root)
entry_cmyk_m.grid(row=4, column=1)

tk.Label(root, text="Y").grid(row=5, column=0)
entry_cmyk_y = tk.Entry(root)
entry_cmyk_y.grid(row=5, column=1)

tk.Label(root, text="K").grid(row=6, column=0)
entry_cmyk_k = tk.Entry(root)
entry_cmyk_k.grid(row=6, column=1)

# Поля для HSV
tk.Label(root, text="H (HSV)").grid(row=7, column=0)
entry_hsv_h = tk.Entry(root)
entry_hsv_h.grid(row=7, column=1)

tk.Label(root, text="S (HSV)").grid(row=8, column=0)
entry_hsv_s = tk.Entry(root)
entry_hsv_s.grid(row=8, column=1)

tk.Label(root, text="V (HSV)").grid(row=9, column=0)
entry_hsv_v = tk.Entry(root)
entry_hsv_v.grid(row=9, column=1)

# Поля для HLS
tk.Label(root, text="H (HLS)").grid(row=10, column=0)
entry_hls_h = tk.Entry(root)
entry_hls_h.grid(row=10, column=1)

tk.Label(root, text="L (HLS)").grid(row=11, column=0)
entry_hls_l = tk.Entry(root)
entry_hls_l.grid(row=11, column=1)

tk.Label(root, text="S (HLS)").grid(row=12, column=0)
entry_hls_s = tk.Entry(root)
entry_hls_s.grid(row=12, column=1)

# Кнопка для обновления
tk.Button(root, text="Обновить", command=update_colors).grid(row=13, column=1)

root.mainloop()
