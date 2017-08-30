# -*- coding: utf-8 -*-
from atf import *
from atf.ui import *
from pages import yandex


class TestYandexPage(TestCaseUI):

    def setup(self):
        self.browser.open('https://yandex.ru/')

    def test_yandex_search(self):
        """Проверка поиска сайта tensor.ru в сервисе Яндекс"""

        input_text = "Тензор"

        yandex_page = yandex.YandexPage(self)

        yandex_page.input_text(input_text)
        yandex_page.check_suggest()

    if __name__ == '__main__':
        run_tests()
