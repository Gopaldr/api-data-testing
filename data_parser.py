
import pandas as pd

def parse_posts(posts):
    df = pd.DataFrame(posts)
    return df[["userId", "id", "title", "body"]]
