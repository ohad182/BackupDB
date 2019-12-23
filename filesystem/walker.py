"""
Ability to walk the given file system and collect all relevant files
"""
import glob


class FileWalker(object):
    def __init__(self, **kwargs):
        self.root = kwargs.get('root', None)
        self.pattern = kwargs.get('pattern', '*.*')

    def walk(self):
        return [f for f in glob.glob(self.root + "*.*", recursive=True)]
