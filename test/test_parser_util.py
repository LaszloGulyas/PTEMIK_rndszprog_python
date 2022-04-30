import unittest

from application.model.data_item import DataItem
from application.util.parser_util import ParserUtil

test_data_object = DataItem("aa", "bb", [1, 2], "cc", "dd", [3, 4])
test_json = {'identifier': 'aa', 'identifier_image': 'bb', 'results': [1, 2], 'result_image': 'cc', 'confirmed_identifier': 'dd', 'confirmed_results': [3, 4]}


class TestParserUtil(unittest.TestCase):
    def test_object_parsed_to_json(self):
        parsed_json = ParserUtil.parse_data_item_to_json_object(test_data_object)
        print(parsed_json)
        self.assertEqual(test_json, parsed_json)

    def test_json_parsed_to_object(self):
        parsed_data_object = ParserUtil.parse_json_object_to_data_item(test_json)
        print(parsed_data_object)
        self.assertEqual(test_data_object, parsed_data_object)
