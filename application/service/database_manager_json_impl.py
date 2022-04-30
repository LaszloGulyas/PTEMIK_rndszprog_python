from application.repository.file_io_json import FileIoJson
from application.service.database_manager_abc import DatabaseManagerAbc
from application.util.parser_util import ParserUtil
from application.util.path_util import PathUtil

_RESOURCE_FOLDER_NAME_ = "resources"
_INPUT_FILE_NAME_ = "database_input.json"
_OUTPUT_FILE_NAME = "database_input.json"


def __fill_default_value_if_data_missing__(data_item):
    if data_item.confirmed_identifier is None:
        data_item.confirmed_identifier = data_item.identifier
    if data_item.confirmed_results is None:
        data_item.confirmed_results = data_item.results


class DatabaseManagerJsonImpl(DatabaseManagerAbc):
    def __init__(self):
        self._input_file_path_ = None
        self._output_file_path_ = None
        self.__init_file_paths__()
        self._file_manager_ = FileIoJson(self._input_file_path_, self._output_file_path_)

    def read_data(self):
        json_read = self._file_manager_.read_json_object_from_file()
        data_item_list = []
        for item in json_read:
            data_item = ParserUtil.parse_json_object_to_data_item(item)
            __fill_default_value_if_data_missing__(data_item)
            data_item_list.append(data_item)
        return data_item_list

    def save_data(self, data_item_list):
        json_to_write = []
        for item in data_item_list:
            json_to_write.append(ParserUtil.parse_data_item_to_json_object(item))
        self._file_manager_.write_json_object_to_file(json_to_write)

    def __init_file_paths__(self):
        root_path = PathUtil.get_project_root()
        self._input_file_path_ = root_path.joinpath(_RESOURCE_FOLDER_NAME_).joinpath(_INPUT_FILE_NAME_)
        self._output_file_path_ = root_path.joinpath(_RESOURCE_FOLDER_NAME_).joinpath(_OUTPUT_FILE_NAME)
