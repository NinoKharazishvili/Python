import threading
import requests

# Function to download MP3 file
def download_mp3(url, filename):
    try:
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename} successfully!")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    # List of URLs and corresponding filenames
    urls = [
        "https://archive.org/details/TheShowMustGoOn",
        "https://archive.org/details/ShapeOfMyHeart",
        "https://archive.org/details/AndyWilliamsnon-remakes/WhereDoIBeginloveStory.mp3"
    ]
    filenames = ["TheShowMustGoOn.mp3", "ShapeOfMyHeart.mp3", "WhereDoIBeginloveStory.mp3"]

    # Create threads for downloading
    threads = []
    for url, filename in zip(urls, filenames):
        thread = threading.Thread(target=download_mp3, args=(url, filename))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All downloads completed.")
