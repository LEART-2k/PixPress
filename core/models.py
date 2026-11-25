from enum import Enum


class ImageFormat(Enum):
    WEBP = "WEBP"
    JPEG = "JPEG"
    PNG = "PNG"

    @property
    def extension(self) -> str:
        extensions = {
            ImageFormat.WEBP: "",
            ImageFormat.JPEG: "",
            ImageFormat.PNG: "",
        }
        return extensions[self]


