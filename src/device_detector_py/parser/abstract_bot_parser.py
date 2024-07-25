""" """

from abc import ABCMeta, abstractmethod


class AbstractBotParser(metaclass=ABCMeta):
    """Abstract class for all bot parsers"""

    @abstractmethod
    def discard_details(self) -> None: ...
