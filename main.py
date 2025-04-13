from scraping import extraer_noticias_araucaniadiario as extraer_noticias
from exportador_csv import guardar_en_csv

def main():
    print("📰 Extrayendo noticias de Araucanía Diario...")
    noticias = extraer_noticias(max_articulos=50)

    print(f"✅ Se extrajeron {len(noticias)} noticias.")
    guardar_en_csv(noticias)

if __name__ == "__main__":
    main()
