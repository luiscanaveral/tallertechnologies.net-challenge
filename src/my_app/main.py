import os
from dotenv import load_dotenv

def main() -> None:
    load_dotenv()
    name = os.getenv("APP_NAME", "My Python Seed")
    print(f"🚀 Starting {name}...")

if __name__ == "__main__":
    main()