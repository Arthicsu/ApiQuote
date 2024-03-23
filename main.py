import requests


def GetQuote():
    url = "http://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "ru"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["quoteText"]:
            return {
                "quote": data["quoteText"],
                "author": data["quoteAuthor"]
            }
    else:
        return print("Ошибка импорта данных!!!")


def main():
    print("Добро пожаловать в приложение для получения случайных цитат!")
    input("Нажмите Enter, чтобы получить новую цитату...")

    quote_info = GetQuote()

    if quote_info:
        print("\nВот случайная цитата для Вас:")
        print(f'"{quote_info["quote"]}" - {quote_info["author"]}')
    else:
        print("Не удалось получить цитату :(")


if __name__ == "__main__":
    main()