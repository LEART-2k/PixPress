from enum import Enum
from pathlib import Path

from attrs import frozen

from statuses import Status, MISSING

DEFAULT_QUALITY = 85

class ImageFormat(Enum):
    WEBP = "WEBP"
    JPEG = "JPEG"
    PNG = "PNG"

    @property
    def extension(self) -> str:
        extensions = {
            ImageFormat.WEBP: ".webp",
            ImageFormat.JPEG: ".jpg",
            ImageFormat.PNG: ".png",
        }
        return extensions[self]


@frozen
class ConversionConfig:
    _target_format: ImageFormat = ImageFormat.WEBP
    _quality: int = DEFAULT_QUALITY
    _max_width: int | Status = MISSING
    _strip_exif: bool = True
    _rename_pattern: str | Status = MISSING

    @property
    def target_format(self) -> ImageFormat:
        return self._target_format

    @property
    def quality(self) -> int:
        return self._quality

    @property
    def max_width(self) -> int | Status:
        return self._max_width

    @property
    def strip_exif(self) -> bool:
        return self._strip_exif

    @property
    def rename_pattern(self) -> str | Status:
        return self._rename_pattern


@frozen()
class ConversionResult:
    _source_path: Path
    _output_path: Path
    _original_size: int
    _converted_size: int

    @property
    def source_path(self) -> Path:
        return self._source_path

    @property
    def output_path(self) -> Path:
        return self._output_path

    @property
    def original_size(self) -> int:
        return self._original_size

    @property
    def converted_size(self) -> int:
        return self._converted_size

    @property
    def saved_bytes(self) -> int:
        return self._original_size - self._converted_size

    @property
    def compression_ratio(self) -> float:
        if self._original_size <= 0:
            return 0.0
        return (1 - self._converted_size / self._original_size) * 100
