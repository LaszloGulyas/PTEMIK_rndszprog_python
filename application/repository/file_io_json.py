import json


class FileIoJson:
    def __init__(self, input_file_path, output_file_path):
        self._input_file_path_ = input_file_path
        self._output_file_path_ = output_file_path

    def read_json_object_from_file(self):
        file = open(self._input_file_path_, "r")
        json_object = json.load(file)
        file.close()
        return json_object

    def write_json_object_to_file(self, json_object):
        json_object_formatted = json.dumps(json_object, indent=4)
        file = open(self._output_file_path_, "w")
        file.write(json_object_formatted)
        file.close()
