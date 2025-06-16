import customtkinter as ctk

def mostrar_modal_exito(self):
    modal = ctk.CTkToplevel(self)
    modal.title("Éxito")
    modal.geometry("300x180")
    modal.grab_set()  # bloquea la ventana principal hasta cerrar esta

    label = ctk.CTkLabel(modal, text="🎉 Canción guardada correctamente", font=ctk.CTkFont(size=14, weight="bold"), wraplength=260)
    label.pack(pady=(20, 10), padx=10)

    btn_ver = ctk.CTkButton(modal, text="Ver canciones registradas", command=lambda: [modal.destroy(), self.mostrar_lista()])
    btn_ver.pack(pady=5, padx=20, fill="x")

    btn_nueva = ctk.CTkButton(modal, text="Registrar nueva canción", command=lambda: [modal.destroy(), self.mostrar_registro()])
    btn_nueva.pack(pady=(0, 10), padx=20, fill="x")

def mostrar_modal_error(self):
    modal = ctk.CTkToplevel(self)
    modal.title("Error")
    modal.geometry("300x180")
    modal.grab_set()  # bloquea la ventana principal hasta cerrar esta

    label = ctk.CTkLabel(modal, text="Ocurrio un error, verifica que hayas llenado por lo menos el nombre y el link de la canción", font=ctk.CTkFont(size=14, weight="bold"), wraplength=260)
    label.pack(pady=(20, 10), padx=10)

    btn_ver = ctk.CTkButton(modal, text="Aceptar", command=lambda: [modal.destroy()])
    btn_ver.pack(pady=5, padx=20, fill="x")