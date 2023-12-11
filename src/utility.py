from exceptions import FlagError
from exceptions import InvalidFormatError
import os


class File:
    def __init__(self, file):
        self.file = file

    def read_lines(self):
        with open(self.file, 'r') as fin:
            lines = fin.readlines()
        return lines

    def read(self):
        with open(self.file, 'r') as fin:
            line = fin.read()
        return line

    def write(self, output):
        with open(self.file, 'w') as fout:
            fout.write(output)
        return


class Validator:
    @staticmethod
    def check_flag(given_flag, actual_flag):
        if given_flag != actual_flag:
            raise FlagError(f"Error: Wrong flag name given. Expected: \"{actual_flag}\" Given: \"{given_flag}\"")

    @staticmethod
    def check_path_exists(path):
        if not os.path.exists(path):
            raise FlagError(f"Error: '{path}': Path does not exist")

    @staticmethod
    def check_string_isdigit(char):
        if not char.isdigit():
            raise InvalidFormatError(f"Error: Invalid flag argument. Expected digit(s)")
