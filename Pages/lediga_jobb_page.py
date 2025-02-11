from Pages.base_page import BasePage

class LedigaJobbPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def filter_jobs_for_city(self, city):
        self.page.get_by_role("button", name="ort").click()
        self.page.locator("#Dropdown-1-options .chakra-text").get_by_text(city).click()