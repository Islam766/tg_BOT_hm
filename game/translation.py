"""
Переводчик.
"""
import json


class Translation:
    """
    Класс переводчика.
    """
    __players = {}
    __menu_translation_path = f'./Translations/menu.json'
    __slots_translation_path = f'./Translations/slots.json'
    __xo_translation_path = f'./Translations/xo.json'
    __bj_translation_path = f'./Translations/bj.json'
    __hm_translation_path = f'./Translations/hangman.json'
    __dating_translation_path = f'./Translations/dating.json'
    __tora_translation_path = f'./Translations/TorA.json'

    @classmethod
    def get_hangman_exp(cls, key, user_id):
        """
        Метод получения выражения из hangman.json по ключу.

        :param key: Ключ.
        :param user_id: ID пользователя.
        :return: Выражение.
        """
        if user_id not in cls.__players:
            cls.__players[user_id] = 0
        with open(cls.__hm_translation_path, "r", encoding="utf8") as read:
            return json.load(read)[key][cls.__players[user_id]]

    @classmethod
    def get_player_language(cls, user_id):
        """
        Метод получения языка игрока.

        :param user_id: ID игрока.
        :return: Язык.
        """
        if user_id not in cls.__players:
            cls.__players[user_id] = 0
        return cls.__players[user_id]

    @staticmethod
    def switch_language(user_id):
        """
        Метод смены языка.

        :param user_id: ID игрока.
        """
        if user_id in Translation.__players:
            if Translation.__players[user_id] == 0:
                Translation.__players[user_id] = 1
            else:
                Translation.__players[user_id] = 0

    @classmethod
    def set_lang(cls, user_id):
        """
        Метод установки языка.

        :param user_id: ID пользователя.
        """
        if user_id not in cls.__players:
            cls.__players[user_id] = 0
        else:
            cls.__players[user_id] = 1

    @classmethod
    def set_language(cls, user_id, lang):
        """
        Метод установки языка (улучшенный).

        :param user_id: ID пользователя.
        :param lang: Язык.
        """
        cls.__players[user_id] = lang

    @classmethod
    def get_language(cls, user_id):
        """
        Метод получения языка пользователя (улучшенный).

        :param user_id: ID пользователя
        :return: Язык
        """
        return cls.__players[user_id]
