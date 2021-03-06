"""Module for setting project"""
from data import base_data_model
from data._field import Field


SETTINGS_PATH = 'password-generator/data/settings.ini'
DATA_PATH = 'password-generator/data/app_data.ini'


class GeneralSettings(base_data_model.BaseModel):
    _section_name = 'general'

    storages: list[str] = Field()


class PasswordSettings(base_data_model.BaseModel):
    _section_name: str = 'password'

    length: int = Field()
    is_digits: bool = Field()
    is_capital_letters: bool = Field()
    is_small_letters: bool = Field()
    is_punctuation: bool = Field()
