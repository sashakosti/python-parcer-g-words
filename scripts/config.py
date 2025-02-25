import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../data", "config.json")

def load_config():
    """Загружает JSON-конфиг"""
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"❌ Ошибка загрузки конфига: {e}")
        return {}

CONFIG = load_config()