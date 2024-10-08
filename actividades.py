import customtkinter as ctk

class Actividad:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

def seleccion_actividades(actividades):
    # Ordenar actividades por tiempo de finalización
    actividades.sort(key=lambda x: x.fin)
    
    actividades_seleccionadas = []
    ultima_fin = 0  # Mantiene el tiempo de finalización de la última actividad seleccionada

    for actividad in actividades:
        # Si la actividad comienza después de la última actividad seleccionada
        if actividad.inicio >= ultima_fin:
            actividades_seleccionadas.append(actividad)
            ultima_fin = actividad.fin  # Actualizar el tiempo de finalización

    return actividades_seleccionadas

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Selección de Actividades")
        self.root.geometry("400x400")

        # Elementos de la interfaz
        self.label_actividades = ctk.CTkLabel(root, text="Actividades (inicio, fin):")
        self.label_actividades.pack(pady=10)
        self.entry_actividades = ctk.CTkEntry(root)
        self.entry_actividades.pack(pady=5)

        self.button_calcular = ctk.CTkButton(root, text="Calcular", command=self.calcular_actividades)
        self.button_calcular.pack(pady=20)

        self.resultado = ctk.CTkTextbox(root, width=300, height=150)
        self.resultado.pack(pady=10)

    def calcular_actividades(self):
        # Obtener datos de entrada
        actividad_strings = self.entry_actividades.get().split(';')
        actividades = []

        # Crear actividades a partir de la entrada del usuario
        for actividad_str in actividad_strings:
            inicio, fin = map(float, actividad_str.split(','))
            actividades.append(Actividad(inicio, fin))

        # Calcular las actividades seleccionadas
        actividades_seleccionadas = seleccion_actividades(actividades)

        # Mostrar resultados
        self.resultado.delete("1.0", ctk.END)
        for actividad in actividades_seleccionadas:
            self.resultado.insert(ctk.END, f"Inicio: {actividad.inicio}, Fin: {actividad.fin}\n")
        self.resultado.insert(ctk.END, f"Total de actividades seleccionadas: {len(actividades_seleccionadas)}\n")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modo oscuro
    ctk.set_default_color_theme("blue")  # Tema azul
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
