# file_manager_srp.py
import zlib
from pathlib import Path


class FileManager:
    """
    Cette classe fait plusieurs choses:
      - 4 méthodes
      - lire/écrire fichier
      - compresser/décompresser fichier
    """
    def __init__(self, filename: str | Path):
        self.path = Path(filename)

    def read(self) -> str:
        return self.path.read_text("utf-8")

    def write(self, data: str) -> None:
        self.path.write_text(data, "utf-8")

    def compress(self) -> None:
        compressed_data = zlib.compress(self.path.read_bytes())
        self.path.write_bytes(compressed_data)

    def decompress(self) -> None:
        decompressed_data = zlib.decompress(self.path.read_bytes())
        self.path.write_bytes(decompressed_data)


class RawFileManager:
    def __init__(self, filename: str | Path):
        self.path = Path(filename)

    def read(self) -> str:
        return self.path.read_text("utf-8")

    def write(self, data: str) -> None:
        self.path.write_text(data, "utf-8")


class CompressionFileManager:
    def __init__(self, filename: str | Path):
        self.path = Path(filename)

    def compress(self) -> None:
        compressed_data = zlib.compress(self.path.read_bytes())
        self.path.write_bytes(compressed_data)

    def decompress(self) -> None:
        decompressed_data = zlib.decompress(self.path.read_bytes())
        self.path.write_bytes(decompressed_data)

