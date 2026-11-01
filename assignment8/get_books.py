# Task 3: Import required libraries

# Task 3: Import required libraries

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import json

url = (
    "https://durhamcounty.bibliocommons.com/v2/search"
    "?query=learning%20spanish&searchType=smart"
)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get(url)

    # Allow the dynamic webpage time to load
    sleep(3)

    # Find all li search-result elements

    book_entries = driver.find_elements(
        By.CSS_SELECTOR,
        "li.row.cp-search-result-item"
    )

    print(f"Number of search results found: {len(book_entries)}")


    # Create an empty results list

    results = []


    # Extract information from every search result

    for book in book_entries:

        # Find the book title
        title_element = book.find_element(
            By.CSS_SELECTOR,
            "span.title-content"
        )

        title = title_element.text.strip()


        # Find all authors
        author_elements = book.find_elements(
            By.CSS_SELECTOR,
            "a.author-link"
        )

        author_names = []

        for author_element in author_elements:
            author_name = author_element.text.strip()

            if author_name:
                author_names.append(author_name)

        authors = "; ".join(author_names)


        # Find the format and publication year container
        format_container = book.find_element(
            By.CSS_SELECTOR,
            "div.cp-format-info"
        )

        # Find the format and year inside the container
        format_year_element = format_container.find_element(
            By.CSS_SELECTOR,
            "span.display-info-primary"
        )

        format_year = format_year_element.text.strip()


        # Store the extracted information in a dictionary
        book_data = {
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        }

        results.append(book_data)


    # Task 3: Create and print the DataFrame

    books_df = pd.DataFrame(results)

    print(books_df)
# Task 4: Write the DataFrame to a CSV file

    books_df.to_csv("get_books.csv", index=False)
    print("Created get_books.csv")


    # Write the results list to a JSON file

    with open("get_books.json", "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=4, ensure_ascii=False)

    print("Created get_books.json")

finally:
    # Close the browser even if an error occurs

    driver.quit()