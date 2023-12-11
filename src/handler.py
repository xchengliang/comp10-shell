from commandFactory import CommandFactory
from collections import deque
from utility import File
from exceptions import MultipleRedirectionError
from exceptions import CommandNotFoundError


class CommandHandler:
    def __init__(self):
        self.out = deque()

    def get_out(self):
        return self.out

    def get_handler_elems(self, command_dict):
        cmd = command_dict['cmd']
        args = command_dict['arguments']
        inputFile = command_dict['inputFile']
        if inputFile is not None and len(inputFile) == 1:
            inputFile = File(inputFile[0]).read_lines()
        elif inputFile is not None:
            inputFile = 'raise_error'
        outputFile = command_dict['outputFile']
        return [cmd, args, inputFile, outputFile]

    def handle_pipe(self, pipe):
        if pipe[-1] is not None:
            return pipe[-1].split('\n')
        return

    def handle_substituted_cmd(self, sub_cmd):
        return self.process_sub_call(sub_cmd)[0][0]

    def get_new_arg_echo_sub(self, dict_call, sub_output, sub_index):
        modified_arg = ""
        for arg in dict_call[1][:sub_index]:
            modified_arg += arg
        modified_arg += sub_output[0][0]
        for arg in dict_call[1][sub_index + 1:]:
            modified_arg += arg
        return [modified_arg]

    def echo_sub(self, command_dict, dict_call, sub_output, index):
        for sub_index in command_dict['subcommands']:
            if 0 < sub_index < len(dict_call[1]) - 1:
                dict_call[1] = self.get_new_arg_echo_sub(dict_call, sub_output, sub_index)
            else:
                dict_call[1] = dict_call[1][:index] + [arg[0] for arg in sub_output] + dict_call[1][index + 1:]

    def handle_substituted_arg(self, command_dict, dict_call, sub_output, index):
        if command_dict['cmd'] == 'echo':
            self.echo_sub(command_dict, dict_call, sub_output, index)
        else:
            dict_call[1] = dict_call[1][:index] + sub_output[0] + dict_call[1][index + 1:]

    def pipe(self, pipe, dict_call):
        if pipe and dict_call[2] is None:
            dict_call[2] = self.handle_pipe(pipe)

    def process(self, commands, out):
        for command in commands:
            pipe = []
            for command_dict in command:
                dict_call = self.get_handler_elems(command_dict)
                self.pipe(pipe, dict_call)

                if isinstance(command_dict['cmd'], list):
                    dict_call[0] = self.handle_substituted_cmd(command_dict['cmd'])

                if command_dict['subcommands'] is not None:
                    for index in command_dict['subcommands']:
                        sub_call = command_dict['subcommands'][index]
                        sub_output = self.process_sub_call(sub_call)
                        self.handle_substituted_arg(command_dict, dict_call, sub_output, index)

                output = self.run_call(dict_call)
                if dict_call[3] is not None and len(dict_call[3]) == 1:
                    File(dict_call[3][0]).write(output)
                else:
                    pipe.append(output.strip() if output is not None else output)

            if pipe:
                out.append(pipe[-1]+'\n' if pipe[-1] is not None else pipe[-1])

    def process_sub_call(self, commands):
        out = []
        self.process(commands, out)
        out = [line.strip('\n').split('\n') for line in out]
        # print(out)
        return out

    def process_call(self, commands):
        out = []
        self.process(commands, out)
        for output in out:
            if output is not None:
                self.out.append(output)

    def run_redir_infront(self, args):
        new_args = []
        for arg in args:
            if arg:
                if arg.startswith('_'):
                    if CommandFactory().is_command(arg[1:]):
                        cmd = arg
                elif CommandFactory().is_command(arg):
                    cmd = arg
                else:
                    new_args.append(arg)
        args = new_args
        return cmd, args

    def check_redir(self, stdIn, stdOut):
        stdIn_error = "Error: Multiple Input Redirections given"
        stdOut_error = "Error: Multiple Output Redirections given"
        if stdIn == "raise_error":
            raise MultipleRedirectionError(stdIn_error)
        if stdOut is not None and len(stdOut) != 1:
            raise MultipleRedirectionError(stdOut_error)

    def run_call(self, dict_call):
        cmd = dict_call[0]
        args = dict_call[1]
        stdIn = dict_call[2]
        stdOut = dict_call[3]

        if cmd == '<':
            cmd, args = self.run_redir_infront(args)

        if cmd.startswith('_'):
            try:
                command = CommandFactory().get_command(cmd[1:])
                self.check_redir(stdIn, stdOut)
                return command.execute(args, stdIn)
            except CommandNotFoundError as e:
                return f"{e}\n"
            except MultipleRedirectionError as e:
                return f"{e}\n"
            except Exception as e:
                return f"{e}\n"

        else:
            command = CommandFactory().get_command(cmd)
            self.check_redir(stdIn, stdOut)
            return command.execute(args, stdIn)
