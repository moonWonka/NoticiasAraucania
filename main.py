from scraping import Noticia, extraer_noticias_araucaniadiario, extraer_noticias_elperiodico
from exportador_csv import guardar_en_csv

def main():
    print("📰 Extrayendo noticias de Araucanía Diario...")
    noticias = extraer_noticias_araucaniadiario(max_articulos=50)

    print("📰 Extrayendo noticias de El Periodico...")
    noticias_elperiodico: list[Noticia] = extraer_noticias_elperiodico(max_articulos=50)

    print(f"✅ Se extrajeron {len(noticias)} noticias.")
    guardar_en_csv(noticias)

    print(f"✅ Se extrajeron {len(noticias_elperiodico)} noticias 2.")
    guardar_en_csv(noticias_elperiodico, nombre_archivo="noticias2.csv")

if __name__ == "__main__":
    main()
