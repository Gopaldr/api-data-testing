from data_parser import parse_posts

def test_parse_posts():
    posts = [
        {"userId": 1, "id": 1, "title": "Test", "body": "Sample"}
    ]

    df = parse_posts(posts)

    assert len(df) == 1
    assert list(df.columns) == ["userId", "id", "title", "body"]
    assert df.iloc[0]["title"] == "Test"