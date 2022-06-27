
from appiumbase import BaseCase

from appium.webdriver.common.mobileby import MobileBy
import pytest
import logging


class Velvot(BaseCase):

    def test_create_account(self):
        
        self.click('com.velvot.android:id/onBoardingCreateBtn', MobileBy.ID)
        self.set_text('com.velvot.android:id/registrationFirstStepEmailTiEt','22', MobileBy.ID)
        self.set_text('com.velvot.android:id/registrationFirstStepPasswordTiEt', MobileBy.ID)
        
