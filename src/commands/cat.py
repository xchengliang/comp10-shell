from commands.command import Command
from utility import File
from utility import Validator


class Cat(Command):
    def execute(self, args, stdIn=None):
        concat_output = ""
        if args:
            for file_path in args:
                Validator.check_path_exists(file_path)
                concat_output += File(file_path).read()
        elif stdIn is not None:
            for line in stdIn:
                concat_output += line

        return concat_output + "\n"
