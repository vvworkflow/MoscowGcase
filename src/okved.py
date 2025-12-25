def parse_okved(phone: str, items: list, best: dict) -> None:
    for item in items:
        code = item.get("code", "")
        name = item.get("name", "")
        clean_code = code.replace(".", "")

        if not clean_code:
            continue

        if phone.endswith(clean_code):
            if len(clean_code) > best["length"]:
                best["code"] = code
                best["name"] = name
                best["length"] = len(clean_code)

        if isinstance(item.get("items"), list):
            parse_okved(phone, item["items"], best)
