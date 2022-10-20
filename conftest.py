import pytest
from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright
from page_object.application import App
import settings
from page_object.challenging_dom import Dom
from page_object.context_menu import ContextMenu
import page_object.dropdown
from page_object.download_file import DownloadFile
from page_object.dynamic_control import DynamicControl
from page_object.dynamic_loading import DynamicLoading
from page_object.entry_ad import EntryAd
from page_object.floating_menu import FloatingMenu
from page_object.form_authentication import FormAuth
from page_object.geolocation import GeolocationTest
from page_object.iframe import IFrame
from page_object.popup_alerts import PopUpAlerts
from page_object.drug_drop import DrugDrop


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright



#
# @fixture
# def work_browser(get_playwright):
#     base_class = BaseClass(get_playwright, base_url=settings.BASE_URL)
#     yield base_class


@fixture
def desktop_app(get_playwright):
    app = App(get_playwright, base_url=settings.BASE_URL)
    yield app
    app.close()


@fixture
def desktop_app_auth(desktop_app):
    app = desktop_app
    app.goto('/login')
    app.login('alice', 'Qamania123')
    yield app


@fixture
def dom_page(get_playwright):
    dom = Dom(get_playwright, base_url=settings.BASE_URL)
    yield dom
    dom.close()


@fixture
def context_menu_page(get_playwright):
    context_menu = ContextMenu(get_playwright, base_url=settings.BASE_URL)
    yield context_menu
    context_menu.close()


@fixture
def popup_alerts(get_playwright):
    popup_alerts = PopUpAlerts(get_playwright, base_url=settings.BASE_URL)
    yield popup_alerts
    popup_alerts.close()


@fixture
def drug_drop(get_playwright):
    drug_drop = DrugDrop(get_playwright, base_url=settings.BASE_URL)
    yield drug_drop
    drug_drop.close()


@fixture
def dropdown(get_playwright):
    dropdown = page_object.dropdown.Dropdown(get_playwright, base_url=settings.BASE_URL)
    yield dropdown
    dropdown.close()


@fixture
def dynamic_control(get_playwright):
    dynamic_control = DynamicControl(get_playwright, base_url=settings.BASE_URL)
    yield dynamic_control
    dynamic_control.close()


@fixture
def dynamic_loading(get_playwright):
    dynamic_loading = DynamicLoading(get_playwright, base_url=settings.BASE_URL)
    yield dynamic_loading
    dynamic_loading.close()


@fixture
def entry_ad(get_playwright):
    entry_ad = EntryAd(get_playwright, base_url=settings.BASE_URL)
    yield entry_ad
    entry_ad.close()

@fixture
def download_file(get_playwright):
    download_file = DownloadFile(get_playwright, base_url=settings.BASE_URL)
    yield download_file
    download_file.close()

@fixture
def floating_menu(get_playwright):
    floating_menu = FloatingMenu(get_playwright, base_url=settings.BASE_URL)
    yield floating_menu
    floating_menu.close()

@fixture
def form_auth(get_playwright):
    form_auth = FormAuth(get_playwright, base_url=settings.BASE_URL)
    yield form_auth
    form_auth.close()

@fixture
def iframe(get_playwright):
    iframe = IFrame(get_playwright, base_url=settings.BASE_URL)
    yield iframe
    iframe.close()

@fixture
def iframe(get_playwright):
    geolocation = GeolocationTest(get_playwright, base_url=settings.BASE_URL)
    yield geolocation
    geolocation.close()


