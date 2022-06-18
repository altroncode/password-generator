import configparser
import os
import pathlib


config = configparser.ConfigParser()
config_path = pathlib.Path(os.curdir) / 'config.ini'
config.read(config_path)


class PasswordGeneratorData:
    email = config.get('password_generator', 'email')


class TelegramData:
    user_id = int(config.get('telegram', 'user_id'))
    token = config.get('telegram', 'token')
    message_id = int(config.get('telegram', 'last_message_id'))