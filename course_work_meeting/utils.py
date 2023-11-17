import basic_word
import player
import requests
import random as rd
import json

from settings import URL


def load_random_word() -> basic_word.BasicWord:
        response: requests.Response = requests.get(url=URL)

        if response.status_code == 200:
            data: list[dict[str, dict | str | list[str]]] = json.loads(response.text)
        else:
            raise requests.HTTPError(f"Wrong answer from server {URL}")

        word = basic_word.BasicWord(**rd.choice(data))  # BasicWord(word="питон", subwords=[...])

        return word


def end_game_stats(user: player.Player):
    print(f"Игра завершена, вы угадали {user.count_used_words()} слов!")
