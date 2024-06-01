# tests/test_example.py
import unittest
from selenium import webdriver

class TestExample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        self.driver.get("http://example.com")
        self.assertEqual(self.driver.title, "Example Domain")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
