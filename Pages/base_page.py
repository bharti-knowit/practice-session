from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://knowit.se/"

    @property
    @abstract
    def url_segment(self):
        raise NotImplementedError("Child class must implement")
        return ""

    def navigate_to(self):
     url= self.base_url + self.url_segment
     self.page.goto(url)

    def dismiss_cookies(self):
     self.page.locator("[aria-label='Godkänn alla']").click()