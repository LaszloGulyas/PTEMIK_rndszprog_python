from application.service.database_manager_json_impl import DatabaseManagerJsonImpl
import unittest

db_manager = DatabaseManagerJsonImpl()
_data_list_ = []


class TestDatabaseManagerJsonImpl(unittest.TestCase):
    def test_reading_and_writing(self):
        self._data_list_ = db_manager.read_data()
        self.assertNotEqual(self._data_list_, None)
        db_manager.save_data(self._data_list_)
