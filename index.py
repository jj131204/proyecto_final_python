import customtkinter as ctk
import webbrowser
from createCard import crear_tarjeta_cancion
from modal import mostrar_modal_error, mostrar_modal_exito
from saveSongs import cargar_canciones, guardar_canciones

# ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MusicaHistoricaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Música Histórica")
        self.geometry("500x600")
        self.configure(fg_color="#f8f8f8")  
        self.lista_canciones = cargar_canciones() # This is correct!
        self.mostrar_menu_principal()


    def mostrar_menu_principal(self):
        # Limpiar widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        header = ctk.CTkLabel(self, text="🎶 Música Histórica", font=ctk.CTkFont(size=26, weight="bold"), text_color="#333333")
        header.pack(pady=20)

        tarjetas_frame = ctk.CTkFrame(self, fg_color="#F8F8F8")
        tarjetas_frame.pack()

        
        tarjeta_registrar = ctk.CTkFrame(tarjetas_frame,corner_radius=15,fg_color="white", border_width=2, border_color="#000000")
        tarjeta_registrar.grid(row=0, column=0, pady=20, padx=20)

        contenido_tarjeta = ctk.CTkFrame(tarjeta_registrar, fg_color="transparent")
        contenido_tarjeta.pack(padx=15, pady=20, fill="both", expand=True)

        label1 = ctk.CTkLabel(contenido_tarjeta, text="Registrar nueva canción", font=ctk.CTkFont(size=16), text_color="black")
        label1.pack(pady=(0, 20))

        boton1 = ctk.CTkButton(contenido_tarjeta, text="Ingresar", command=self.mostrar_registro)
        boton1.pack()

        # Tarjeta 2: Ver canciones registradas
        
        tarjeta_ver = ctk.CTkFrame(tarjetas_frame,corner_radius=15,fg_color="white", border_width=2, border_color="#000000" )
        tarjeta_ver.grid(row=0, column=1, pady=20, padx=20)

        contenido_tarjeta_ver = ctk.CTkFrame(tarjeta_ver, fg_color="transparent")
        contenido_tarjeta_ver.pack(padx=15, pady=20, fill="both", expand=True)

        label2 = ctk.CTkLabel(contenido_tarjeta_ver, text="Ver canciones registradas", font=ctk.CTkFont(size=16), text_color="black")
        label2.pack(pady=(0, 20))

        boton2 = ctk.CTkButton(contenido_tarjeta_ver, text="Ver", command=self.mostrar_lista)
        boton2.pack()

    def guardar_cancion(self):
        nombre = self.entry_nombre.get().strip()
        descripcion = self.textbox_descripcion.get("0.0", "end-1c").strip()
        link = self.entry_link.get().strip()

        if nombre and link:
            nueva = {
                "nombre": nombre,
                "descripcion": descripcion,
                "link": link
            }
            self.lista_canciones.append(nueva)
            guardar_canciones(self.lista_canciones)
            mostrar_modal_exito(self)
        else:
            mostrar_modal_error(self)


    def mostrar_registro(self):
        # Vista para registrar canciones
        for widget in self.winfo_children():
            widget.destroy()

        titulo = ctk.CTkLabel(self, text="Registrar Canción", font=ctk.CTkFont(size=20, weight="bold"), text_color="#333333")
        titulo.pack(pady=20)

        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre de la canción", height=40)
        self.entry_nombre.pack(pady=5, fill="x", padx=20)

        self.textbox_descripcion = ctk.CTkTextbox(self, height=100)
        self.textbox_descripcion.pack(pady=5, fill="x", padx=20)
        self.textbox_descripcion.insert("0.0", "Letra de la canción...")
        self.textbox_descripcion.pack(pady=5, fill="x", padx=20)

        self.entry_link = ctk.CTkEntry(self, placeholder_text="Link de YouTube", height=40)
        self.entry_link.pack(pady=5, fill="x", padx=20)

        ctk.CTkButton(self, text="Guardar", command=self.guardar_cancion).pack(pady=10)
        ctk.CTkButton(self, text="← Volver", command=self.mostrar_menu_principal).pack(pady=5)


    def mostrar_lista(self):
        for widget in self.winfo_children():
            widget.destroy()

        titulo = ctk.CTkLabel(self, text="Canciones registradas", font=ctk.CTkFont(size=20, weight="bold"), text_color="#333333")
        titulo.pack(pady=20)

        self.frame_lista = ctk.CTkScrollableFrame(self)
        self.frame_lista.pack(padx=20, pady=20, fill="both", expand=True)

        if not self.lista_canciones:
            ctk.CTkLabel(self.frame_lista, text="No hay canciones registradas todavía.").pack(pady=20)
        else:
            for cancion in self.lista_canciones:
                crear_tarjeta_cancion(self, self.frame_lista, cancion)


        ctk.CTkButton(self, text="← Volver", command=self.mostrar_menu_principal).pack(pady=5)

    def mostrar_detalle_cancion(self, cancion):
        for widget in self.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self, text=cancion['nombre'], text_color="#333333", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))

        # scroll
        scroll_frame = ctk.CTkScrollableFrame(self, width=500, height=250)
        scroll_frame.pack(padx=20, pady=10, fill="both", expand=False)

        ctk.CTkLabel(scroll_frame, text="Letra:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=(0, 5))
        ctk.CTkLabel(scroll_frame, text=cancion['descripcion'], wraplength=460, justify="left").pack(anchor="w")

        ctk.CTkButton(self, text="Ver video en YouTube", command=lambda: webbrowser.open(cancion['link'])).pack(pady=10)

        ctk.CTkButton(self, text="Borrar Canción", fg_color="red", hover_color="#CC0000",
                      command=lambda: self.eliminar_cancion(cancion)).pack(pady=10)

        ctk.CTkButton(self, text="← Volver", command=self.mostrar_lista).pack(pady=5)
    
    def eliminar_cancion(self, cancion_a_borrar):
        nueva_lista = [cancion for cancion in self.lista_canciones if cancion != cancion_a_borrar]
        
        if len(nueva_lista) < len(self.lista_canciones):
            self.lista_canciones = nueva_lista
            guardar_canciones(self.lista_canciones)
            print(f"Canción '{cancion_a_borrar['nombre']}' eliminada.")
            self.mostrar_lista()
        else:
            print("Error: La canción no se encontró en la lista.")
            mostrar_modal_error(self, "La canción no pudo ser eliminada.") # Muestra un modal de error

if __name__ == "__main__":
    app = MusicaHistoricaApp()
    app.mainloop()