from commands.command import Command
from exceptions import FlagError
from utility import File, Validator


class Wc(Command):
    def process_flag(self, arg):
        l_flag, w_flag, m_flag = False, False, False
        if arg == "-l":
            l_flag = True
        elif arg == "-w":
            w_flag = True
        elif arg == "-m":
            m_flag = True
        else:
            msg = "Error: Wrong flag name given."
            msg2 = f"Expected: -l,-w,-m Given: '{arg}'"
            raise FlagError(msg + " " + msg2)
        return l_flag, w_flag, m_flag

    def process_files(self, files):
        for file in files:
            Validator.check_path_exists(file)
        lines = []
        for file in files:
            temp_lines = File(file).read_lines()
            lines += temp_lines
        return lines

    def validate_args(self, args, stdIn):
        l, w, m = True, True, True
        num_args = len(args) if args else 0
        if num_args == 0 and stdIn is not None:
            lines = stdIn
        elif num_args > 0:
            if args[0].startswith("-"):
                l, w, m = self.process_flag(args[0])
                lines = self.process_files(args[1:])
                if not lines:
                    lines = stdIn
            else:
                lines = self.process_files(args)
        else:
            raise FlagError("Error: Wrong number of arguments given")

        return (l, w, m), lines

    def exec_l(self, lines):
        return len(lines)

    def exec_w(self, lines):
        words = 0
        for line in lines:
            temp_words = len(line.split(" "))
            words += temp_words
        return words

    def exec_m(self, lines):
        chars = 0
        for line in lines:
            temp_chars = len(line)
            chars += temp_chars
        return chars

    def execute(self, args, stdIn):
        temp = self.validate_args(args, stdIn)
        flags = temp[0]
        lines = temp[1]

        output = []

        if flags[0]:
            output.append(str(self.exec_l(lines)))
        if flags[1]:
            output.append(str(self.exec_w(lines)))
        if flags[2]:
            output.append(str(self.exec_m(lines)))

        return " ".join(output) + "\n"
