import io
import unittest
from shell import eval, main, interactive_mode
from exceptions import FlagError, InvalidFormatError, CommandNotFoundError
from unittest.mock import patch


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = eval("echo foo")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ["foo"])
        self.assertEqual(len(out), 0)

    def test_shell_main2(self):
        with patch('sys.argv', new=['script_name', '-c', 'echo']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                main()
                self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_shell_main_ValueError(self):
        with patch('sys.argv', new=['script_name', 'echo foo bar', '-c']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                with self.assertRaises(ValueError):
                    main()

    def test_shell_main_ValueError2(self):
        with patch('sys.argv', new=['script_name', '-c', 'echo foo', "echo ss"]):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                with self.assertRaises(ValueError):
                    main()

    @patch('builtins.input', return_value='echo')
    @patch('builtins.print')
    def test_interactive_mode(self, mock_input, mock_print):
        with io.StringIO() as buf, patch('sys.stdout', buf):
            interactive_mode(flag=True)
            output = buf.getvalue()
        expected_output = ''
        self.assertIn(expected_output, output)

    def test_pipe(self):
        out = eval("echo foo bar | cat")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ["foo bar"])
        self.assertEqual(len(out), 0)

    def test_cat_single_file(self):
        out = eval("cat test/file1.txt")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['AAA', 'AAA', 'BBB', 'ABA'])

    def test_cat_multiple_files(self):
        out = eval("cat 'test/file1.txt' 'test/file2.txt'")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['AAA', 'AAA', 'BBB', 'ABA', 'CCCC', 'DDD', 'CDCD', 'CCCC'])

    def test_cat_no_args(self):
        out = eval("cat")
        result = out.popleft()
        self.assertEqual(result, "\n")

    def test_cat_empty_file(self):
        out = eval("cat test/empty.txt")
        result = out.popleft()
        self.assertEqual(result, '\n')

    def test_cat_head(self):
        out = eval("cat test/file1.txt | head -n 2")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['AAA', 'AAA'])

    def test_cat_head_no_arg(self):
        out = eval("cat test/file2.txt | head")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['CCCC', 'DDD', 'CDCD', 'CCCC'])

    def test_cat_tail(self):
        out = eval("cat test/file1.txt | tail -n 2")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['BBB', 'ABA'])

    def test_cat_tail_no_arg(self):
        out = eval("cat test/file1.txt | tail")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['AAA', 'AAA', 'BBB', 'ABA'])

    def test_cd_pwd_semicolon(self):
        out = eval("cd tools; pwd")
        result = out.popleft().strip()
        self.assertEqual(result, "/comp0010/tools")

    def test_cd_pwd_semicolon2(self):
        out = eval("cd ..; pwd")
        stdout = out.popleft()
        result = stdout.strip()
        self.assertEqual(result, "/comp0010")

    def test_cd_not_found(self):
        with self.assertRaises(FlagError):
            eval("cd wrongDir")

    def test_cd_no_args(self):
        with self.assertRaises(ValueError):
            eval("cd ")

    def test_cut_interval(self):
        out = eval("cut -b 1-3 test/file2.txt")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['CCC', 'DDD', 'CDC', 'CCC'])

    def test_cut_open_interval(self):
        out = eval("cut -b 2- test/file2.txt")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['CCC', 'DD', 'DCD', 'CCC'])

    def test_cut_intervals(self):
        out = eval("echo abcdefgfhdasdas | cut -b 1-2,4-5")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['abde'])

    def test_cut_stdin(self):
        out = eval("echo abc | cut -b 1")
        result = out.popleft().strip()
        self.assertEqual(result, "a")

    def test_cut_union(self):
        out = eval("echo abc | cut -b -1,2-")
        result = out.popleft().strip()
        self.assertEqual(result, "abc")

    def test_cut_wrong_args_num(self):
        with self.assertRaises(FlagError):
            eval("cut -b -c 1- test/file1.txt")

    def test_cut_wrong_range(self):
        with self.assertRaises(InvalidFormatError):
            eval("cut -b 1-2-3 test/file1.txt")

    def test_echo_single_arg(self):
        out = eval("echo 'hello'")
        result = out.popleft()
        self.assertEqual(result, "hello\n")

    def test_echo_multi_args(self):
        out = eval("echo 'Hello' 'World'")
        result = out.popleft()
        self.assertEqual(result, 'Hello World\n')

    def test_echo_no_args(self):
        out = eval("echo")
        result = out.popleft()
        self.assertEqual(result, "\n")

    def test_echo_substitution(self):
        out = eval("echo `echo foo`")
        result = out.popleft()
        self.assertEqual(result, 'foo\n')

    def test_find(self):
        out = eval("find -name *.txt")
        result = out.popleft()
        self.assertEqual(result, './requirements.txt\n')

    def test_find_dir(self):
        cmdline = "find test -name '*.txt'"
        out = eval(cmdline)
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['test/file1.txt', 'test/file2.txt', 'test/empty.txt'])

    def test_find_wrong(self):
        with self.assertRaises(FlagError):
            eval("find test -name '*.txt' -name '*.txt'")

    def test_grep(self):
        out = eval("grep AB test/file1.txt")
        result = out.popleft()
        self.assertEqual(result, 'ABA\n')

    def test_grep_stdin(self):
        out = eval("cat test/file1.txt test/file2.txt | grep '...'")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['AAA', 'AAA', 'BBB', 'ABA',
                                  'CCCC', 'DDD', 'CDCD', 'CCCC'])

    def test_grep_flag_error(self):
        with self.assertRaises(FlagError):
            eval("grep AB nonexistent.file")

    def test_grep_wrong_num_arg(self):
        with self.assertRaises(FlagError):
            eval("grep ")

    def test_head_default_lines(self):
        out = eval("head test/file1.txt")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['AAA', 'AAA', 'BBB', 'ABA'])

    def test_head_custom_lines(self):
        out = eval("head -n 3 test/file1.txt")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['AAA', 'AAA', 'BBB'])

    def test_head_wrong_args(self):
        with self.assertRaises(FlagError):
            eval("head -n 3 test/file1.txt test/file2.txt")

    def test_head_invalid_format(self):
        with self.assertRaises(InvalidFormatError):
            eval("head -n 'test/file1.txt'")

    def test_head_wrong_num_arg(self):
        with self.assertRaises(FlagError):
            eval("head -n -b -b 'test/file1.txt'")

    def test_ls_no_args(self):
        out = eval("ls")
        result = out.popleft().strip().split("\t")
        result = set(result)
        self.assertEqual(result, {'README.md', 'system_test', 'gen', 'tools', 'sh',
                                  'apps.svg', 'test', 'requirements.txt', 'Dockerfile', 'src'})

    def test_ls_dir(self):
        out = eval("ls tools")
        result = out.popleft().strip().split("\t")
        result = set(result)
        self.assertEqual(result, {'analysis', 'coverage', 'test'})

    def test_ls_wrong_num_args(self):
        with self.assertRaises(FlagError):
            eval("ls tools test")

    def test_pwd(self):
        out = eval("pwd")
        result = out.popleft().strip().split("\t")
        self.assertEqual(result, ['/comp0010'])

    def test_sort(self):
        out = eval("sort test/file1.txt")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['AAA', 'AAA', 'ABA', 'BBB'])

    def test_sort_r(self):
        out = eval("sort -r test/file1.txt")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['BBB', 'ABA', 'AAA', 'AAA'])

    def test_sort_stdin(self):
        out = eval("< test/file1.txt sort")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['AAA', 'AAA', 'ABA', 'BBB'])

    def test_sort_r_stdin(self):
        out = eval(" sort -r < test/file1.txt")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['BBB', 'ABA', 'AAA', 'AAA'])

    def test_sort_uniq(self):
        cmdline = "sort test/file2.txt | uniq"
        stdout = eval(cmdline)
        result = stdout.popleft().strip().split("\n")
        self.assertEqual(result, ['CCCC', 'CDCD', 'DDD'])

    def test_sort_i(self):
        out = eval("uniq -i test/file1.txt")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['AAA', 'BBB', 'ABA'])

    def test_sort_cat(self):
        out = eval("cat test/file2.txt | sort")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['CCCC', 'CCCC', 'CDCD', 'DDD'])

    def test_sort_i_cat(self):
        out = eval("cat test/file2.txt | sort -r")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['DDD', 'CDCD', 'CCCC', 'CCCC'])

    def test_sort_wrong_arg_num(self):
        with self.assertRaises(FlagError):
            eval("sort -r -b 'test/file1.txt'")

    def test_tail_default_lines(self):
        out = eval("tail test/file1.txt")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['AAA', 'AAA', 'BBB', 'ABA'])

    def test_tail_custom_lines(self):
        out = eval("tail -n 3 'test/file1.txt'")
        result = out.popleft().strip().split('\n')
        self.assertEqual(result, ['AAA', 'BBB', 'ABA'])

    def test_tail_invalid_format(self):
        with self.assertRaises(InvalidFormatError):
            eval("tail -n 'test/file1.txt'")

    def test_tail_wrong_num_arg(self):
        with self.assertRaises(FlagError):
            eval("tail -n -b -b 'test/file1.txt'")

    def test_tail_no_arg(self):
        out = eval("tail 'test/file1.txt'")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['AAA', 'AAA', 'BBB', 'ABA'])

    def test_tail_zero_line(self):
        out = eval("tail -n 0 test/file1.txt")
        result = out.popleft().strip()
        self.assertEqual(result, '')

    def test_uniq_stdin(self):
        stdout = eval("uniq < test/file2.txt")
        result = stdout.popleft().strip().split("\n")
        self.assertEqual(result, ['CCCC', 'DDD', 'CDCD', 'CCCC'])

    def test_uniq_one_arg(self):
        out = eval("uniq -i < test/file2.txt")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ["CCCC", "DDD", "CDCD", "CCCC"])

    def test_uniq_no_i(self):
        out = eval("uniq test/file2.txt")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ["CCCC", "DDD", "CDCD", "CCCC"])

    def test_uniq_wrong_num_arg(self):
        with self.assertRaises(FlagError):
            eval("uniq -i -b -b 'test/file1.txt'")

    def test_cmd_not_found(self):
        with self.assertRaises(CommandNotFoundError):
            eval("notcommand -r 'test/file1.txt'")

    def test_no_cmdline(self):
        out = eval("")
        result = out.popleft()
        self.assertEqual(result, '\n')

    def test_unsafe_ls(self):
        out = eval("_ls")
        result = out.popleft().strip().split("\t")
        result = set(result)
        self.assertEqual(result, {'README.md', 'system_test', 'gen', 'tools', 'sh', 'apps.svg', 'test',
                                  'requirements.txt', 'Dockerfile', 'src'})

    def test_unsafe_command_not_found(self):
        out = eval("_wrong")
        result = out.popleft().strip()
        self.assertEqual(result, "Error: Command Not Found")

    def test_unsafe_MultipleRedirectionError(self):
        out = eval("_echo foo > test/multi.txt > test/multi.txt")
        result = out.popleft().strip()
        self.assertEqual(result, "Error: Multiple Output Redirections given")

    def test_unsafe_other_error(self):
        out = eval("_cat https:sdsda")
        result = out.popleft().strip()
        self.assertEqual(result, "Error: 'https:sdsda': Path does not exist")


if __name__ == "__main__":
    unittest.main()
