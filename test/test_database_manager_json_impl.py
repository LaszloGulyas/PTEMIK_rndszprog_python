from application.service.database_manager_json_impl import DatabaseManagerJsonImpl
import unittest

db_manager = DatabaseManagerJsonImpl()
_data_list_ = []


class TestDatabaseManagerJsonImpl(unittest.TestCase):
    def test_reading_and_writing(self):
        db_manager.read_data()
        self.assertNotEqual(db_manager.data_object, None)
        db_manager.save_data()
