from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.etsy.com/signin?from_page=%2Fyour%2Forders%2Fsold%2Fcompleted%3Fref%3Dseller-platform-mcnav&lp=0")
    page.get_by_label("Email address").click()
    page.get_by_label("Email address").fill("YOUR ETSY USER NAME")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("YOUR ETSY PASSWORD")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("combobox").first.select_option("50")
    # page.goto('https://www.etsy.com/your/orders/sold/completed?ref=seller-platform-mcnav&page=x')


    for j in range(0,100):
        page.wait_for_selector('.pr-md-0  .col-xs-12 .col-group .mr-xs-1 .active')
        value1 = page.query_selector('#browse-view > div > div.col-lg-9.pl-xs-0.pl-md-4.pr-xs-0.pr-md-4.pr-lg-0.float-left > div:nth-child(3) > div.wt-display-flex-xs.wt-justify-content-flex-end.wt-mb-xs-2 > div.wt-display-flex-xs.wt-align-items-center > div > select').input_value()   
        emails_d = page.query_selector_all('.dropdown-group .dropdown-body .list-unstyled') #? Add the e mails
        orderId_d = page.query_selector_all('.pr-md-0  .col-xs-12 .col-group .mr-xs-1 .active')#? Add the order id's
        emails_d = emails_d[2:]

        print(f"current page: {value1}")
            
        
        wr = open('./data.csv','a')
        for i in range(50):
            wr.write("\n" + emails_d[i].query_selector('li:last-child').inner_text()+ ";" + orderId_d[i].inner_text() )
        
        
 
        #! Go to the next page
        page.get_by_test_id("next-page").click()
        
    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
