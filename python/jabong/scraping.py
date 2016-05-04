from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

def correct_url(url): 
    if not url.startswith("http://") and not url.startswith("https://"):
      url = "http://" + url
    return url

def scrollDown(browser, numberOfScrollDowns):
    body = browser.find_element_by_tag_name("body")
    while numberOfScrollDowns >=0: 
        body.send_keys(Keys.PAGE_DOWN)
        numberOfScrollDowns -= 1
    return browser

def crawl_url(url, run_headless=True):
    if run_headless:
      display = Display(visible=0, size=(1024, 768))
      display.start()

    url = correct_url(url)
    browser = webdriver.Firefox()
    browser.get(url)
    browser = scrollDown(browser, 10)

    all_hover_elements = browser.find_elements_by_css_selector(".product-tile")

    for hover_element in all_hover_elements:
        product_title = hover_element.find_element_by_class_name("h4").text
        imgen = hover_element.find_element_by_tag_name("a")
        product_link = imgen.get_attribute("href")
        print product_title, product_link

    browser.quit()

if __name__=='__main__':
  url = "http://www.jabong.com/men/shoes/new-products/"
  crawl_url(url)
