import urllib.request
import time
urls = [
    'http://www.python.org',
    'https://docs.python.org/3/',
    'https://docs.python.org/3/whatsnew/3.7.html',
    'https://docs.python.org/3/tutorial/index.html',
    'https://docs.python.org/3/library/index.html',
    'https://docs.python.org/3/reference/index.html',
    'https://docs.python.org/3/using/index.html',
    'https://docs.python.org/3/howto/index.html',
    'https://docs.python.org/3/installing/index.html',
    'https://docs.python.org/3/distributing/index.html',
    'https://docs.python.org/3/c-api/index.html',
    'https://docs.python.org/3/c-api/index.html',
    'https://docs.python.org/3/faq/index.html'
] * 20
results = []
start_time = time.time()
for url in urls:
    with urllib.request.urlopen(url) as src:
        results.append(src)
duration = time.time() - start_time
print(f"Descargados {len(urls)} en {duration} segundos")
