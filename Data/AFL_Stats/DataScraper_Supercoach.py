# Python program to scrape table from website

# import libraries selenium and time
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


PATH = 'C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/'
driver = webdriver.Chrome(ChromeDriverManager().install())

# Create webdriver object
# driver = webdriver.Chrome(
# 	executable_path="C:/Users/Craig/Downloads/chromedriver_win32\chromedriver.exe")

# Get the website
s = time.time
print(s)
def write_to_csv():
    pass

def scrape_data(year):
    for i in range(1,24):
        driver.get(
            f"https://www.footywire.com/afl/footy/supercoach_round?year={year}&round={i}&p=&s=T")

        # Make Python sleep for some time
        time.sleep(2)

        # Obtain the number of rows in body
        rows = 1+len(driver.find_elements("xpath",
            "//div[@id='supercoach-round-div']/table/tbody/tr"))

        # Obtain the number of columns in table
        cols = len(driver.find_elements("xpath",
            "//div[@id='supercoach-round-div']/table/tbody/tr[1]/td"))

        # Print rows and columns
    
        # Printing the table headers
        # print("Locators		 "+"			 Description")

        
        
   
        header = 'round,player,team,score'
        fields = header.split(',')

        
        file_output = open(PATH+'Year/Games/supercoach_round'+str(i)+'_'+str(year)+'.csv', 'w')
        file_output.writelines(header+'\n')

        

        # Printing the data of the table
        for r in range(2, rows):
            # obtaining the text from each column of the table
            
            player = driver.find_element("xpath",
                "//div[@id='supercoach-round-div']/table/tbody/tr["+str(r)+"]/td[1]").text
            team = driver.find_element("xpath",
                "//div[@id='supercoach-round-div']/table/tbody/tr["+str(r)+"]/td[2]").text
            score = driver.find_element("xpath",
                "//div[@id='supercoach-round-div']/table/tbody/tr["+str(r)+"]/td[6]").text
           
            out = ','.join([str(i),player,team,score])
            file_output.writelines(out+'\n')
        file_output.close()
    
scrape_data(2013)   
        
