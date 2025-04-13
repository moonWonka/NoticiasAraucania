import csv
from scraping import Noticia

def guardar_en_csv(noticias: list[Noticia], nombre_archivo: str = "noticias.csv"):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["Título", "Fecha", "Descripción"])
        for noticia in noticias:
            writer.writerow([noticia.titulo, noticia.fecha, noticia.descripcion])
    print(f"✅ Archivo 🚀 guardado como: {nombre_archivo}")
