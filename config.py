# -*- coding:utf-8 -*-


import os
import configparser


class Config(object):
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: " + config_file)
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)


base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
print(base_path)
global_config = Config(base_path)
