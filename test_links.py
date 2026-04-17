from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="storage_state.json")
    page = context.new_page()
    page.goto("https://www.instagram.com/govbr/", wait_until="load")
    page.wait_for_timeout(3000)
    
    # Extract all links that contain /p/ or /reel/
    links = page.evaluate("""
        () => Array.from(document.querySelectorAll('a'))
                   .map(a => a.href)
                   .filter(h => h.includes('/p/') || h.includes('/reel/'))
                   .filter((v, i, a) => a.indexOf(v) === i)
    """)
    
    print("Found links:")
    for link in links:
        print(link)
    
    # Try the specific selector
    article_links = page.evaluate("""
        () => Array.from(document.querySelectorAll('article a'))
                   .map(a => a.href)
    """)
    print(f"\nLinks inside <article>: {len(article_links)}")
    
    browser.close()
