from api_client import fetch_posts
from data_parser import parse_posts

posts = fetch_posts()
df = parse_posts(posts)

print("Total posts:", len(df))
print(df[["id", "title"]].head(5))