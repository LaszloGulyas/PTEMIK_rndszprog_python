from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage


class ImageUtil:
    @staticmethod
    def build_photo_image_by_path(img_path, resize_x, resize_y) -> PhotoImage:
        image = Image.open(img_path)
        image = image.resize((resize_x, resize_y), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
