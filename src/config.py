# 'https://github.com/bergstar/testcase/blob/master/okved.json' - из какого репозитория тянем файл
from pathlib import Path


class Settings():
    url: str = 'https://raw.githubusercontent.com/bergstar/testcase/master/okved.json'
    output_file: str = Path(__file__).parent.parent / "saved_data" /'okved.json'  # Имя файла в который будем сохранять данные


settings = Settings()
