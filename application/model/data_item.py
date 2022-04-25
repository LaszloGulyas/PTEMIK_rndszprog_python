from dataclasses import dataclass


@dataclass
class DataItem:
    identifier: str
    identifier_image: str
    results: list
    result_image: str
    confirmed_identifier: str
    confirmed_results: list

    def __getitem__(self, key):
        return super().__getattribute__(key)
