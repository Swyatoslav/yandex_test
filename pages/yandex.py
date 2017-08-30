# -*- coding: utf-8 -*-
from atf import *
from atf.ui import *


class YandexPage(Page):
    """Начальная страница: https://yandex.ru"""
    field_inp = TextField(By.CSS_SELECTOR, '[name="text"] input', "Поле ввода")
    suggest_ccb = ControlsComboBox(By.CSS_SELECTOR, 'span [class="suggest2-item__text"]', "Подсказки")

    def input_text(self, text):
        self.field_inp.type_in(text)

    def check_suggest(self):
        delay(0.5)
        self.suggest_ccb.should_be(Displayed, wait_time=True)

