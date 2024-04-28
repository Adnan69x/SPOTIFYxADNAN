from SpotifyXAdnan import SpotifyXAdnan
from os import sys,mkdir,path

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")
    SpotifyXAdnan().run()
