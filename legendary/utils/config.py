import configparser
import os


class LGDConf(configparser.ConfigParser):
    def __init__(self, *args, **kwargs):
        self.modified = False
        self.read_only = False
        self.modtime = None
        super().__init__(*args, **kwargs)

    def read(self, filename):
        # if config file exists, save modification time
        if os.path.exists(filename):
            self.modtime = int(os.stat(filename).st_mtime)

        return super().read(filename)

    def set(self, *args, **kwargs):
        if self.read_only:
            return

        self.modified = True
        super().set(*args, **kwargs)

    def __setitem__(self, key, value):
        if self.read_only:
            return

        self.modified = True
        super().__setitem__(key, value)