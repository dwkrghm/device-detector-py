""" """

from device_detector_py.parser.client.abstract_client_parser import AbstractClientParser


class Engine(AbstractClientParser):
    """Client parser for browser engine detection"""


class Version(AbstractClientParser):
    """Client parser for browser engine version detection"""
