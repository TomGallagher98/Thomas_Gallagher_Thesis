# Python program to scrape table from website

# import libraries selenium and time
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Create webdriver object
# driver = webdriver.Chrome(
# 	executable_path="C:/Users/Craig/Downloads/chromedriver_win32\chromedriver.exe")

# Get the website

def write_to_csv():
    pass

def scrape_data():
    for i in range(1,24):
        driver.get(
            f"https://www.footywire.com/afl/footy/supercoach_round?year=2012&round={i}&p=&s=T")

        # Make Python sleep for some time
        sleep(2)

        # Obtain the number of rows in body
        rows = 1+len(driver.find_elements("xpath",
            "//div[@id='supercoach-round-div']/table/tbody/tr"))

        # Obtain the number of columns in table
        cols = len(driver.find_elements("xpath",
            "//div[@id='supercoach-round-div']/table/tbody/tr[1]/td"))

        # Print rows and columns
        print(rows)
        print(cols)
        print(18*23*7)

        # Printing the table headers
        # print("Locators		 "+"			 Description")

        # Printing the data of the table
        for r in range(2, rows):
            for p in range(1, cols+1):
                
                # obtaining the text from each column of the table
                value = driver.find_element("xpath",
                    "//div[@id='supercoach-round-div']/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                print(value, end=',')
            print()
