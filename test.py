import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from post import post_articles


class TestPostArticles(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("https://jmty.jp/users/sign_in")
        self.browser.maximize_window()

    def test_post_articles(self):
        post_articles(self.browser)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
