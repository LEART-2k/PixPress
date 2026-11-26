from abc import ABC, abstractclassmethod
from pathlib import Path

from core.models import ConversionConfig, ConversionResult


class ImageProcessor(ABC):
    @abstractclassmethod
    def process(self,
                source_path: Path,
                output_dir: Path,
                config: ConversionConfig,
                index: int = 1) -> ConversionResult:
        ...