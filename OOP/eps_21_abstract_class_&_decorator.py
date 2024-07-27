from abc import ABC, abstractmethod


class Button(ABC):

    # abstrac class bisa berisi non abstractmethod
    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass


class PushButton(Button):
    def click(self):
        print(f'go to {self.link}')


tombol1 = PushButton('www.facebook.com')
tombol1.click()