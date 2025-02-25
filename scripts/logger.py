import logging
from scripts.config import CONFIG

logging.basicConfig(
    filename=CONFIG["log"],  # Файл для логов
    level=logging.INFO,   # Уровень логирования (INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    """Записывает информационное сообщение"""
    logging.info(message)

def log_warning(message):
    """Записывает предупреждение"""
    logging.warning(message)

def log_error(message):
    """Записывает ошибку"""
    logging.error(message)
