from abc import ABC, abstractmethod


class IEmailSender(ABC):

    @abstractmethod
    def send(self, addresses, header, html):
        pass
