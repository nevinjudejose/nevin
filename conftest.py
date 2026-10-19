
import os
import pytest
from config import BROWSER, HEADLESS, TIMEOUT, NAVIGATION_TIMEOUT
from dotenv import load_dotenv
load_dotenv()


# Task 2
@pytest.fixture
def custom_context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def custom_page(custom_context):
    page = custom_context.new_page()
    yield page
    page.close()


# Task 4
@pytest.fixture
def configured_page(playwright):
    browser_type = getattr(playwright, BROWSER)
    browser = browser_type.launch(headless=HEADLESS)

    page = browser.new_page()
    page.set_default_timeout(TIMEOUT)
    page.set_default_navigation_timeout(NAVIGATION_TIMEOUT)

    yield page
    browser.close()

# Task 5 - Async Playwright fixture
import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture
async def async_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        yield page
        await browser.close()


# Task 18
@pytest.fixture
def app_url():
    return os.getenv("BASE_URL", "https://www.saucedemo.com/")


@pytest.fixture
def setup_page(page):
    page.set_default_timeout(5000)
    page.set_default_navigation_timeout(10000)
    return page


@pytest.fixture
def credentials():
    return (
        os.getenv("USERNAME"),
        os.getenv("PASSWORD")
    )
