from pathlib import Path

from _pytest._py.path import LocalPath

from solid.single_responsability.file_manager import FileManager


class TestFileManagerTest:

    def test_happy_path(self, tmpdir: LocalPath):
        file_ = Path(tmpdir) / "something"
        service = FileManager(file_)
        service.write("le petit canard")
        assert file_.is_file()
        assert service.read() == "le petit canard"

    def test_compressed_happy_path(self, tmpdir: LocalPath):
        file_ = Path(tmpdir) / "something"
        service = FileManager(file_)
        service.write("le petit canard")
        service.compress()
        assert file_.read_bytes() != "le petit canard".encode('utf-8')
        service.decompress()
        assert service.read() == "le petit canard"