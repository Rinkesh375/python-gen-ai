import threading
import requests
import time


def download_image(url):

    try:

        print(
            f"{threading.current_thread().name} downloading..."
        )

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        print(
            f"{threading.current_thread().name} "
            f"Downloaded {len(response.content)} bytes"
        )

    except requests.RequestException as error:

        print(error)


image_urls = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5--Cj0WLIn6gvnJf8iwoYsRETm73w2HHFC04-DERzGQ&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIAfracvOoZljaK5PXjXNQY6PsV46t9-i-moptP3TkDQ&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnXDNuhDvUB2FkVKsvUibrj3BNyjHKzqZQWD_oRq3XK06fMiEjqTnkOCw&s=10"
]

threads = []

start = time.time()

for index, url in enumerate(image_urls, start=1):

    thread = threading.Thread(

        target=download_image,

        args=(url,),

        name=f"Downloader-{index}"
    )

    threads.append(thread)

    thread.start()

for thread in threads:
    thread.join()

print(
    f"Finished in {time.time()-start:.2f} seconds"
)      