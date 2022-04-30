from abc import ABC, abstractmethod

from application.model.data_item import DataItem


class DatabaseManagerAbc(ABC):

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def find_first_by_identifier(self, identifier) -> DataItem | None:
        return

    @abstractmethod
    def get_first_item(self) -> DataItem | None:
        return
