from application.service.database_manager import DatabaseManager
import unittest

db_manager = DatabaseManager("../resources/database_input.json", "../resources/database_output.json")
_data_list_ = []


class TestDataBaseManagerService(unittest.TestCase):
    def test_reading_and_writing(self):
        self._data_list_ = db_manager.read_data()
        self.assertNotEqual(self._data_list_, None)
        db_manager.save_data(self._data_list_)
