from pathlib import Path


def count_number_of_line(filename: str) -> int:
    with open(filename, "rt") as file_:
        return file_.read().count("\n")


def test_naive() -> None:
    # setup
    temp_file = Path("/tmp/test_toto")
    temp_file.write_text("allo\nmon\ncoco\n")
    assert count_number_of_line(temp_file) == 3
    temp_file.unlink()


def test_with_basic_fixture(tmp_path: Path) -> None:
    temp_file = tmp_path / "test_file"
    temp_file.write_text("allo\nmon\ncoco\n")
    assert count_number_of_line(temp_file) == 3


