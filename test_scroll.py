from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="storage_state.json", viewport={"width": 1280, "height": 720})
    page = context.new_page()
    page.goto("https://www.instagram.com/govbr/", wait_until="load")
    time.sleep(3)
    
    links = set()
    for _ in range(5):
        elements = page.locator("a[href*='/p/'], a[href*='/reel/']").all()
        for el in elements:
            try:
                href = el.get_attribute("href")
                if href: links.add(href)
            except: pass
            
        print(f"Found {len(links)} links")
        page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(2)
        
    browser.close()
