# coding=utf-8
import os
from configparser import RawConfigParser


class MyConfig:

    def __init__(self):
        curr_path = os.path.dirname(os.path.realpath(__file__))
        self.conf_path = os.path.join(curr_path, 'config.ini')
        self.config = RawConfigParser()
        self.config.read(self.conf_path, encoding='utf-8')

    def get_conf(self, title, value):
        """配置文件读取"""

        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """配置文件修改"""

        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_section(self, title):
        """配置文件添加section"""

        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def remove_option(self, title, value):
        """配置文件删除option"""

        self.config.remove_option(title, value)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def remove_section(self, title):
        """配置文件删除section"""

        self.config.remove_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
