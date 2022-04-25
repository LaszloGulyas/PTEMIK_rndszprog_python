from application.model.data_item import DataItem

FIELD_NAME_IDENTIFIER = "identifier"
FIELD_NAME_IDENTIFIER_IMAGE = "identifier_image"
FIELD_NAME_RESULTS = "results"
FIELD_NAME_RESULTS_IMAGE = "result_image"
FIELD_NAME_CONFIRMED_IDENTIFIER = "confirmed_identifier"
FIELD_NAME_CONFIRMED_RESULTS = "confirmed_results"


class ParserUtil:
    @staticmethod
    def parse_json_object_to_data_item(json_object):
        data_item = DataItem(json_object.get(FIELD_NAME_IDENTIFIER),
                             json_object.get(FIELD_NAME_IDENTIFIER_IMAGE),
                             json_object.get(FIELD_NAME_RESULTS),
                             json_object.get(FIELD_NAME_RESULTS_IMAGE),
                             json_object.get(FIELD_NAME_CONFIRMED_IDENTIFIER),
                             json_object.get(FIELD_NAME_CONFIRMED_RESULTS))
        return data_item

    @staticmethod
    def parse_data_item_to_json_object(data_item):
        json_object = {
            FIELD_NAME_IDENTIFIER: data_item[FIELD_NAME_IDENTIFIER],
            FIELD_NAME_IDENTIFIER_IMAGE: data_item[FIELD_NAME_IDENTIFIER_IMAGE],
            FIELD_NAME_RESULTS: data_item[FIELD_NAME_RESULTS],
            FIELD_NAME_RESULTS_IMAGE: data_item[FIELD_NAME_RESULTS_IMAGE],
            FIELD_NAME_CONFIRMED_IDENTIFIER: data_item[FIELD_NAME_CONFIRMED_IDENTIFIER],
            FIELD_NAME_CONFIRMED_RESULTS: data_item[FIELD_NAME_CONFIRMED_RESULTS]
        }
        return json_object
