import tkinter as tk
from tkinter import messagebox
import numpy as np

class CalculadoraEcuacionesLineales:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Ecuaciones Lineales")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Centrar ventana
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        x = (ancho_pantalla - 800) // 2
        y = (alto_pantalla - 600) // 2
        self.root.geometry(f"800x600+{x}+{y}")

        # Colores y fuentes
        self.bg_color = "#f0f0f5"
        self.accent_color = "#4a86e8"
        self.text_color = "#333333"
        self.root.configure(bg=self.bg_color)

        self.font_normal = ("Arial", 12)
        self.font_bold = ("Arial", 12, "bold")
        self.font_header = ("Arial", 16, "bold")

        self.crear_interfaz()

    def crear_interfaz(self):
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        header_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=10)

        tk.Label(header_frame,
                 text="Calculadora de Ecuaciones Lineales",
                 font=self.font_header,
                 bg=self.bg_color,
                 fg=self.text_color).pack()

        self.crear_menu()

        self.content_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        self.mostrar_calculadora_2x2()

    def crear_menu(self):
        menu_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        menu_frame.pack(fill=tk.X, pady=10)

        tk.Button(menu_frame, text="Sistema 2x2",
                  command=self.mostrar_calculadora_2x2,
                  font=self.font_bold, bg=self.accent_color, fg="white",
                  padx=15, pady=5, bd=1, cursor="hand2").pack(side=tk.LEFT, padx=5)

        tk.Button(menu_frame, text="Sistema 3x3",
                  command=self.mostrar_calculadora_3x3,
                  font=self.font_bold, bg=self.accent_color, fg="white",
                  padx=15, pady=5, bd=1, cursor="hand2").pack(side=tk.LEFT, padx=5)

        tk.Button(menu_frame, text="Acerca de",
                  command=self.mostrar_acerca_de,
                  font=self.font_bold, bg=self.accent_color, fg="white",
                  padx=15, pady=5, bd=1, cursor="hand2").pack(side=tk.LEFT, padx=5)

        tk.Button(menu_frame, text="Salir",
                  command=self.root.quit,
                  font=self.font_bold, bg=self.accent_color, fg="white",
                  padx=15, pady=5, bd=1, cursor="hand2").pack(side=tk.RIGHT, padx=5)

    def mostrar_acerca_de(self):
        mensaje = (
            "Calculadora de Ecuaciones Lineales\n"
            "Versión 1.0\n"
            "Desarrollada como proyecto educativo en Ingeniería de Software.\n"
            "Permite resolver sistemas de ecuaciones lineales de 2x2 y 3x3."
        )
        messagebox.showinfo("Acerca de", mensaje)

    def mostrar_calculadora_2x2(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        tk.Label(self.content_frame, text="Sistema de ecuaciones 2x2",
                 font=self.font_bold, bg=self.bg_color, fg=self.text_color).pack(pady=10)

        self.entradas_2x2 = []
        variables = ["X1", "Y1", "Igual1", "X2", "Y2", "Igual2"]

        grid = tk.Frame(self.content_frame, bg=self.bg_color)
        grid.pack(pady=10)

        for i, var in enumerate(variables):
            tk.Label(grid, text=var + " =", font=self.font_normal,
                     bg=self.bg_color, fg=self.text_color).grid(row=i, column=0, sticky="e")
            entry = tk.Entry(grid, font=self.font_normal, width=10)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entradas_2x2.append(entry)

        self.resultado_2x2 = tk.Label(self.content_frame, text="",
                                      font=self.font_bold, bg=self.bg_color, fg=self.text_color)
        self.resultado_2x2.pack(pady=10)

        tk.Button(self.content_frame, text="Resolver", command=self.resolver_2x2,
                  font=self.font_bold, bg=self.accent_color, fg="white",
                  padx=10, pady=5).pack()

    def resolver_2x2(self):
        try:
            datos = [float(e.get()) for e in self.entradas_2x2]
            A = np.array([[datos[0], datos[1]], [datos[3], datos[4]]])
            B = np.array([datos[2], datos[5]])
            solucion = np.linalg.solve(A, B)
            self.resultado_2x2.config(text=f"x = {solucion[0]:.2f}, y = {solucion[1]:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo resolver el sistema: {e}")

    def mostrar_calculadora_3x3(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        tk.Label(self.content_frame, text="Sistema de ecuaciones 3x3",
                 font=self.font_bold, bg=self.bg_color, fg=self.text_color).pack(pady=10)

        self.entradas_3x3 = []
        variables = ["X1", "Y1", "Z1", "Igual1",
                     "X2", "Y2", "Z2", "Igual2",
                     "X3", "Y3", "Z3", "Igual3"]

        grid = tk.Frame(self.content_frame, bg=self.bg_color)
        grid.pack(pady=10)

        for i, var in enumerate(variables):
            tk.Label(grid, text=var + " =", font=self.font_normal,
                     bg=self.bg_color, fg=self.text_color).grid(row=i, column=0, sticky="e")
            entry = tk.Entry(grid, font=self.font_normal, width=10)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entradas_3x3.append(entry)

        self.resultado_3x3 = tk.Label(self.content_frame, text="",
                                      font=self.font_bold, bg=self.bg_color, fg=self.text_color)
        self.resultado_3x3.pack(pady=10)

        tk.Button(self.content_frame, text="Resolver", command=self.resolver_3x3,
                  font=self.font_bold, bg=self.accent_color, fg="white",
                  padx=10, pady=5).pack()

    def resolver_3x3(self):
        try:
            datos = [float(e.get()) for e in self.entradas_3x3]
            A = np.array([
                [datos[0], datos[1], datos[2]],
                [datos[4], datos[5], datos[6]],
                [datos[8], datos[9], datos[10]]
            ])
            B = np.array([datos[3], datos[7], datos[11]])
            solucion = np.linalg.solve(A, B)
            self.resultado_3x3.config(text=f"x = {solucion[0]:.2f}, y = {solucion[1]:.2f}, z = {solucion[2]:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo resolver el sistema: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraEcuacionesLineales(root)
    root.mainloop()
