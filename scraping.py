import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Noticia:
    titulo: str
    fecha: str
    descripcion: str

def extraer_noticias_araucaniadiario(max_articulos: int = 50) -> list[Noticia]:
    base_url = "https://araucaniadiario.cl/default/listar_contenido?p="
    noticias = []
    pagina = 1

    while len(noticias) < max_articulos:
        print(f"📄 Extrayendo página {pagina}...")
        response = requests.get(f"{base_url}{pagina}")
        print(response.elapsed.total_seconds())
        soup = BeautifulSoup(response.content, 'html.parser')

        contenedor = soup.find("div", class_="lista-contenido")
        if not contenedor:
            print(f"⚠️ No se encontró contenido en la página {pagina}")
            break

        articulos = contenedor.find_all("article", class_="post__noticia")

        for articulo in articulos:
            if len(noticias) >= max_articulos:
                break

            titulo_tag = articulo.find("h2", class_="post__titulo")
            titulo = titulo_tag.a.text.strip() if titulo_tag and titulo_tag.a else "Sin título"

            fecha_tag = articulo.find("span", class_="fecha")
            fecha = fecha_tag.text.strip() if fecha_tag else "Sin fecha"

            descripcion_tag = articulo.find("p", class_="post__detalle")
            descripcion = descripcion_tag.text.strip() if descripcion_tag else "Sin descripción"

            noticias.append(Noticia(titulo=titulo, fecha=fecha, descripcion=descripcion))

        pagina += 1

    return noticias


# extraer_noticias_araucaniadiario(20)