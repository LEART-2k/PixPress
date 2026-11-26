from pathlib import Path
from PIL import Image, ImageOps
from attrs import frozen
import core.protocols as proto
from core.models import ConversionConfig, ConversionResult, ImageFormat
from statuses import MISSING

SUPPORTED_EXTENSIONS = frozenset({".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"})
DEFAULT_BACKGROUND_COLOR = (255, 255, 255)
PNG_COMPRESSION_LEVEL = 6


@frozen
class PillowImageProcessor(proto.ImageProcessor):
    _background_color: tuple[int, int, int] = DEFAULT_BACKGROUND_COLOR

    def process(self,
                source_path: Path,
                output_dir: Path,
                config: ConversionConfig,
                index: int = 1) -> ConversionResult:
        if not source_path.exists():
            raise FileNotFoundError(f"File not found: {source_path}")

        output_dir.mkdir(parents=True, exist_ok=True)
        original_size = source_path.stat().st_size
        output_path = self._build_output_path(source_path, output_dir, config, index)

...