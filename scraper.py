from playwright.sync_api import sync_playwright

def scrape_reviews(url, review_selector):
    if not url.startswith("http"):
        print("Error: Invalid URL. Please provide a valid product page URL.")
        return []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run in visible mode for debugging
        page = browser.new_page()

        try:
            page.goto(url, timeout=60000)
            page.wait_for_load_state("networkidle")

            # Scroll down to load all reviews
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(3000)

            # Increase timeout & check different selectors
            page.wait_for_selector(review_selector, timeout=30000, state="attached")

            # Extract reviews
            reviews = page.locator(review_selector).all_inner_texts()

        except Exception as e:
            print(f"Error while scraping: {e}")
            reviews = []

        browser.close()
        return reviews

if __name__ == "__main__":
    product_url = "https://www.amazon.com/dp/B08N5WRWNW"
    review_css_selector = ".review-text-content span"  # Try different selectors

    extracted_reviews = scrape_reviews(product_url, review_css_selector)
    print("Extracted Reviews:", extracted_reviews)
