from nose.tools import *
from packager.shell import Shell
import types

def do(self): # mock do function
    return "do called: " + self.execute

def test_shell_command():
    opts = {'execute': 'echo "hello"', 'source': {'name': '/tmp'}}
    s = Shell(opts)
    s.do = types.MethodType(do, s)
    assert_equal(s.execute, 'echo "hello"')
    assert_equal(s.source, '/tmp')
    assert dir(s).index('do') > 0
    assert_equal(s.do(), 'do called: echo "hello"')

def test_shell_command_no_source():
    opts = {'execute': 'echo "hello"'}
    s = Shell(opts)
    s.do = types.MethodType(do, s)
    assert_equal(s.source, None)
    assert_equal(s.do(), 'do called: echo "hello"')

def test_shell_command_with_target():
    opts = {'execute': 'echo "hello"', 'source': {'name': '/tmp'}, 'target': {'name': 'my_tmp/', 'mkdir': True}}
    s = Shell(opts)
    assert_equal(s.target, 'my_tmp/')
