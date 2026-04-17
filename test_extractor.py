import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="storage_state.json", viewport={"width": 1280, "height": 720})
    page = context.new_page()
    
    page.goto("https://www.instagram.com/govbr/p/DXJoAPekbE2/", wait_until="load")
    page.wait_for_timeout(3000)
    
    # Try different selectors to find where the main content is
    res = page.evaluate("""
        () => {
            let main = document.querySelector('main');
            if (!main) return { error: "No main found" };
            
            let imgs = Array.from(main.querySelectorAll('img[src*="instagram"]')).map(i => ({ alt: i.alt, src: i.src }));
            
            // Look for the caption
            let spans = Array.from(main.querySelectorAll('span')).map(s => s.innerText).filter(s => s && s.length > 50).slice(0, 2);
            
            let arias = Array.from(main.querySelectorAll('[aria-label]')).map(a => a.getAttribute('aria-label')).slice(0, 10);
            
            let vids = Array.from(main.querySelectorAll('video')).map(v => v.src);
            
            return {
                imgs_count: imgs.length,
                first_img: imgs[0] || null,
                captions: spans,
                arias,
                vids
            };
        }
    """)
    print(res)
    browser.close()
