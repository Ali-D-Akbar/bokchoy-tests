import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestPolls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )

    def test_index_page(self):
        self.driver.get('http://demo.app:8000/polls/')
        assert "Index" in self.driver.title

        question = self.driver.find_element_by_css_selector('#question1 a')
        question.click()

        assert "Detail" == self.driver.title

    def test_detail_page(self):
        self.driver.get('http://demo.app:8000/polls/1')
        assert "Detail" in self.driver.title

        vote_button = self.driver.find_element_by_css_selector('#vote')
        vote_button.click()

        assert "You didn't select a choice." in self.driver.find_element_by_css_selector('#error strong').text

        self.driver.find_element_by_css_selector('#choice1').click()
        vote_button = self.driver.find_element_by_css_selector('#vote')
        vote_button.click()

        assert "Results" == self.driver.title

    def test_results_page(self):
        self.driver.get('http://demo.app:8000/polls/1/results')
        assert "Results" in self.driver.title

        vote_again = self.driver.find_element_by_css_selector('#vote_again')

        vote_again.click()

        assert "Detail" == self.driver.title

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
