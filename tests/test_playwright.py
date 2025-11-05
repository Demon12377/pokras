from playwright.sync_api import sync_playwright, expect

def test_color_territory():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000")

        # Create a country in GR1
        page.fill('input[name="name"]', "Test Country")
        page.evaluate('document.querySelector(\'input[name="color"]\').value = "#FF0000"')
        page.fill('input[name="territory"]', "GR1")
        page.click('input[type="submit"]')

        # Wait for the map to be colored
        page.wait_for_timeout(1000)

        # Take a screenshot
        page.screenshot(path="screenshot.png")

        # Check the color of the GR1 territory
        path_element = page.locator("#GR1")
        expect(path_element).to_have_attribute("fill", "#FF0000")

        browser.close()
