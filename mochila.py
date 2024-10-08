import customtkinter as ctk

class Articulo:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.valor_por_peso = valor / peso  # Relación valor/peso

def mochila_fraccionaria(articulos, capacidad_maxima):
    # Ordenar artículos por valor/peso en orden descendente
    articulos.sort(key=lambda x: x.valor_por_peso, reverse=True)
    
    valor_total = 0
    cantidades_seleccionadas = []

    for articulo in articulos:
        if capacidad_maxima == 0:
            break
        
        if articulo.peso <= capacidad_maxima:
            cantidades_seleccionadas.append((articulo, 1.0))  # Artículo completo
            valor_total += articulo.valor
            capacidad_maxima -= articulo.peso
        else:
            fraccion = capacidad_maxima / articulo.peso  # Fracción que se puede agregar
            cantidades_seleccionadas.append((articulo, fraccion))  # Agregar fracción
            valor_total += articulo.valor * fraccion
            capacidad_maxima = 0  # Mochila llena

    return cantidades_seleccionadas, valor_total

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mochila Fraccionaria")
        self.root.geometry("400x400")

        # Elementos de la interfaz
        self.label_peso = ctk.CTkLabel(root, text="Pesos (separados por comas):")
        self.label_peso.pack(pady=10)
        self.entry_peso = ctk.CTkEntry(root)
        self.entry_peso.pack(pady=5)

        self.label_valor = ctk.CTkLabel(root, text="Valores (separados por comas):")
        self.label_valor.pack(pady=10)
        self.entry_valor = ctk.CTkEntry(root)
        self.entry_valor.pack(pady=5)

        self.label_capacidad = ctk.CTkLabel(root, text="Capacidad de la mochila:")
        self.label_capacidad.pack(pady=10)
        self.entry_capacidad = ctk.CTkEntry(root)
        self.entry_capacidad.pack(pady=5)

        self.button_calcular = ctk.CTkButton(root, text="Calcular", command=self.calcular_mochila)
        self.button_calcular.pack(pady=20)

        self.resultado = ctk.CTkTextbox(root, width=300, height=150)
        self.resultado.pack(pady=10)

    def calcular_mochila(self):
        # Obtener datos de entrada
        pesos = list(map(float, self.entry_peso.get().split(',')))
        valores = list(map(float, self.entry_valor.get().split(',')))
        capacidad = float(self.entry_capacidad.get())

        # Validar que los números de pesos y valores coincidan
        if len(pesos) != len(valores):
            self.resultado.delete("1.0", ctk.END)
            self.resultado.insert(ctk.END, "Error: La cantidad de pesos y valores debe ser igual.\n")
            return

        # Crear artículos y mantener el índice original
        articulos = [Articulo(peso, valor) for peso, valor in zip(pesos, valores)]
        
        # Calcular la mochila fraccionaria
        cantidades_seleccionadas, valor_total = mochila_fraccionaria(articulos, capacidad)

        # Mostrar resultados
        self.resultado.delete("1.0", ctk.END)
        self.resultado.insert(ctk.END, "Resultado Final\nArtículos seleccionados:\n\n")

        # Mostrar los artículos seleccionados con su índice original
        for articulo, cantidad in cantidades_seleccionadas:
            articulo_index = articulos.index(articulo)  # Obtener el índice en la lista original
            if cantidad == 1.0:
                self.resultado.insert(ctk.END, f"Artículo {articulo_index + 1}: {cantidad} (completo)\n")
            else:
                self.resultado.insert(ctk.END, f"Artículo {articulo_index + 1}: {cantidad:.2f} (fracción)\n")
        
        self.resultado.insert(ctk.END, f"Valor Total = {valor_total:.2f}\n")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modo oscuro
    ctk.set_default_color_theme("blue")  # Tema azul
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
