from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="storage_state.json")
    page = context.new_page()
    page.goto("https://www.instagram.com/govbr/", wait_until="load")
    page.wait_for_timeout(3000)
    
    # Try different selectors
    res = page.evaluate("""
        () => {
            let links = Array.from(document.querySelectorAll('a')).filter(a => a.href.includes('/p/') || a.href.includes('/reel/'));
            if(links.length === 0) return { links: 0, sample_parent: null };
            let first = links[0];
            let parents = [];
            let curr = first.parentElement;
            while(curr && curr.tagName !== 'HTML' && parents.length < 5) {
                parents.push(curr.tagName + (curr.className ? '.' + curr.className.split(' ').join('.') : ''));
                curr = curr.parentElement;
            }
            return { links: links.length, sample_parent: parents };
        }
    """)
    print(res)
    browser.close()
