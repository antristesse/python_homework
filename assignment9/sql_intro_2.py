import sqlite3
import pandas as pd

conn = None

try:
    # Task 5: Connect to the lesson database
    conn = sqlite3.connect("../db/lesson.db")

    # Join line_items and products
    query = """
        SELECT
            line_items.line_item_id,
            line_items.quantity,
            line_items.product_id,
            products.product_name,
            products.price
        FROM line_items
        JOIN products
            ON line_items.product_id = products.product_id
    """

    # Read the query results into a DataFrame
    df = pd.read_sql_query(query, conn)

    print("First five rows:")
    print(df.head())

    # Calculate the total price for each line item
    df["total"] = df["quantity"] * df["price"]

    print("\nFirst five rows with total:")
    print(df.head())

    # Group the data by product
    summary_df = (
        df.groupby("product_id")
        .agg({
            "line_item_id": "count",
            "total": "sum",
            "product_name": "first"
        })
        .reset_index()
    )

    print("\nFirst five rows of the summary:")
    print(summary_df.head())

    # Sort by product name
    summary_df = summary_df.sort_values("product_name")

    # Write the summary to a CSV file
    summary_df.to_csv("order_summary.csv", index=False)

    print("\nCreated order_summary.csv successfully.")

except sqlite3.Error as error:
    print("Database error:", error)

except Exception as error:
    print("Error:", error)

finally:
    if conn is not None:
        conn.close()
        print("Database connection closed.")