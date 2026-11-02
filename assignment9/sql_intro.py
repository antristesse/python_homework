import sqlite3


# Task 3: Add a publisher without duplication
def add_publisher(cursor, name):
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO publishers (name) VALUES (?)",
            (name,)
        )

        cursor.execute(
            "SELECT publisher_id FROM publishers WHERE name = ?",
            (name,)
        )

        return cursor.fetchone()[0]

    except sqlite3.Error as error:
        print("Error adding publisher:", error)
        return None


# Task 3: Add a magazine without duplication
def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute(
            """
            INSERT OR IGNORE INTO magazines (name, publisher_id)
            VALUES (?, ?)
            """,
            (name, publisher_id)
        )

        cursor.execute(
            "SELECT magazine_id FROM magazines WHERE name = ?",
            (name,)
        )

        return cursor.fetchone()[0]

    except sqlite3.Error as error:
        print("Error adding magazine:", error)
        return None


# Task 3: Add a subscriber without duplicating name and address
def add_subscriber(cursor, name, address):
    try:
        cursor.execute(
            """
            SELECT subscriber_id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        )

        existing_subscriber = cursor.fetchone()

        if existing_subscriber:
            return existing_subscriber[0]

        cursor.execute(
            """
            INSERT INTO subscribers (name, address)
            VALUES (?, ?)
            """,
            (name, address)
        )

        return cursor.lastrowid

    except sqlite3.Error as error:
        print("Error adding subscriber:", error)
        return None


# Task 3: Add a subscription without duplication
def add_subscription(
    cursor,
    subscriber_id,
    magazine_id,
    expiration_date
):
    try:
        cursor.execute(
            """
            INSERT OR IGNORE INTO subscriptions
            (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
            """,
            (subscriber_id, magazine_id, expiration_date)
        )

    except sqlite3.Error as error:
        print("Error adding subscription:", error)


conn = None

try:
    # Task 1: Connect to the database
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Task 2: Create publishers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
        """)

        # Task 2: Create magazines table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id)
                    REFERENCES publishers (publisher_id)
            )
        """)

        # Task 2: Create subscribers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)

        # Task 2: Create subscriptions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id)
                    REFERENCES subscribers (subscriber_id),
                FOREIGN KEY (magazine_id)
                    REFERENCES magazines (magazine_id),
                UNIQUE (subscriber_id, magazine_id)
            )
        """)

        # Task 3: Add publishers
        conde_id = add_publisher(cursor, "Conde Nast")
        hearst_id = add_publisher(cursor, "Hearst")
        time_id = add_publisher(cursor, "Time USA")

        # Task 3: Add magazines
        vogue_id = add_magazine(
            cursor,
            "Vogue",
            conde_id
        )

        cosmopolitan_id = add_magazine(
            cursor,
            "Cosmopolitan",
            hearst_id
        )

        time_magazine_id = add_magazine(
            cursor,
            "Time",
            time_id
        )

        # Task 3: Add subscribers
        ana_id = add_subscriber(
            cursor,
            "Ana Gmyrina",
            "Brooklyn, NY"
        )

        joe_id = add_subscriber(
            cursor,
            "Joe Atkachunas",
            "New York, NY"
        )

        christine_id = add_subscriber(
            cursor,
            "Christine Lee",
            "Queens, NY"
        )

        # Task 3: Add subscriptions
        add_subscription(
            cursor,
            ana_id,
            vogue_id,
            "2027-12-31"
        )

        add_subscription(
            cursor,
            joe_id,
            time_magazine_id,
            "2027-10-31"
        )

        add_subscription(
            cursor,
            christine_id,
            cosmopolitan_id,
            "2027-08-31"
        )

        conn.commit()
        print("Database populated successfully.")

        # Task 4.1: Retrieve all subscribers
        try:
            cursor.execute("SELECT * FROM subscribers")
            subscriber_rows = cursor.fetchall()

            print("\nAll subscribers:")

            for row in subscriber_rows:
                print(row)

        except sqlite3.Error as error:
            print("Error retrieving subscribers:", error)

        # Task 4.2: Retrieve magazines sorted by name
        try:
            cursor.execute("""
                SELECT *
                FROM magazines
                ORDER BY name
            """)

            magazine_rows = cursor.fetchall()

            print("\nMagazines sorted by name:")

            for row in magazine_rows:
                print(row)

        except sqlite3.Error as error:
            print("Error retrieving magazines:", error)

        # Task 4.3: Find magazines for one publisher
        try:
            cursor.execute("""
                SELECT magazines.name, publishers.name
                FROM magazines
                JOIN publishers
                    ON magazines.publisher_id =
                       publishers.publisher_id
                WHERE publishers.name = ?
            """, ("Conde Nast",))

            publisher_rows = cursor.fetchall()

            print("\nMagazines published by Conde Nast:")

            for row in publisher_rows:
                print(row)

        except sqlite3.Error as error:
            print("Error retrieving publisher magazines:", error)

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if conn is not None:
        conn.close()
        print("\nDatabase connection closed.")