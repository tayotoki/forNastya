class BasicWord:
    def __init__(self, word: str, subwords: list[str]):
        self.word = word
        self.subwords = subwords

    def is_subword(self, user_word: str) -> bool:
        return user_word in self.subwords

    def count_subwords_quantity(self) -> int:
        return len(self.subwords)

    def __repr__(self):
        return (
            f"Составьте {self.count_subwords_quantity()} "
            f"слов из слова {self.word.upper()}\n"
            f"Слова должны быть не короче 3 букв\n"
            f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
            f"Поехали, ваше первое слово?\n"
        )
