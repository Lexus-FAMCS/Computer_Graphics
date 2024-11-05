import tkinter as tk
from tkinter import Canvas
import time
import math

class RasterizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Алгоритмы растеризации")

        self.attemps = 100
        
        self.canvas = Canvas(root, width=850, height=850, bg="white")
        self.canvas.pack(side="left")
        
        self.controls = tk.Frame(root)
        self.controls.pack(side="right", fill="y")
        
        tk.Label(self.controls, text="Выберите алгоритм:").pack()

        self.selected_algorithm = tk.StringVar(value="Step-by-Step")
        for algo in ["Пошаговый", "ЦДА", "Алгоритм Брезенхема", "Алгоритм Брезенхема(окружность)"]:
            tk.Radiobutton(self.controls, text=algo, variable=self.selected_algorithm, value=algo).pack()
        
        tk.Label(self.controls, text="Старт (x1, y1):").pack()
        self.x1_entry = tk.Entry(self.controls)
        self.x1_entry.pack()
        self.y1_entry = tk.Entry(self.controls)
        self.y1_entry.pack()
        
        tk.Label(self.controls, text="Конец (x2, y2) / Радиус:").pack()
        self.x2_entry = tk.Entry(self.controls)
        self.x2_entry.pack()
        self.y2_entry = tk.Entry(self.controls)
        self.y2_entry.pack()
        
        tk.Button(self.controls, text="Нарисовать", command=self.draw).pack()

        tk.Label(self.controls, text="Маштаб сетки:").pack()
        self.grid_scale = tk.Scale(self.controls, from_=20, to=40, orient="horizontal", command=self.update_grid)
        self.grid_scale.set(10)
        self.grid_scale.pack()

    def draw(self):
        x1 = int(self.x1_entry.get())
        y1 = int(self.y1_entry.get())
        x2 = int(self.x2_entry.get())
        y2 = int(self.y2_entry.get())
        
        self.canvas.delete("all")
        self.draw_grid()
        start_time = time.time()
        if self.selected_algorithm.get() == "Пошаговый":
            self.step_by_step(x1, y1, x2, y2)
        elif self.selected_algorithm.get() == "ЦДА":
            self.dda(x1, y1, x2, y2)
        elif self.selected_algorithm.get() == "Алгоритм Брезенхема":
            self.bresenham_line(x1, y1, x2, y2)
        elif self.selected_algorithm.get() == "Алгоритм Брезенхема(окружность)":
            self.bresenham_circle(x1, y1, x2)
        end_time = time.time()
        print(f"Среднее время выполнения {self.selected_algorithm.get()} на {self.attemps} попыток: {(end_time - start_time) / self.attemps * 10**6:.5f} микросекунд")

    def draw_pixel(self, x, y):
        scale = self.grid_scale.get()
        self.canvas.create_rectangle(x * scale, y * scale, x * scale + scale, y * scale + scale, fill="black")

    def draw_grid(self):
        scale = self.grid_scale.get()
        for i in range(0, 800, scale):
            # Вертикальные линии и метки
            self.canvas.create_line([(i, 0), (i, 800)], fill="gray")
            self.canvas.create_text(i + 5, 5, text=str(i // scale), anchor="nw", fill="black")
            
            # Горизонтальные линии и метки
            self.canvas.create_line([(0, i), (800, i)], fill="gray")
            self.canvas.create_text(5, i + 5, text=str(i // scale), anchor="nw", fill="black")
        self.canvas.create_line([(i + scale, 0), (i + scale, 800)], fill="gray")
        self.canvas.create_line([(0, i + scale), (800, i + scale)], fill="gray")
        
        # Добавляем метку оси X в правом верхнем углу
        self.canvas.create_text(830, 1, text="x", anchor="ne", fill="black", font=("Arial", 14, "bold"))
        
        # Добавляем метку оси Y в нижнем левом углу
        self.canvas.create_text(5, 830, text="y", anchor="sw", fill="black", font=("Arial", 14, "bold"))


    def update_grid(self, _):
        self.canvas.delete("all")
        self.draw_grid()

    def step_by_step(self, x1, y1, x2, y2):
        for _ in range(self.attemps):
            dx, dy = x2 - x1, y2 - y1
            steps = max(abs(dx), abs(dy))
            x_inc, y_inc = dx / steps, dy / steps
            x, y = x1, y1
            # print(f"текущая точка: ({x}, {y})")
            for _ in range(steps):
                self.draw_pixel(round(x), round(y))
                x += x_inc
                y += y_inc
                # print(f"текущая точка: ({x}, {y})")
            x, y = x2, y2
            self.draw_pixel(x, y)

    def dda(self, x1, y1, x2, y2):
        for _ in range(self.attemps):
            dx, dy = x2 - x1, y2 - y1
            steps = max(abs(dx), abs(dy))
            x_inc, y_inc = dx / steps, dy / steps
            x, y = x1, y1
            for _ in range(steps):
                self.draw_pixel(round(x), round(y))
                x += x_inc
                y += y_inc
            x, y = x2, y2
            self.draw_pixel(x, y)

    def bresenham_line(self, x1, y1, x2, y2):
        for _ in range(self.attemps):
            dx, dy = abs(x2 - x1), -abs(y2 - y1)
            sx = 1 if x1 < x2 else -1
            sy = 1 if y1 < y2 else -1
            err = dx + dy
            while True:
                self.draw_pixel(x1, y1)
                if x1 == x2 and y1 == y2:
                    break
                e2 = err * 2
                if e2 > dy:
                    if x1 == x2:
                        break
                    err += dy
                    x1 += sx
                if e2 < dx:
                    if y1 == y2:
                        break
                    err += dx
                    y1 += sy

    def bresenham_circle(self, xc, yc, r):
        for _ in range(self.attemps):
            x, y = 0, r
            d = 3 - 2 * r
            while y >= x:
                self.draw_circle_points(xc, yc, x, y)
                x += 1
                if d > 0:
                    y -= 1
                    d += 4 * (x - y) + 10
                else:
                    d += 4 * x + 6
                self.draw_circle_points(xc, yc, x, y)

    def draw_circle_points(self, xc, yc, x, y):
        points = [(x, y), (y, x), (-x, y), (-y, x), (-x, -y), (-y, -x), (x, -y), (y, -x)]
        for px, py in points:
            self.draw_pixel(xc + px, yc + py)

root = tk.Tk()
app = RasterizationApp(root)
root.mainloop()
