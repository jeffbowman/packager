from nose.tools import *
from packager.file import Copy, Move

def test_move_command():
    opts = {'source': {'name': '/tmp', 'contents': ['foo']}, 'target': {'name': 'mytmp'}}
    m = Move(opts)
    assert_equal(m.source, '/tmp')
    assert_equal(1, len(m.src_contents))
    assert_equal(m.target, 'mytmp')

def test_move_command_no_contents():
    opts = {'source': {'name': '/tmp'}, 'target': {'name': 'mytmp'}}
    m = Move(opts)
    assert_equal(m.source, '/tmp')
    assert m.src_contents == None
    assert_equal(m.target, 'mytmp')

def test_copy_command():
    opts = {'source': {'name': '/tmp', 'contents': ['foo']}, 'target': {'name': 'mytmp'}}
    c = Copy(opts)
    assert_equal(c.source, '/tmp')
    assert_equal(1, len(c.src_contents))
    assert_equal(c.target, 'mytmp')

def test_copy_command_no_contents():
    opts = {'source': {'name': '/tmp'}, 'target': {'name': 'mytmp'}}
    c = Copy(opts)
    assert_equal(c.source, '/tmp')
    assert c.src_contents == None
    assert_equal(c.target, 'mytmp')
