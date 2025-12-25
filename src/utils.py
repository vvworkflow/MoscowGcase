import requests


def download_data(url: str, output_file: str):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        with open(output_file, "wb") as f:
            f.write(response.content)
    except Exception as e:
        raise e
