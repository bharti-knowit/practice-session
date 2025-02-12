from Pages.base_page import BasePage

class KontaktPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://knowit.se/kontakt"

    def navigate(self):
        self.page.goto(self.url)

    def click_on_town(self, city):
        self.page.get_by_role("button", name=city).click()

    def does_address_exist(self, address):
        address_selector = self.page.get_by_role(role="heading", name=address)

        try:
           address_selector.wait_for(timeout=3000, state="visible")
           return True
        except:
            return False

    def does_location_exist(self, address):
        address_selector = self.page.get_by_role(role="heading", name=address)

        try:
            address_selector.wait_for(timeout=3000, state="visible")
            return True
        except:
            return False

