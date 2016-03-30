from nose.tools import *
from packager.npm import Compile, Doc

def test_compile_command():
    opts = {'source': {'name': '/tmp'}, 'vars': [{'env': {'name': 'NODE_ENV', 'value': 'production'}}]}
    c = Compile(opts)
    assert_equal(c.source, '/tmp')
    assert_equal(1, len(c.vars))
    assert_equal(c.vars[0]['env']['name'], 'NODE_ENV')
    assert_equal(c.vars[0]['env']['value'], 'production')
    assert_equal(c.execute, 'NODE_ENV=production npm run compile')


def test_doc_command():
    opts = {'source': {'name': '/tmp'}}
    d = Doc(opts)
    assert_equal(d.target, None)
    assert_equal(d.execute, 'npm run doc')
