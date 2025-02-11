from Pages.base_page import BasePage

class MenuPage(BasePage):
 def __init__(self, page):
    super().__init__(page)

 def click_on_menu(self):
    self.page.locator(".chakra-button .chakra-text").get_by_text("Meny").click()

 def click_on_kontakt(self):
    self.page.get_by_role("link", name="Kontakt").click()