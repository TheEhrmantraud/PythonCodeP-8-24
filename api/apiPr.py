import requests
import sys
from config import WEATHER_API_KEY, WEATHER_BASE_URL

# request запрос
# responce ответ
def get_weather(city):
    params = {
        "q": city,
        "appid": WEATHER_API_KEY, #сам апи
        "units": "metric", #единицы метрик
        "lang": "ru", 
    }

    try:
        response = requests.get(WEATHER_BASE_URL, params=params,timeout=5)
        if response.status_code == 401:
            print("Ошибка 401 неверный API")
            return None
        if response.status_code == 404:
            print(f"Ошибка 404 город '{city}' не найден")
            return None

        response.raise_for_status() #смотрит на статус код который пришел от сервера и если норм то пропускает дальше. или же просто вызовет хттп еррор

        print(response.json())
        data = response.json()

        result = {
            "город": data["name"],
            "страна": data["sys"]["country"],
            "температура": data["main"]["temp"],
            "ощущается": data["main"]["feels_like"],
            "описание": data["weather"][0]["description"],
            "влажность": data["main"]["humidity"],
            "ветер": data["wind"]["speed"],
            "давление": data["main"]["pressure"],
        }
        return result




    except requests.exceptions.Timeout:
        print("Ошибка: Превышен таймаут запроса 5 секунд")
        return None
    except requests.exceptions.ConnectionError:
        print("Нет подключения к интернету")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP ошибка: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    except KeyError as e:
        print(f"Отсутствует поле {e}")
        return None



def print_weather(weather):
    print(f"Погода в городе: {weather['город']}, {weather['страна']}")
    print(f"Температура: {weather['температура']}C")
    print(f"Ощущается: {weather['ощущается']}C")
    print(f"Описание: {weather['описание']}")
    print(f"Влажность: {weather['влажность']}%")
    print(f"Ветер: {weather['ветер']} м/с")
    print(f"Давление: {weather['давление']}")


def main():
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = input("Введите название города: ").strip()
        if not city:
            city = "Moscow"
    print(f"\nЗапрашиваем погоду для: {city}")


    weather = get_weather(city)
    if weather:
        print_weather(weather)
    else:
        print("Не удалось получить данные")
        sys.exit(1)


if __name__ == "__main__":
    main()