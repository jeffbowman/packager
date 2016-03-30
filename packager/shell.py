from command import Command

class Shell(Command):
    def __init__(self, opts):
        if not opts.has_key('execute'):
            raise Exception('A shell command must have an "execute" tag, provided: ', opts)
        self.execute = opts['execute']

        if not opts.has_key('source'):
            self.source = None
        else:
            self.source = opts['source']['name']

        if not opts.has_key('target'):
            self.target = None
        else:
            self.target = opts['target']['name']
