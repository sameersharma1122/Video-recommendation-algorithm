import pandas as pd

def preprocess_data(viewed_posts, liked_posts, inspired_posts):
    # Convert to DataFrame
    viewed_df = pd.DataFrame(viewed_posts)
    liked_df = pd.DataFrame(liked_posts)
    inspired_df = pd.DataFrame(inspired_posts)

    # Combine DataFrames
    all_data = pd.concat([viewed_df, liked_df, inspired_df], ignore_index=True)

    
    all_data.fillna({"rating": 0, "views": 0, "likes": 0}, inplace=True)

    
    all_data['engagement_score'] = all_data['likes'] + all_data['views'] * 0.5
    return all_data
