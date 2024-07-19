class Queries:
    CREATE_REVIEW_TABLE = """
    CREATE TABLE IF NOT EXISTS review_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        instagram_username TEXT,
        visit_date INTEGER,
        food_rating INTEGER,
        cleanliness_rating INTEGER,
        extra_comments TEXT
    )
    """

    CREATE_CATEGORY_OF_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS category_dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """

    CREATE_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        category_of_dishes INTEGER,
        FOREIGN KEY (category_of_dishes) REFERENCES category_dishes(id)
    )
    """