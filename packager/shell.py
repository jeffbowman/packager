from command import Command

class Shell(Command):
    """Command to run shell commands.

    Used when other commands are not provided or not
    sufficient. Prefer an existing command to this, but use if
    necessary.

    Required:
      execute

    Optional:
      source
      target

    yaml syntax
    ---
      - shell:
          source:
            name: String
            contents: [list of String]
          target:
            name: String
          execute: String

    """
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
