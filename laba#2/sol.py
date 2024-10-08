import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from matplotlib import pyplot as plt
from PIL import Image, ImageTk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")

        self.canvas = tk.Label(self.root)
        self.canvas.pack()

        self.load_button = ttk.Button(self.root, text="Загрузить изображение", command=self.load_image)
        self.load_button.pack()

        self.histogram_eq_button = ttk.Button(self.root, text="Эквализация гистограммы", command=self.histogram_equalization)
        self.histogram_eq_button.pack()

        self.linear_contrast_button = ttk.Button(self.root, text="Линейное контрастирование", command=self.linear_contrast)
        self.linear_contrast_button.pack()

        self.high_pass_filter_button = ttk.Button(self.root, text="Высокочастотный фильтр (резкость)", command=self.high_pass_filter)
        self.high_pass_filter_button.pack()

        self.image = None
        self.max_image_size = (1900, 1080)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image(self.image)

    def display_image(self, img):
        img_height, img_width = img.shape[:2]
        scale = min(self.max_image_size[0] / img_width, self.max_image_size[1] / img_height)
        if scale < 1: 
            img = cv2.resize(img, (int(img_width * scale), int(img_height * scale)))

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        self.canvas.config(image=img_tk)
        self.canvas.image = img_tk

    def histogram_equalization(self):
        if self.image is not None:
            hsv_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv_img)
            v_eq = cv2.equalizeHist(v)
            hsv_eq_img = cv2.merge((h, s, v_eq))
            eq_img = cv2.cvtColor(hsv_eq_img, cv2.COLOR_HSV2BGR)

            b, g, r = cv2.split(self.image)
            b_eq = cv2.equalizeHist(b)
            g_eq = cv2.equalizeHist(g)
            r_eq = cv2.equalizeHist(r)
            rgb_eq_img = cv2.merge((b_eq, g_eq, r_eq))

            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            plt.title("Эквализация в пространстве HSV")
            plt.imshow(cv2.cvtColor(eq_img, cv2.COLOR_BGR2RGB))
            plt.subplot(1, 2, 2)
            plt.title("Эквализация по каналам RGB")
            plt.imshow(cv2.cvtColor(rgb_eq_img, cv2.COLOR_BGR2RGB))
            plt.show()

    def linear_contrast(self):
        if self.image is not None:
            contrast_img = cv2.normalize(self.image, None, 0, 255, cv2.NORM_MINMAX)

            plt.figure(figsize=(10, 5))
            
            plt.subplot(1, 2, 1)
            plt.title("Исходное изображение")
            plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
            plt.axis('off')

            plt.subplot(1, 2, 2)
            plt.title("Контрастированное изображение")
            plt.imshow(cv2.cvtColor(contrast_img, cv2.COLOR_BGR2RGB))
            plt.axis('off')

            plt.show()

    def high_pass_filter(self):
        if self.image is not None:
            blurred = cv2.GaussianBlur(self.image, (5, 5), 0)

            sharpened = cv2.addWeighted(self.image, 2, blurred, -1, 0)

            plt.figure(figsize=(10, 5))

            plt.subplot(1, 2, 1)
            plt.title("Исходное изображение")
            plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
            plt.axis('off')

            plt.subplot(1, 2, 2)
            plt.title("Изображение с высоким контрастом")
            plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
            plt.axis('off')

            plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
