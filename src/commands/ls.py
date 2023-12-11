from commands.command import Command
from utility import Validator
from exceptions import FlagError
import os


class Ls(Command):
    @staticmethod
    def validate_args(args):
        if args is None:
            return '.'
        num_args = len(args)
        if num_args == 1:
            Validator.check_path_exists(args[0])
            return args[0]
        else:
            raise FlagError("Error: Wrong number of flags given")

    def execute(self, args, stdIn=None):
        path = self.validate_args(args)
        files = [file for file in os.listdir(path) if not file.startswith('.')]
        return '\t'.join(files) + '\n'
