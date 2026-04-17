import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="storage_state.json", viewport={"width": 1280, "height": 720}, locale="pt-BR")
    page = context.new_page()
    
    # We will pick a few posts from the discovery process we observed earlier
    test_urls = [
        "https://www.instagram.com/govbr/p/DXJoAPekbE2/",
        "https://www.instagram.com/govbr/p/DXOyIshkecI/",
        "https://www.instagram.com/govbr/p/DXNSuN4FETV/",
        "https://www.instagram.com/govbr/p/DXMJNR0EYdB/"
    ]
    
    results = []
    
    for url in test_urls:
        print(f"Investigating: {url}")
        page.goto(url, wait_until="load")
        page.wait_for_timeout(3000)
        
        data = page.evaluate("""
            () => {
                let main = document.querySelector('main');
                if(!main) return null;
                
                let imgs = Array.from(main.querySelectorAll('img[src*="instagram"]')).map(i => i.alt).filter(a => a && !a.includes('profile picture'));
                let captionSpan = main.querySelector('span[dir="auto"]');
                let captionText = captionSpan ? captionSpan.innerText : '';
                
                return {
                    img_alts: imgs.slice(0, 3), // return first 3 valid alts
                    caption_preview: captionText.substring(0, 150) + '...'
                };
            }
        """)
        
        results.append({
            "url": url,
            "data": data
        })
        
    for res in results:
        print(f"\n--- URL: {res['url']} ---")
        if res['data']:
            print("Captions:", res['data']['caption_preview'])
            for idx, alt in enumerate(res['data']['img_alts']):
                print(f"ALT {idx}: {alt}")
        else:
            print("No data extracted.")
            
    browser.close()
