from command import Command

class Archive(Command):
    """Command to create an archive of files, either as a zip or tar
    file. Tar files can optionally be compressed.

    Required:
      source
      archive_name
      type (zip|tar)

    Optional:
      target
      compress (True|False) (ignored if type is zip)

    yaml syntax:
    ---
      - archive:
          source:
            name: String
            contents: [list of String]
          target:
            name: String
          archive_name: string
          type: tar|zip
          compress: Boolean (default=False if type=tar; if type=zip default=True)

    """

    def __init__(self, opts):
        if not opts.has_key('source'):
            raise Exception('source must be provided for archive in ', opts)

        if not opts.has_key('target'):
            self.target = None
        else:
            self.target = opts['target']['name']

        if not opts['source'].has_key('contents'):
            self.src_contents = None
        else:
            self.src_contents = opts['source']['contents']

        if not opts.has_key('archive_name'):
            raise Exception('archive_name must be provided for archive in ', opts)
        else:
            self.archive_name = opts['archive_name']

        if not opts.has_key('type'):
            raise Exception('type must be provided for archive and must be one of zip or tar in ', opts)
        else:
            self.type = opts['type']

        if not opts.has_key('compress'):
            self.compress = False if opts['type'] == 'tar' else True
        else:
            self.compress = opts['compress']

        self.source = opts['source']['name']


        name = self.archive_name + "." + self.type
        ending = '.gz' if self.compress and self.type == 'tar' else ''
        cmd = 'tar -czf ' if self.type == 'tar' else 'zip '
        contents = '*' if self.src_contents == None else ' '.join(self.src_contents)
        cmd += name + ending + ' ' + contents

        self.execute = cmd
