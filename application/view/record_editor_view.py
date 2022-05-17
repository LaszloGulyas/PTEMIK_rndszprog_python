import tkinter as tk
import tkinter.messagebox
from tkinter.constants import NW
from application.view.image_group import ImageGroup


class RecordEditorView:
    def __init__(self, controller):
        self._controller_ = controller

        self.window = None
        self.msg_box = None
        self.lbl_identifier = None
        self.lbl_identifier_value = None
        self.lbl_confirmed_identifier = None
        self.txt_confirmed_identifier_value = None
        self.txt_confirmed_identifier_value_var = None
        self.img_grp_identifier_image = None
        self.lbl_results = None
        self.lbl_results_value = None
        self.lbl_confirmed_results = None
        self.txt_confirmed_results_value = None
        self.txt_confirmed_results_value_var = None
        self.cvs_results_image = None
        self.cvs_results_image_file = None
        self.lbl_search_identifier = None
        self.txt_search_identifier_value = None
        self.btn_show_previous = None
        self.btn_show_next = None
        self.btn_search = None

    def show(self):
        self._create_window_()
        self._create_widgets_()
        self._controller_.init_view_fields()
        self.window.mainloop()

    def _create_window_(self):
        self.window = tk.Tk()
        self.window.title("Browser GUI")
        self.window.geometry('640x480')

    def _create_widgets_(self):
        self.msg_box = tkinter.messagebox

        self.lbl_identifier = tk.Label(self.window, text="Identifier:")
        self.lbl_identifier.place(x=20, y=30)

        self.lbl_identifier_value = tk.Label(self.window, text="")
        self.lbl_identifier_value.place(x=140, y=30)

        self.lbl_confirmed_identifier = tk.Label(self.window, text="Confirmed identifier:")
        self.lbl_confirmed_identifier.place(x=20, y=70)

        self.txt_confirmed_identifier_value_var = tk.StringVar(name="confirmed_identifier_value")
        self.txt_confirmed_identifier_value = tk.Entry(self.window,
                                                       textvariable=self.txt_confirmed_identifier_value_var, width=20)
        self.txt_confirmed_identifier_value.place(x=140, y=70)
        self.txt_confirmed_identifier_value.bind("<Return>", self.__event_enter_pressed_in_text_entry_handler)
        self.txt_confirmed_identifier_value.bind("<FocusOut>", self.__event_text_entry_focused_out_handler)

        canvas = tk.Canvas(self.window)
        canvas.configure(width=300, height=70, bg="white")
        canvas.place(x=320, y=30)
        self.img_grp_identifier_image = ImageGroup(canvas, None, None)

        self.lbl_results = tk.Label(self.window, text="Results:")
        self.lbl_results.place(x=20, y=140)

        self.lbl_results_value = tk.Label(self.window, text="")
        self.lbl_results_value.place(x=140, y=140)

        self.lbl_confirmed_results = tk.Label(self.window, text="Confirmed results:")
        self.lbl_confirmed_results.place(x=20, y=180)

        self.txt_confirmed_results_value_var = tk.StringVar(name="confirmed_results_value")
        self.txt_confirmed_results_value = tk.Entry(self.window,
                                                    textvariable=self.txt_confirmed_results_value_var, width=80)
        self.txt_confirmed_results_value.place(x=140, y=180)
        self.txt_confirmed_results_value.bind("<Return>", self.__event_enter_pressed_in_text_entry_handler)
        self.txt_confirmed_results_value.bind("<FocusOut>", self.__event_text_entry_focused_out_handler)

        canvas = tk.Canvas(self.window)
        canvas.configure(width=600, height=120, bg="white")
        canvas.place(x=20, y=220)
        self.img_grp_results_image = ImageGroup(canvas, None, None)

        self.lbl_search_identifier = tk.Label(self.window, text="Identifier:")
        self.lbl_search_identifier.place(x=200, y=370)

        self.txt_search_identifier_value_var = tk.StringVar(name="search_results_value")
        self.txt_search_identifier_value = tk.Entry(self.window,
                                                    textvariable=self.txt_search_identifier_value_var, width=20)
        self.txt_search_identifier_value.place(x=260, y=370)

        self.btn_show_previous = tk.Button(self.window, text="Show previous", command=self.__show_previous_handler)
        self.btn_show_previous.place(x=20, y=400)

        self.btn_search = tk.Button(self.window, text="Search", command=self.__submit_search_handler)
        self.btn_search.place(x=300, y=400)

        self.btn_show_next = tk.Button(self.window, text="Show next", command=self.__show_next_handler)
        self.btn_show_next.place(x=555, y=400)

    @staticmethod
    def update_txt_field_value(txt_field_var, new_value):
        txt_field_var.set(new_value)

    @staticmethod
    def update_img_in_canvas(image_group, photo_image):
        image_group.image = photo_image
        image_group.canvas.create_image(0, 0, image=image_group.image, anchor=NW)

    def send_message_box(self, message):
        self.msg_box.showinfo("Message", message)

    def __send_update_request_for_confirmed_fields__(self):
        identifier = self.lbl_identifier_value.cget("text")
        confirmed_identifier = self.txt_confirmed_identifier_value_var.get()
        confirmed_results = self.txt_confirmed_results_value_var.get()
        self._controller_.update_db_values(identifier, confirmed_identifier, confirmed_results)

    def __show_previous_handler(self):
        self.__send_update_request_for_confirmed_fields__()
        identifier_to_search = self.lbl_identifier_value.cget("text")
        self._controller_.handle_previous_button_press(identifier_to_search)

    def __submit_search_handler(self):
        self.__send_update_request_for_confirmed_fields__()
        confirmed_identifier_to_search = self.txt_search_identifier_value_var.get()
        self._controller_.handle_search_button_press(confirmed_identifier_to_search)

    def __show_next_handler(self):
        self.__send_update_request_for_confirmed_fields__()
        identifier_to_search = self.lbl_identifier_value.cget("text")
        self._controller_.handle_next_button_press(identifier_to_search)

    def __event_enter_pressed_in_text_entry_handler(self, event):
        self.__send_update_request_for_confirmed_fields__()

    def __event_text_entry_focused_out_handler(self, event):
        self.__send_update_request_for_confirmed_fields__()
