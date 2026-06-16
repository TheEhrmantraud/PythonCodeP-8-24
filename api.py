import sys
import requests

API_KEY = "37b217ab3e8c4a4cadc05f3b45abb090"


def news(query="python", language="ru", page_size=5):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": language,
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": API_KEY,  # ДОБАВЛЕНО: передаем ключ авторизации
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("status") != "ok":
            # ИСПРАВЛЕНО: изменены кавычки внутри f-строки и добавлен метод .get()
            error_msg = data.get("message", "неизвестная ошибка")
            print(f"Ошибка апи: {error_msg}")
            return None

        return data.get("articles", [])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка http: {e}")
        return None


def main():
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("Введите тему для поиска: ").strip()
        if not query:
            query = "python"
    print(f"Ищем новости по запросу: {query}\n")

    # ИСПРАВЛЕНО: передаем переменную query, а не строку "python"
    articles = news(query=query, language="ru", page_size=5)

    if not articles:
        print("Новостей нет")
        return

    print(f"Выдано {len(articles)}\n")

    # ИСПРАВЛЕНО: возвращены правильные отступы для вывода ВСЕХ статей
    for i, article in enumerate(articles, start=1):
        title = article.get("title", "Без названия")
        dec = article.get("description", "Нет описания") or "Нет описания"
        url = article.get("url", "*")
        published = article.get("publishedAt", "Дата неизвестна")

        # ИСПРАВЛЕНО: заменены внутренние кавычки в f-строке с "" на ''
        dots = "..." if len(dec) > 120 else ""

        print(f"{i}. {title}")
        print(f"Дата: {published[:10]}")
        print(f"Описание: {dec[:120]}{dots}")
        print(f"Ссылка: {url}")
        print("-" * 40)  # Разделитель для красоты


if __name__ == "__main__":
    main()