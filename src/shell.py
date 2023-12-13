from visitor import ShellVisitor
from handler import CommandHandler
import sys
import os


def eval(cmdline):
    if not cmdline:
        return eval("echo")
    visitor = ShellVisitor()
    call = visitor.getCall(cmdline)

    handler = CommandHandler()
    handler.process_call(call)

    outer = handler.get_out()
    return outer


def non_interactive_mode(args):
    if len(args) - 1 != 2:
        raise ValueError("wrong number of command line arguments")
    if args[1] != "-c":
        raise ValueError(f"unexpected command line argument {args[1]}")
    out = eval(args[2])
    while len(out) > 0:
        print(out.popleft(), end="")


def interactive_mode():
    print(os.getcwd() + "> ", end="")
    out = eval(input())
    while len(out) > 0:
        print(out.popleft(), end="")


def main():
    args_num = len(sys.argv) - 1
    if args_num > 0:
        non_interactive_mode(sys.argv)
    else:
        while True:
            interactive_mode()


if __name__ == "__main__":
    main()
