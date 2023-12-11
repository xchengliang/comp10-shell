from commands.command import Command


class Echo(Command):
    def execute(self, args, stdIn=None):
        if args is None:
            return '\n'
        return ' '.join(args)+'\n'
