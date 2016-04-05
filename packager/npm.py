from command import Command

class Npm(Command):
    """Command to run npm commands.

    This class should not be used directly, instead subclass as
    necessary to provide additional functionality

    """
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
    """Npm Compile command. Will execute `npm run compile`

    Optional:
      source (default to current directory)
      target (default will be `npm run compile` default directory
        -- if provided, is currently ignored)
      vars (environment variables which need to be set on when running)

    yaml example
    ---
      - compile:
          source:
            name: String
            contents: [list of String]
          target:
            name: String
          vars:
            - env: (can be repeated to provide additional multiple vars)
                name: String
                value: String

    """
    def __init__(self, opts):
        super(Compile, self).__init__(opts)
        self.execute += ' compile'

class Doc(Npm):
    """Npm Doc command. Will execute `npm run doc`

    Optional:
      source (default to current directory)
      target (default will be `npm run doc` default directory -- if provided, is currently ignored)
      vars (environment variables which need to be set on when running)

    yaml example
    ---
      - compile:
          source:
            name: String
            contents: [list of String]
          target:
            name: String
          vars:
            - env: (can be repeated to provide additional multiple vars)
                name: String
                value: String

    """
    def __init__(self, opts):
        super(Doc, self).__init__(opts)
        self.execute += ' doc'
