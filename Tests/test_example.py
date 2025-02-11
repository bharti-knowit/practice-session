import re
from playwright.sync_api import Page, expect

from Pages.base_page import BasePage
from Pages.landing_page import LandingPage
from Pages.lediga_jobb_page import LedigaJobbPage
from Pages.menu_page import MenuPage
from Pages.kontakt_page import KontaktPage

def test_has_title(page: Page):
    page.goto("https://knowit.se/")
    expect(page).to_have_title(re.compile("Knowit"))


def test_get_om_oss_link(page: Page):
    page.goto("https://knowit.se/")
    page.locator("[aria-label='Godkänn alla']").click()
    page.get_by_role("link", name="Om oss").click()
    expect(page).to_have_title(re.compile("It-konsultföretag som levererar digitala lösningar | Knowit"))


def test_hitta_ditt_nya_jobb(page: Page):
    page.goto("https://knowit.se/")
    page.locator("[aria-label='Godkänn alla']").click()
    page.wait_for_timeout(2000)
    page.locator("[title='Hitta ditt nya jobb här']").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="ort").click()
    page.locator("#Dropdown-1-options .chakra-text").get_by_text("Lund").click()
    assert page.url.endswith("/karriar/lediga-jobb/?Ort=Lund")


def test_hitta_ditt_nya_jobb_POM(page: Page):
    # Find the job using POM structure
    landing_page = LandingPage(page)
    lediga_page = LedigaJobbPage(page)
    landing_page.navigate()
    landing_page.dismiss_cookies()
    landing_page.find_new_job()
    lediga_page.filter_jobs_for_city("Lund")
    assert page.url.endswith("Lund")


def test_does_address_exist(page: Page):
    # Visit kontakt page and click on city Lund and verify it has correct title
    base_page = BasePage(page)
    menu_page = MenuPage(page)
    kontakt_page = KontaktPage(page)
    base_page.navigate_to()

    base_page.dismiss_cookies()
    menu_page.click_on_menu()
    menu_page.click_on_kontakt()
    kontakt_page.click_on_town("Lund")
    assert kontakt_page.does_address_exist("Mobilvägen 10")
