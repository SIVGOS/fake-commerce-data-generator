from random import choice
import string

class SecretGenerator:
    def __init__(self) -> None:
        self.__secret_characters = string.ascii_letters + string.digits
        self.__default_length = 16

    def generate_secret(self, length=None):
        if length is None:
            length = self.__default_length
        return ''.join([choice(self.__secret_characters) for _ in range(16)])
