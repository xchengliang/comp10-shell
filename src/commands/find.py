from commands.command import Command
from exceptions import FlagError
from utility import Validator
import os
import fnmatch


class Find(Command):
    @staticmethod
    def validate_flags(args):
        num_args = len(args)
        if num_args == 2:
            path = '.'
            Validator.check_flag(args[0], "-name")
            pattern = args[-1]
        elif num_args == 3:
            path = args[0]
            Validator.check_path_exists(path)
            Validator.check_flag(args[1], "-name")
            pattern = args[2]
        else:
            raise FlagError("Error: Wrong number of flags given")
        return path, pattern

    @staticmethod
    def find_files(path, pattern):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, pattern):
                yield os.path.join(dirpath, filename)

    def execute(self, args, stdIn=None):
        path, pattern = self.validate_flags(args)
        matched_files = self.find_files(path, pattern)
        return '\n'.join(matched_files)+'\n'
