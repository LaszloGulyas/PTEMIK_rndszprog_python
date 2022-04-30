from application.service.database_manager_json_impl import DatabaseManagerJsonImpl
from application.util.image_util import ImageUtil
from application.util.path_util import PathUtil
from application.view.record_editor_view import RecordEditorView


class RecordEditorController:
    def __init__(self):
        self._db_service_ = DatabaseManagerJsonImpl()
        self._db_service_.read_data()
        self._editor_view_ = None

    def create_view(self):
        self._editor_view_ = RecordEditorView(self)
        self._editor_view_.show()

    def init_view_fields(self):
        first_record = self._db_service_.get_first_item()
        self.update_view_fields(first_record.identifier)

    def update_view_fields(self, identifier):
        record = self._db_service_.get_first_item_by_identifier(identifier)
        view = self._editor_view_

        view.lbl_identifier_value.config(text=record.identifier)
        view.update_txt_field_value(view.txt_confirmed_identifier_value, record.confirmed_identifier)
        view.lbl_results_value.config(text=self.__convert_array_to_printable_string__(record.results))
        view.update_txt_field_value(view.txt_confirmed_results_value,
                                    self.__convert_array_to_printable_string__(record.confirmed_results))
        self.__update_image_widget__(view.img_grp_identifier_image,
                                     PathUtil.get_project_resources().joinpath(record.identifier_image))
        self.__update_image_widget__(view.img_grp_results_image,
                                     PathUtil.get_project_resources().joinpath(record.result_image))

    def handle_search_button_press(self, identifier):
        if self._db_service_.get_index_of_item(identifier) is None:
            self._editor_view_.send_message_box("Identifier not found!")
        else:
            self.update_view_fields(identifier)

    def handle_previous_button_press(self, identifier):
        record_index = self._db_service_.get_index_of_item(identifier)
        record_index -= 1
        record = self._db_service_.get_first_item_by_index(record_index)
        if record is None:
            self._editor_view_.send_message_box("This is the first record.")
        else:
            self.update_view_fields(record.identifier)

    def handle_next_button_press(self, identifier):
        record_index = self._db_service_.get_index_of_item(identifier)
        record_index += 1
        record = self._db_service_.get_first_item_by_index(record_index)
        if record is None:
            self._editor_view_.send_message_box("This is the last record.")
        else:
            self.update_view_fields(record.identifier)

    @staticmethod
    def __convert_array_to_printable_string__(array):
        result_string = ""
        for num in array:
            result_string += str(num)
            result_string += ", "
        return result_string.strip().strip(',')

    def __update_image_widget__(self, img_group, path):
        view = self._editor_view_
        canvas_height = int(img_group.canvas.cget("height"))
        canvas_width = int(img_group.canvas.cget("width"))
        view.update_img_in_canvas(img_group,
                                  ImageUtil.build_photo_image_by_path(path, canvas_width, canvas_height))
