""" """

from abc import ABC

from device_detector_py.parser.abstract_parser import AbstractParser


class AbstractDeviceParser(ABC, AbstractParser):
    """Abstract class for all device parsers"""
