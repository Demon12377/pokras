from playwright.sync_api import sync_playwright, expect

def test_server_starts():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000")
        expect(page).to_have_title("ЗАХВАТИ ЕВРОПУ")
        browser.close()
