from playwright.sync_api import sync_playwright, expect

def test_color_territory():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000")

        # Wait for the map to load
        page.wait_for_selector("#map-container svg")

        # Fill the form
        page.fill('input[name="territory"]', "path7")
        page.evaluate('document.querySelector(\'input[name="color"]\').value = "#0000FF"')
        page.click('button[type="submit"]')

        # Wait for the map to be colored
        page.wait_for_timeout(1000)

        # Take a screenshot
        page.screenshot(path="screenshot.png")

        # Check the color of the path7 territory
        path_element = page.locator("#path7")
        expect(path_element).to_have_attribute("fill", "#0000ff")

        browser.close()
