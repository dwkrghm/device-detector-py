""" """

from device_detector_py.parser.abstract_bot_parser import AbstractBotParser


class Bot(AbstractBotParser):
    """
    Parses a user agent for bot information

    Detected bots are defined in regexes/bots.yml
    """
