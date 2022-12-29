from robot.api.deco import keyword
import Browser
from Browser.utils.data_types import SupportedBrowsers
from robot.api import logger

from resources.locators import RpaChallenge

from libraries.LibraryBase import LibraryBase
from libraries.utils import (
    debug,
    get_variable,
)


class RpaChallengeLibrary(LibraryBase):
    """
    Template for implementing a robot library.
    """

    def __init__(self):
        super().__init__()
        self.env = get_variable("${ENV}")
        self.browser = Browser.Browser()
        self.rpa_challenge_url = get_variable("${rpa_challenge_url}")
        self.downloads_path = get_variable("${download_path}")
        self.download_url = get_variable("${download_url}")

    @keyword
    def debug_library(self):
        logger.info(f"{self.__class__}")
        debug()

    @keyword
    def download_rpa_excel(self):
        self.browser.download(self.download_url)


    @keyword
    def go_to_rpa_challenge(self):
        self.browser.new_browser(
            SupportedBrowsers.chromium,
            headless= True,
            downloadsPath=self.downloads_path,
            )
        self.browser.new_context()
        self.browser.new_page(self.rpa_challenge_url)

    @keyword
    def start_challenge(self):
        self.browser.click(RpaChallenge.start_button)

    @keyword
    def insert_company_name(self, company_name):
        self.browser.fill_text(RpaChallenge.company_name, company_name)

    @keyword
    def insert_first_name(self, first_name):
        self.browser.fill_text(RpaChallenge.first_name, first_name)

    @keyword
    def insert_last_name(self, last_name):
        self.browser.fill_text(RpaChallenge.last_name, last_name)

    @keyword
    def insert_role_in_company(self, role_in_company):
        self.browser.fill_text(RpaChallenge.role_in_company, role_in_company)

    @keyword
    def insert_address(self, address):
        self.browser.fill_text(RpaChallenge.address, address)

    @keyword
    def insert_email(self, email):
        self.browser.fill_text(RpaChallenge.email, email)

    @keyword
    def insert_phone_number(self, phone_number):
        self.browser.fill_text(RpaChallenge.phone_number, str(phone_number))

    @keyword
    def click_submit(self):
        self.browser.click(RpaChallenge.submit_button)

    @keyword
    def log_text(self):
        logger.warn(f"{self.browser.get_text(RpaChallenge.result_text)}")

    @keyword
    def close_rpa_challenge(self):
        self.browser.close_browser()


