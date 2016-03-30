from nose.tools import *
from packager.archive import Archive
import types

def do(self):
    cmd = 'tar -czf ' if self.type == 'tar' else 'zip'
    name_type = '.' + self.type
    ending = '.gz' if self.compress else ''
    name = self.archive_name + name_type + ending
    contents = '*' if self.src_contents == None else ' '.join(self.src_contents)
    cmd += name + ' ' + contents
    return cmd

def test_archive_command():
    opts = {'source': {'name': '/tmp', 'contents': ['foo', 'bar', 'baz']}, 'target': {'name': 'mytmp'}, 'archive_name': 'arc_name', 'type': 'tar', 'compress': True}
    a = Archive(opts)
    a.do = types.MethodType(do, a)
    assert_equals(a.source, '/tmp')
    assert_equals(a.target, 'mytmp')
    assert_equals(3, len(a.src_contents))
    assert_equals(a.archive_name, 'arc_name')
    assert_equals(a.compress, True)
    assert_equals(a.do(), 'tar -czf arc_name.tar.gz foo bar baz')
