import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestIno():

    def setup_class(self):
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize('site', ["895", "896", "897", "898", "899", "903", "904", "905"])
    def test_ino(self, site):
        self.driver.get(f"https://stepik.org/lesson/236{site}/step/1")
        answer = math.log(int(time.time()))
        answer_str = str(answer)
        answer_field = WebDriverWait(self.driver, 15)\
            .until(EC.visibility_of_element_located((By.CLASS_NAME, "string-quiz__textarea")))
        answer_field.send_keys(answer_str)

        self.driver.find_element_by_class_name('submit-submission').click()

        feadback = WebDriverWait(self.driver, 10)\
            .until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__feedback')))
        feadback_text = feadback.text
        assert feadback_text == "Correct!", "Ответ неверный"




