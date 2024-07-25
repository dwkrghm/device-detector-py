""" """

from device_detector_py.parser.abstract_parser import AbstractParser


class OperatingSystem(AbstractParser):
    """
    Parses the useragent for operating system information

    Detected operating systems can be found in self.operating_systems and /regexes/oss.yml
    This class also defined some operating system families and methods to get the family for a specific os
    """
