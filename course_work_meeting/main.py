import player
import utils
import basic_word


STOP_WORDS = [
    "стоп",
    "stop",
    "stёp",
]


def main():
    user_name = input(
        "Привет, назови свое имя!\n"
    )

    user: player.Player = player.Player(username=user_name)

    print(f"Привет {user}")

    word: basic_word.BasicWord = utils.load_random_word()

    print(word)

    true_answer_counter = 0

    while true_answer_counter < word.count_subwords_quantity():
        user_suppose = input()

        if user_suppose in STOP_WORDS:
            break

        if word.is_subword(user_word=user_suppose):
            if not user.is_already_used(user_word=user_suppose):
                user.add_word(user_word=user_suppose)
                print("верно")
            else:
                print("уже использовано")
        else:
            print("неправильно")

    utils.end_game_stats(user=user)


if __name__ == "__main__":
    main()
