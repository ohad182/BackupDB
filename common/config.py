import os

from common import try_parse_int

try:
    import ConfigParser as cp
except ImportError as e:
    import configparser as cp


class Configuration(object):
    ENV = "ENV"

    def __init__(self):
        self.config = cp.RawConfigParser()
        self.config_path = None

    def get(self, section, option, default):
        return try_parse_int(self.config.get(section, option)) if self.config.has_option(section, option) else default

    def read_cwd(self, file_name: str = None, file_ext='ini'):
        print("Searching for {} at : {}".format('configuration file' if file_name is None else file_name, os.getcwd()))
        config_file = None
        for current_file in os.listdir(os.getcwd()):
            if file_name is not None:
                if file_name in current_file:
                    config_file = current_file
                    break
            elif file_ext is not None:
                if current_file.endswith(file_ext):
                    config_file = current_file
                    break
            else:
                raise Exception("Cannot find configuration file, please specify file name or extension")

        if config_file:
            self.read(config_file)
            print("Found {}".format(config_file))
            self.expose_env()
        else:
            print("No config file found")

    def read(self, config_file):
        self.config.read(config_file)
        self.config_path = config_file

    def expose_env(self):
        if self.config.has_section(Configuration.ENV):
            for var_name in self.config.options(Configuration.ENV):
                var_name = var_name.upper()
                var_value = self.config.get(Configuration.ENV, var_name).replace('"', "").replace("'", '')
                print("Extending {} - {}: {}".format(Configuration.ENV, var_name, var_value))
                os.environ[var_name] = var_value
