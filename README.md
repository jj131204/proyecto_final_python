# 🎶 Música Histórica

Aplicación de escritorio desarrollada en Python con `customtkinter` que permite registrar, visualizar y gestionar una colección de canciones históricas, incluyendo su letra y enlace a YouTube.

---

## 📂 Índice

- [🔧 Requisitos](#-requisitos)
- [🧩 Estructura del proyecto](#-estructura-del-proyecto)
- [📌 Funcionalidades](#-funcionalidades)
- [📤 Exportar y guardar](#-exportar-y-guardar)
- [💡 Ideas futuras](#-ideas-futuras)
- [📄 Licencia](#-licencia)

---

## 🔧 Requisitos

- Python 3.10 o superior
- `customtkinter`
- `tkinter` (incluido en la mayoría de instalaciones de Python)

Instala las dependencias necesarias ejecutando:

```bash
pip install customtkinter

## 🧩 Estructura del proyecto
musica-historica/
├── index.py                # Archivo principal de la aplicación
├── saveSongs.py            # Funciones para guardar y cargar canciones (JSON)
├── createCard.py           # Generación de tarjetas con información de canciones
├── modal.py                # Modales de éxito y error reutilizables
├── canciones.json          # Archivo local donde se almacenan las canciones
└── README.md               # Documentación del proyecto

