class Player:
    def __init__(self, username: str):
        self.username = username
        self.used_words = set()

    def count_used_words(self) -> int:
        return len(self.used_words)

    def add_word(self, user_word: str) -> None:
        self.used_words.add(user_word)

    def is_already_used(self, user_word: str) -> bool:
        return user_word in self.used_words

    def __repr__(self):
        return self.username
