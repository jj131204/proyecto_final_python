import customtkinter as ctk

def crear_tarjeta_cancion(self, parent, cancion):
    tarjeta = ctk.CTkFrame(parent, fg_color="white", corner_radius=12, border_width=1, border_color="#ccc")
    tarjeta.pack(padx=10, pady=10, fill="x")

    # Función que se ejecutará al hacer clic
    def al_hacer_click(event=None):
        self.mostrar_detalle_cancion(cancion)

    # Componentes internos
    icono = ctk.CTkLabel(tarjeta, text="🎶", font=ctk.CTkFont(size=30),)
    icono.pack(side="left", padx=(0, 10))
    titulo = ctk.CTkLabel(tarjeta, text=cancion['nombre'], font=ctk.CTkFont(size=14, weight="bold"), text_color="black")
    descripcion = ctk.CTkLabel(tarjeta, text=cancion['descripcion'][:80] + "...", font=ctk.CTkFont(size=12), text_color="#555555")

    titulo.pack(anchor="w", padx=10, pady=(8, 2))
    descripcion.pack(anchor="w", padx=10, pady=(0, 8))

    # Hacer que todo sea clickeable
    tarjeta.bind("<Button-1>", al_hacer_click)
    titulo.bind("<Button-1>", al_hacer_click)
    descripcion.bind("<Button-1>", al_hacer_click)
