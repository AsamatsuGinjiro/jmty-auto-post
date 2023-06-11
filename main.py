from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from post import post_articles

# Chromeドライバーを起動
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://jmty.jp/users/sign_in")
browser.maximize_window()

# ログイン
email = "your_email@example.com"  # 実行時にメールアドレス入力
password = "your_password"  # 実行時にパスワード入力

email_elem = browser.find_element_by_id("user_email")
email_elem.send_keys(email)

pw_elem = browser.find_element_by_id("user_password")
pw_elem.send_keys(password)

submit_elem = browser.find_element_by_id("submit_button")
submit_elem.click()

time.sleep(3)

# 記事を投稿
post_articles(browser)

# ブラウザを終了
browser.quit()
