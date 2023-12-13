from antlr4 import CommonTokenStream, InputStream, ParseTreeVisitor

from parser.shellLexer import shellLexer
from parser.shellParser import shellParser


class ShellVisitor(ParseTreeVisitor):
    def visitCmdline(self, ctx: shellParser.CmdlineContext):
        return self.visit(ctx.commands())

    def visitCommands(self, ctx: shellParser.CommandsContext):
        command_results = [self.visit(command) for command in ctx.command()]
        return command_results

    def visitCommand(self, ctx: shellParser.CommandContext):
        return self.visit(ctx.pipe())

    def visitPipe(self, ctx: shellParser.PipeContext):
        commands = [self.visit(call) for call in ctx.call()]
        return commands

    def visitCall(self, ctx: shellParser.CallContext):
        cmd = self.visit(ctx.cmd()) if ctx.cmd() else None
        arguments = [self.visit(arg) for arg in ctx.argument()] or None
        subcommands = [self.visit(subcmd) for subcmd in
                       ctx.subcommand()] or None
        inputFile, outputFile = self.getRedirections(ctx)

        call = {
            "cmd": cmd,
            "arguments": arguments,
            "subcommands": subcommands,
            "inputFile": inputFile,
            "outputFile": outputFile,
        }
        if call["cmd"] is None and call["inputFile"] is not None:
            call["cmd"] = "<"
            call["arguments"] = [call["inputFile"]]
            call["inputFile"] = None
        # print(call)
        return call

    def getRedirections(self, ctx):
        redirections = self.handleRedirection(ctx)

        inputFile = [
                        redirection[1] for redirection in redirections if
                        redirection[0] == "<"
                    ] or None
        outputFile = [
                         redirection[1] for redirection in redirections if
                         redirection[0] == ">"
                     ] or None

        inputFile = (
            inputFile[0] if inputFile is not None and len(
                inputFile) == 1 else inputFile
        )
        outputFile = (
            outputFile[0]
            if outputFile is not None and len(outputFile) == 1
            else outputFile
        )
        return inputFile, outputFile

    def handleRedirection(self, ctx: shellParser.CallContext):
        redirections = []

        for child in ctx.children:
            # To handle redirection in beginning like '> hi.txt'
            if isinstance(child, shellParser.RedirectionContext):
                redirection_ctx = child
                redirection = self.visit(
                    redirection_ctx) if redirection_ctx else None
                redirections.append(redirection)
                break
            # To handle usual redirection cases
            elif isinstance(child, shellParser.AtomContext):
                for atom_child in child.children:
                    if isinstance(atom_child, shellParser.RedirectionContext):
                        redirection_ctx = atom_child
                        redirection = (
                            self.visit(
                                redirection_ctx) if redirection_ctx else None
                        )
                        redirections.append(redirection)
                        break
        return redirections

    def visitCmd(self, ctx: shellParser.CmdContext):
        if ctx.SINGLE_QUOTED():
            return ctx.SINGLE_QUOTED().getText()[1:-1]
        elif ctx.DOUBLE_QUOTED():
            return ctx.DOUBLE_QUOTED().getText()[1:-1]
        elif ctx.BACKQUOTED():
            return ctx.BACKQUOTED().getText()
        elif ctx.UNQUOTED():
            return ctx.UNQUOTED().getText()
        else:
            return self.visit(ctx.redirection())

    def visitSubcommand(self, ctx: shellParser.SubcommandContext):
        return self.visit(ctx.commands())

    def visitArgument(self, ctx: shellParser.ArgumentContext):
        arguments = []

        for arg in ctx.children:
            if isinstance(arg, shellParser.QuotedContext):
                arguments.append(self.visit(arg))
            elif isinstance(arg, shellParser.UnquotedContext):
                unquoted_arg = self.visit(arg)
                arguments.append(unquoted_arg)
        return arguments

    def visitUnquoted(self, ctx: shellParser.UnquotedContext):
        uq = ctx.UNQUOTED().getText()
        if uq[0] == '"' or uq[0] == "'":
            uq = uq[1:]
        if '"' in uq:
            new_uq = ""
            for char in uq:
                if char != '"':
                    new_uq += char
            uq = new_uq
        return uq

    def visitQuoted(self, ctx: shellParser.QuotedContext):
        if ctx.SINGLE_QUOTED():
            return ctx.SINGLE_QUOTED().getText()
        elif ctx.DOUBLE_QUOTED():
            return ctx.DOUBLE_QUOTED().getText()[1:-1]
        elif ctx.BACKQUOTED():
            return ctx.BACKQUOTED().getText()

    def visitRedirection(self, ctx: shellParser.RedirectionContext):
        redirect_type = ctx.children[0].getText()
        argument = self.visit(ctx.argument())
        return redirect_type, argument

    def converter(self, string_to_parse):
        input_stream = InputStream(string_to_parse)
        lexer = shellLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = shellParser(tokens)
        tree = parser.cmdline()
        custom_visitor = ShellVisitor()
        result = custom_visitor.visit(tree)
        return result

    def filterArgs(self, call_list, echo_flag):
        if call_list is None:
            return
        res = [arg for arg in call_list[0] if arg]
        if not echo_flag:
            temp = []
            for arg in res:
                if arg[0] == arg[-1] == "'":
                    temp.append(arg[1:-1])
                else:
                    temp.append(arg)
            res = temp
        return res

    def cleanArgs(self, cmd_line):
        for command in cmd_line:
            for call_dict in command:
                echo_flag = True if call_dict["cmd"] == "echo" else False
                call_dict["arguments"] = self.filterArgs(
                    call_dict["arguments"], echo_flag
                )
        return cmd_line

    def getSubCall(self, cmd_line):
        for command in cmd_line:
            for call_dict in command:
                if call_dict["arguments"] is not None:
                    for index, args in enumerate(call_dict["arguments"]):
                        if len(args) > 0 and args[0] == args[-1] == "`":
                            sub_cmdline = self.converter(args[1:-1])
                            sub_cmdline = self.cleanArgs(sub_cmdline)
                            call_dict["subcommands"] = {}
                            call_dict["subcommands"][index] = sub_cmdline
        return cmd_line

    def getCmd_get_call(self, call_dict):
        cmd_subCall = self.converter(call_dict["cmd"][1:-1])
        cmd_subCall = self.cleanArgs(cmd_subCall)
        call_dict["cmd"] = cmd_subCall

    def getCmd_subCall_callDict(self, call_dict):
        if call_dict["cmd"] is not None:
            if (
                    len(call_dict["cmd"]) > 0
                    and call_dict["cmd"][0] == call_dict["cmd"][-1] == "`"
            ):
                self.getCmd_get_call(call_dict)
                return

    def getCmd_subCall_cmd(self, command):
        for call_dict in command:
            return self.getCmd_subCall_callDict(call_dict)

    def getCmd_SubCall(self, cmd_line):
        for command in cmd_line:
            self.getCmd_subCall_cmd(command)
        return cmd_line

    def getCall(self, command_string):
        cmdline = self.converter(command_string)
        cmdline = self.cleanArgs(cmdline)
        cmdline = self.getSubCall(cmdline)
        cmdline = self.getCmd_SubCall(cmdline)
        return cmdline
