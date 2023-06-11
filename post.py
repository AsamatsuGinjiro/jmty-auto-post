import time
from selenium.webdriver.support.select import Select
from utils import randomname


def post_articles(browser):
    """
    記事を投稿する関数
    """
    post_area = [("北海道", "札幌市", "函館市"), ("青森県", "青森市", "弘前市"),
                 ("岩手県", "盛岡市", "宮古市")]
    post_category = "地元のお店"
    post_subcategory = "その他"

    count = 10
    for i in post_area:
        if i == ('北海道', '札幌市', '函館市') and count == 10:
            # 投稿ページに遷移
            post_elem = browser.find_element_by_link_text("投稿画面へ(無料)")
            post_elem.click()
            firstLoop = False
            time.sleep(1)

        else:
            # 投稿ページに遷移（2回目以降は続けて投稿の表示が出るため）
            post_elem = browser.find_element_by_link_text("続けて投稿")
            post_elem.click()
            time.sleep(1)

        # カテゴリの選択
        dropdown = browser.find_element_by_id('category_group_id')
        select = Select(dropdown)
        select.select_by_visible_text(post_category)

        dropdown = browser.find_element_by_id('article_category_id')
        select = Select(dropdown)
        select.select_by_visible_text(post_subcategory)

        # 都道府県の入力
        # 地域1
        dropdown = browser.find_element_by_id('article_prefecture_id')
        select = Select(dropdown)
        select.select_by_visible_text(i[0])
        time.sleep(1)
        dropdown = browser.find_element_by_id('article_city_id')
        select = Select(dropdown)
        select.select_by_visible_text(i[1])

        # 地域2
        dropdown = browser.find_element_by_id('location2_prefecture_id')
        select = Select(dropdown)
        select.select_by_visible_text(i[0])
        time.sleep(1)
        dropdown = browser.find_element_by_id('location2_city_id')
        select = Select(dropdown)
        select.select_by_visible_text(i[2])

        # 投稿タイトルの入力
        post_id = randomname(10)
        input_str = browser.find_element_by_id('article_title')
        input_str.send_keys(
            # 調査に引っかかるの防止でランダム英数字をタイトルに記入
            "ID:"+post_id+"【" + i[0] + "タイトル")
        # 投稿内容の入力
        input_str = browser.find_element_by_id('article_text')
        # 改行注意　本文
        input_str.send_keys("投稿本文を記載")
        # 会社・店舗名称の入力
        input_str = browser.find_element_by_id('article_name')
        input_str.send_keys("店名を記載")

        # 投稿
        post_elem = browser.find_element_by_id('article_submit_button')
        post_elem.click()
    count -= count
    time.sleep(600)
