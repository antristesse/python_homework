# Task 6: Import required libraries

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

url = "https://top10.owasp.org/2025/"

results = []

try:
    # Load the OWASP page

    driver.get(url)


    # Find the Top 10 heading

    top_10_heading = driver.find_element(
        By.CSS_SELECTOR,
        '[id="top-102025-list"]'
    )


    # Use XPath to find the ordered list after the heading

    top_10_list = top_10_heading.find_element(
        By.XPATH,
        "following-sibling::ol[1]"
    )


    # Find every vulnerability link in the ordered list

    vulnerability_links = top_10_list.find_elements(
        By.CSS_SELECTOR,
        "a"
    )


    # Store each title and link in a dictionary

    for vulnerability in vulnerability_links:
        title = vulnerability.text.strip()
        link = vulnerability.get_attribute("href")

        vulnerability_data = {
            "Title": title,
            "Link": link
        }

        results.append(vulnerability_data)


    # Print the list

    print(results)


    # Create a DataFrame and save it as CSV

    owasp_df = pd.DataFrame(results)

    print(owasp_df)

    owasp_df.to_csv(
        "owasp_top_10.csv",
        index=False
    )

    print("Created owasp_top_10.csv")


finally:
    driver.quit()