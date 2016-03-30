from command import Command
import shutil
import os
import logging

class File(Command):
    def __init__(self, opts):
        if not opts.has_key('source'):
            raise Exception('source tag must be provided in ', opts)
        else:
            self.source = opts['source']['name']

        if not opts.has_key('target'):
            raise Exception('target tag must be provided in ', opts)
        else:
            self.target = opts['target']['name']

        if opts['source'].has_key('contents'):
            self.src_contents = opts['source']['contents']
            if not type(self.src_contents) == list:
                raise Exception('source contents must be a list in ', opts)
        else:
            self.src_contents = None

class Move(File):
    def __init__(self, opts):
        super(Move, self).__init__(opts)
        if opts.has_key('execute'):
            self.execute = opts['execute']
        else:
            self.execute = None

    def do(self):
        if self.execute != None:
            super(Move, self).do()
            return

        src = os.path.abspath(self.source)
        target = os.path.abspath(self.target)

        if not os.path.exists(target):
            print('making target: ' + target)
            os.makedirs(target)

        if self.src_contents != None:
            files = self.src_contents
        else:
            files = os.listdir(src)

        for f in [src + '/' + f for f in files]:
            logging.info('move ' + f + ' -> ' + target)
            shutil.move(f, target)

class Copy(File):
    def __init__(self, opts):
        super(Copy, self).__init__(opts)
        if opts.has_key('execute'):
            self.execute = opts['execute']
        else:
            self.execute = None

    def do(self):
        if self.execute != None:
            super(File, self).do()

        src = os.path.abspath(self.source)
        target = os.path.abspath(self.target)

        if not os.path.exists(target):
            os.makedirs(target)

        if self.src_contents != None:
            files = [src + '/' + f for f in self.src_contents]
        else:
            files = [src + '/' + f for f in os.listdir(src)]

        for f in files:
            logging.info('copy ' + f + ' -> ' + target)
            shutil.copy(f, target)
