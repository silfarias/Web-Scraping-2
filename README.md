# Web-Scraping-2

El objetivo de este trabajo es la implementación de un web scraper en Python que recorre un sitio web y extrae todas las etiquetas `<img>` con sus respectivas urls, dichas imagenes se descargan y se guardan en un directorio.

## Requisitos para su uso

- Python 3.x
- Bibliotecas `requests` y `BeautifulSoup` (pueden instalarse mediante `pip`)

### Instalación

1. Clona este repositorio.
2. Instala las dependencias necesarias:

```bash
pip install requests beautifulsoup4
```

### Ejecución

Ejecuta el script `app.py` para iniciar el web crawler:

```bash
python app.py