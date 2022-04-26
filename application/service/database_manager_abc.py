from abc import ABC, abstractmethod


class DatabaseManagerAbc(ABC):

    @abstractmethod
    def read_data(self) -> []:
        return

    @abstractmethod
    def save_data(self, data_item_list):
        pass
