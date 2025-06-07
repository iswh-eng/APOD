import requests
import os
from dotenv import load_dotenv
from PIL import Image
from pathlib import Path
import datetime
from directories import create_directories

# directories settings
root_dir = Path.cwd()
home_dir = Path.home()
picture_path = home_dir / "Pictures"
apod_dir = picture_path / "APOD"
config_dir = root_dir / "config"
settings_file = Path("settings.json")

# image settings
WIDTH = 1920
HEIGHT = 1080

# env variables
env_file = root_dir / "config" / ".env"
load_dotenv(dotenv_path=env_file)
key = os.getenv("NASA_API_KEY")


def main():
    print("Hello from apod!")
    try:
        create_directories(config_dir, root_dir, picture_path, home_dir, apod_dir, settings_file, WIDTH, HEIGHT)
    except ImportError as e:
        print(f'Something went wrong\n{e}')


if __name__ == "__main__":
    main()
