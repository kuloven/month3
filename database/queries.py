class Queries:
    CREATE_REVIEW_TABLE = """
    CREATE TABLE IF NOT EXISTS review_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        instagram_username TEXT,
        visit_date INTEGER,
        food_rating TEXT,
        cleanliness_rating TEXT,
        extra_comments TEXT
    )
    """