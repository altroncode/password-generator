import secrets
import string

import data


class Password:
    __slots__ = ('_settings', '_password')

    def __init__(self, settings: data.settings.PasswordSettings):
        self._settings = settings
        self._password = self.create_password()

    def _get_symbols(self) -> str:
        symbols = ''
        if self._settings.is_digits:
            symbols += string.digits
        if self._settings.is_capital_letters:
            symbols += string.ascii_uppercase
        if self._settings.is_small_letters:
            symbols += string.ascii_lowercase
        if self._settings.is_punctuation:
            symbols += string.punctuation
        return symbols

    def create_password(self) -> str:
        symbols = self._get_symbols()
        return "".join(secrets.choice(symbols) for _ in range(self._settings.length))

    def __str__(self):
        return self._password

    def __len__(self):
        return len(self._password)
