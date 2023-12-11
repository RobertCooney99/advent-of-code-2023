from pathlib import Path
import os


def text_to_string(day, use_example=False):
    current_path = os.path.dirname(__file__)
    input_file_path = os.path.join(
        current_path, f"../../inputs/{get_input_file_name(day, '.txt', use_example)}")

    return Path(input_file_path).read_text()


def get_input_file_name(day, ext, use_example):
    return (f"day{str(day).zfill(3)}{'example' if use_example else ''}{ext}")
