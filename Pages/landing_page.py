from Pages.base_page import BasePage

class LandingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)


    def find_new_job(self):
        self.page.get_by_role("link", name="Hitta ditt nya jobb här").click()