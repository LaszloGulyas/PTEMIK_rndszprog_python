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
    def get_first_item_by_identifier(self, identifier) -> DataItem | None:
        return

    @abstractmethod
    def get_first_item_by_index(self, index) -> DataItem | None:
        return

    @abstractmethod
    def get_first_item(self) -> DataItem | None:
        return

    @abstractmethod
    def get_index_of_item(self, identifier) -> int | None:
        return
