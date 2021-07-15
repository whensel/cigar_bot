# This is a sample Python script.

from time import sleep
from selenium import webdriver

driverPath = "/Users/macbook/Documents/webdrivers/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument('log-level=3')

options.headless = False
# set to on to run
driver = webdriver.Chrome(driverPath, options=options)

def get_current_price():
    #prints current price of item, saves lowest seen price

    run = True
    current_leader = 100000

    while run == True:
        price = driver.find_element_by_xpath('//*[@id="page-container"]/div/main/div/section/div[3]/div[1]/span[1]/span[2]/span').text

        if price == "Resetting…":
            print("Lowest Known Price: " + str(current_leader))
            sleep(0.5)
            print("Price resetting, please wait")
            sleep(10)
        else:
            price_fixed = float(price.replace("$", ""))

            if price_fixed < current_leader:
                current_leader = price_fixed

                print(current_leader)
            else:
                pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Cigar Bid Bot is Running")
    ### Chrome setup ###
    input = input("Freefall link: ")

    driver.get(input)

    sleep(4)

    # driver.find_element_by_xpath('//*[@id="onesignal-slidedown-cancel-button"]').click() #close pop up

    ### -------- ###

    get_current_price()

