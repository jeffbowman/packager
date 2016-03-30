from command import Command

class Npm(Command):
    def __init__(self, opts):
        if not opts.has_key('source'):
            self.source = None
        else:
            self.source = opts['source']['name']

        if not opts.has_key('target'):
            self.target = None
        else:
            self.target = opts['target']['name']

        if opts.has_key('vars') and len(opts['vars']) > 0:
            self.vars = opts['vars']
            prepend = " ".join([v['env']['name'] + "=" + v['env']['value'] for v in self.vars])
            self.execute = prepend + ' npm run'
        else:
            self.execute = 'npm run'

class Compile(Npm):
    def __init__(self, opts):
        super(Compile, self).__init__(opts)
        self.execute += ' compile'

class Doc(Npm):
    def __init__(self, opts):
        super(Doc, self).__init__(opts)
        self.execute += ' doc'
