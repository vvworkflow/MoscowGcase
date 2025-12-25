from src.okved import parse_okved
from src.phone import phone_number_validation, phone_normalization
from src.utils import download_data
from src.config import settings
import json


def main():
    phone = input("Введите МОБИЛЬНЫЙ номер телефона: ")
    if phone_number_validation(phone):
        phone = phone_normalization(phone)
    else:
        return 'Некорректный номер телефона'
    best = {
        "code": "",
        "name": "",
        "length": 0
    }

    parse_okved(phone, data, best)
    if best["code"]:
        return (f'Для телефона {phone} ОКВЭД:\n'
                f'[{best["code"]}] - {best["name"] or "Не определено"}\n\n'
                f'максимальная длина - {best["length"]}')
    else:
        return (f'Для номера {phone} не нашлось совпадений по ОКВЭД')


if __name__ == "__main__":
    download_data(url=settings.url, output_file=settings.output_file)
    with open(settings.output_file) as f:
        data = json.load(f)
    data = json.load(open(settings.output_file, encoding="utf-8"))
    print(main())
