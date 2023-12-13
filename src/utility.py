import os

from exceptions import FlagError, InvalidFormatError


class File:
    def __init__(self, file):
        self.file = file

    def read_lines(self):
        with open(self.file, "r") as fin:
            lines = fin.readlines()
        return lines

    def read(self):
        with open(self.file, "r") as fin:
            line = fin.read()
        return line

    def write(self, output):
        with open(self.file, "w") as fout:
            fout.write(output)
        return


class Validator:
    @staticmethod
    def check_flag(given_flag, actual_flag):
        msg = "Error: Wrong flag name given."
        msg2 = f"Expected: '{actual_flag}' Given: '{given_flag}'"
        if given_flag != actual_flag:
            raise FlagError(msg + " " + msg2)

    @staticmethod
    def check_path_exists(path):
        if not os.path.exists(path):
            raise FlagError(f"Error: '{path}': No such file or directory")

    @staticmethod
    def check_path_exists_bool(path):
        return os.path.exists(path)

    @staticmethod
    def check_string_isdigit(char):
        msg = "Invalid flag argument. Expected digit(s)"
        if not char.isdigit():
            raise InvalidFormatError(msg)
