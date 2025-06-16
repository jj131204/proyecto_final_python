# 🎶 Música Histórica

Aplicación de escritorio desarrollada en Python con `customtkinter` que permite registrar, visualizar y gestionar una colección de canciones históricas, incluyendo su letra y enlace a YouTube.

---

## 📂 Índice

- [🔧 Requisitos](#-requisitos)
- [🧩 Estructura del proyecto](#-Estructura_del_proyecto)
- [🖥️ Uso de la aplicación](#-Uso_de_la_aplicacion)


---

## 🔧 Requisitos

- Python 3.10 o superior
- `customtkinter`
- `tkinter` (incluido en la mayoría de instalaciones de Python)

Instala las dependencias necesarias ejecutando:

```bash
pip install customtkinter
```

## 🧩 Estructura_del_proyecto
musica-historica/
-├── index.py                # Archivo principal de la aplicación
-├── saveSongs.py            # Funciones para guardar y cargar canciones (JSON)
-├── modal.py                # Modales de éxito y error reutilizables
-├── canciones.json          # Archivo local donde se almacenan las canciones
-└── README.md               # Documentación del proyecto

## 🖥️ Uso_de_la_aplicacion

En el menú principal puedes elegir:

    ✅ Registrar nueva canción

    ✅ Ver canciones registradas

Al registrar una canción debes completar:

    🎵 Nombre de la canción

    📝 Letra o descripción

    🔗 Enlace de YouTube

En la sección de canciones registradas:

    📋 Verás una lista en forma de tarjetas desplazables.

    👆 Al hacer clic en una tarjeta puedes ver los detalles completos.

    ❌ Puedes eliminar canciones o

    ▶️ Abrir el video directamente en el navegador.
