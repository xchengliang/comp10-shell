import os

from commands.command import Command
from exceptions import FileAlreadyExistsError
from exceptions import FlagError
from utility import Validator


class Mkdir(Command):
    def raise_error(self, file):
        msg = f"Error: Cannot create directory. '{file}' already exists"
        raise FileAlreadyExistsError(msg)

    def validate_args(self, args):
        num_args = len(args) if args else 0
        p = False
        if num_args == 0:
            raise FlagError("Error: mkdir: Operand missing")
        elif num_args == 1:
            if args[0].startswith('-'):
                Validator.check_flag(args[0], "-p")
                raise FlagError("Error: mkdir: Operand missing")
            else:
                dirs = args
        else:
            if args[0].startswith('-'):
                Validator.check_flag(args[0], "-p")
                p = True
                dirs = args[1:]
        return p, dirs

    def execute(self, args, stdIn):
        p, dirs = self.validate_args(args)
        for dir in dirs:
            if Validator.check_path_exists_bool(dir):
                self.raise_error(dir)
            if p:
                os.makedirs(dir)
            else:
                try:
                    os.mkdir(dir)
                except FileNotFoundError:
                    raise FlagError(f"Error: Flag -p required for '{dir}'")
