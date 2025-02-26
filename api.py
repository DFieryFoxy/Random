import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("COuldn't complete request!")
        return
    
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")

main()    