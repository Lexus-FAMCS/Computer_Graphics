import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
import colorsys


class ColorConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Model Converter")

        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        self.color_display = tk.Label(self.root, bg="black", width=20, height=4)
        self.color_display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        #RGB Inputs
        self.rgb_label = ttk.Label(self.root, text="RGB:")
        self.rgb_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.r_value = tk.IntVar()
        self.g_value = tk.IntVar()
        self.b_value = tk.IntVar()
        
        self.r_entry = ttk.Entry(self.root, textvariable=self.r_value, width=5)
        self.r_entry.grid(row=1, column=1, padx=5, pady=5)

        self.g_entry = ttk.Entry(self.root, textvariable=self.g_value, width=5)
        self.g_entry.grid(row=1, column=2, padx=5, pady=5)

        self.b_entry = ttk.Entry(self.root, textvariable=self.b_value, width=5)
        self.b_entry.grid(row=1, column=3, padx=5, pady=5)

        self.r_slider = tk.Scale(self.root, from_=0, to=255, orient="horizontal", variable=self.r_value, command=lambda _: self.update_from_rgb())
        self.r_slider.grid(row=2, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        self.g_slider = tk.Scale(self.root, from_=0, to=255, orient="horizontal", variable=self.g_value, command=lambda _: self.update_from_rgb())
        self.g_slider.grid(row=3, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        self.b_slider = tk.Scale(self.root, from_=0, to=255, orient="horizontal", variable=self.b_value, command=lambda _: self.update_from_rgb())
        self.b_slider.grid(row=4, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        # CMYK Inputs
        self.cmyk_label = ttk.Label(self.root, text="CMYK:")
        self.cmyk_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")

        self.c_value = tk.DoubleVar()
        self.m_value = tk.DoubleVar()
        self.y_value = tk.DoubleVar()
        self.k_value = tk.DoubleVar()

        self.c_entry = ttk.Entry(self.root, textvariable=self.c_value, width=5)
        self.c_entry.grid(row=5, column=1, padx=5, pady=5)

        self.m_entry = ttk.Entry(self.root, textvariable=self.m_value, width=5)
        self.m_entry.grid(row=5, column=2, padx=5, pady=5)

        self.y_entry = ttk.Entry(self.root, textvariable=self.y_value, width=5)
        self.y_entry.grid(row=5, column=3, padx=5, pady=5)

        self.k_entry = ttk.Entry(self.root, textvariable=self.k_value, width=5)
        self.k_entry.grid(row=5, column=4, padx=5, pady=5)

        self.c_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient="horizontal", variable=self.c_value, command=lambda _: self.update_from_cmyk())
        self.c_slider.grid(row=6, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        self.m_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient="horizontal", variable=self.m_value, command=lambda _: self.update_from_cmyk())
        self.m_slider.grid(row=7, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        self.y_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient="horizontal", variable=self.y_value, command=lambda _: self.update_from_cmyk())
        self.y_slider.grid(row=8, column=1, columnspan=4, sticky="we", padx=5, pady=5)
        
        self.k_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient="horizontal", variable=self.k_value, command=lambda _: self.update_from_cmyk())
        self.k_slider.grid(row=9, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        # HSV Inputs
        self.hsv_label = ttk.Label(self.root, text="HSV:")
        self.hsv_label.grid(row=10, column=0, padx=5, pady=5, sticky="e")

        self.h_value = tk.DoubleVar()
        self.s_value = tk.DoubleVar()
        self.v_value = tk.DoubleVar()

        self.h_entry = ttk.Entry(self.root, textvariable=self.h_value, width=5)
        self.h_entry.grid(row=10, column=1, padx=5, pady=5)

        self.s_entry = ttk.Entry(self.root, textvariable=self.s_value, width=5)
        self.s_entry.grid(row=10, column=2, padx=5, pady=5)

        self.v_entry = ttk.Entry(self.root, textvariable=self.v_value, width=5)
        self.v_entry.grid(row=10, column=3, padx=5, pady=5)

        self.h_slider = tk.Scale(self.root, from_=0, to=360, orient="horizontal", variable=self.h_value, command=lambda _: self.update_from_hsv())
        self.h_slider.grid(row=11, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        self.s_slider = tk.Scale(self.root, from_=0, to=100, orient="horizontal", variable=self.s_value, command=lambda _: self.update_from_hsv())
        self.s_slider.grid(row=12, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        self.v_slider = tk.Scale(self.root, from_=0, to=100, orient="horizontal", variable=self.v_value, command=lambda _: self.update_from_hsv())
        self.v_slider.grid(row=13, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        self.choose_color_button = ttk.Button(self.root, text="Choose Color", command=self.choose_color)
        self.choose_color_button.grid(row=14, column=0, columnspan=5, pady=10)

    def bind_events(self):
        self.r_entry.bind("<KeyRelease>", lambda event: self.update_from_rgb())
        self.g_entry.bind("<KeyRelease>", lambda event: self.update_from_rgb())
        self.b_entry.bind("<KeyRelease>", lambda event: self.update_from_rgb())

        self.c_entry.bind("<KeyRelease>", lambda event: self.update_from_cmyk())
        self.m_entry.bind("<KeyRelease>", lambda event: self.update_from_cmyk())
        self.y_entry.bind("<KeyRelease>", lambda event: self.update_from_cmyk())
        self.k_entry.bind("<KeyRelease>", lambda event: self.update_from_cmyk())

        self.h_entry.bind("<KeyRelease>", lambda event: self.update_from_hsv())
        self.s_entry.bind("<KeyRelease>", lambda event: self.update_from_hsv())
        self.v_entry.bind("<KeyRelease>", lambda event: self.update_from_hsv())


    def update_from_rgb(self):
        r = self.r_value.get()
        g = self.g_value.get()
        b = self.b_value.get()

        c, m, y, k = self.rgb_to_cmyk(r, g, b)
        self.c_value.set(c)
        self.m_value.set(m)
        self.y_value.set(y)
        self.k_value.set(k)

        h, s, v = self.rgb_to_hsv(r, g, b)
        self.h_value.set(h)
        self.s_value.set(s)
        self.v_value.set(v)

        self.update_color_display(r, g, b)

    def update_from_cmyk(self):
        c = self.c_value.get()
        m = self.m_value.get()
        y = self.y_value.get()
        k = self.k_value.get()

        r, g, b = self.cmyk_to_rgb(c, m, y, k)
        self.r_value.set(r)
        self.g_value.set(g)
        self.b_value.set(b)

        h, s, v = self.rgb_to_hsv(r, g, b)
        self.h_value.set(h)
        self.s_value.set(s)
        self.v_value.set(v)

        self.update_color_display(r, g, b)

    def update_from_hsv(self):
        h = self.h_value.get()
        s = self.s_value.get()
        v = self.v_value.get()

        r, g, b = self.hsv_to_rgb(h, s, v)
        self.r_value.set(r)
        self.g_value.set(g)
        self.b_value.set(b)

        c, m, y, k = self.rgb_to_cmyk(r, g, b)
        self.c_value.set(c)
        self.m_value.set(m)
        self.y_value.set(y)
        self.k_value.set(k)

        self.update_color_display(r, g, b)

    def rgb_to_cmyk(self, r, g, b):
        if (r, g, b) == (0, 0, 0):
            return 0, 0, 0, 1

        r_prime = r / 255
        g_prime = g / 255
        b_prime = b / 255

        k = 1 - max(r_prime, g_prime, b_prime)
        c = (1 - r_prime - k) / (1 - k)
        m = (1 - g_prime - k) / (1 - k)
        y = (1 - b_prime - k) / (1 - k)

        return round(c, 2), round(m, 2), round(y, 2), round(k, 2)

    def cmyk_to_rgb(self, c, m, y, k):
        r = 255 * (1 - c) * (1 - k)
        g = 255 * (1 - m) * (1 - k)
        b = 255 * (1 - y) * (1 - k)

        return int(r), int(g), int(b)

    def rgb_to_hsv(self, r, g, b):
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        return round(h * 360, 2), round(s * 100, 2), round(v * 100, 2)

    def hsv_to_rgb(self, h, s, v):
        r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)
        return int(r * 255), int(g * 255), int(b * 255)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose color")[0]
        if color_code:
            r, g, b = map(int, color_code)
            self.r_value.set(r)
            self.g_value.set(g)
            self.b_value.set(b)
            self.update_from_rgb()

    def update_color_display(self, r, g, b):
        color_hex = f"#{r:02x}{g:02x}{b:02x}"
        self.color_display.config(bg=color_hex)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x1100")
    app = ColorConverterApp(root)
    root.mainloop()
