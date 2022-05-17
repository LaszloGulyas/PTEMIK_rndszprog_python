import tkinter
from tkinter import PhotoImage


class ImageUtil:
    @staticmethod
    def build_photo_image_by_path(img_path, resize_x, resize_y) -> PhotoImage:
        image = tkinter.PhotoImage(file=img_path)
        if image.width() == 0 or image.height() == 0:
            return image

        while image.width() > resize_x or image.height() > resize_y:
            image = image.subsample(2)
        return image
