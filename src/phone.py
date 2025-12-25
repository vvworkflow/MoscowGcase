import re


def phone_normalization(raw_phone: str) -> str:
    n = re.sub(r"\D", '', raw_phone)
    return f"+7{n[1:]}"


def phone_number_validation(raw_phone: str) -> bool:
    n = re.sub(r"\D", '', raw_phone)
    if (n.startswith('79') or n.startswith('89')) and len(n) == 11:
        return True
    else:
        return False


