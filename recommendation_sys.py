import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data
data = {
    'UserID': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'Product': ['Product A', 'Product B', 'Product C',
                'Product A', 'Product B', 'Product D',
                'Product C', 'Product D', 'Product E'],
    'Rating': [4, 5, 2, 5, 3, 4, 4, 5, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create user-product matrix
pivot_table = df.pivot_table(index='UserID', columns='Product', values='Rating').fillna(0)

# Compute user similarity
user_similarity = cosine_similarity(pivot_table)
user_similarity_df = pd.DataFrame(user_similarity, index=pivot_table.index, columns=pivot_table.index)

# Recommendation function
def recommend_products(user_id, pivot_table, user_similarity_df, n_recommendations=2):
    if user_id not in pivot_table.index:
        return None
    user_ratings = pivot_table.loc[user_id]
    similarity_scores = user_similarity_df.loc[user_id]
    weighted_ratings = pivot_table.T.dot(similarity_scores) / similarity_scores.sum()
    unrated = user_ratings[user_ratings == 0].index
    recommendations = weighted_ratings[unrated].nlargest(n_recommendations)
    return recommendations

# --- MAIN SCRIPT ---

try:
    user_input = int(input("Enter your User ID (e.g., 1, 2, 3): "))
    recommendations = recommend_products(user_input, pivot_table, user_similarity_df)

    if recommendations is not None and not recommendations.empty:
        print(f"\nRecommended Products for User {user_input}:")
        print(recommendations)
    elif recommendations is not None:
        print("No new products to recommend. You've rated all available products.")
    else:
        print("User ID not found.")
except ValueError:
    print("Invalid input. Please enter a numeric User ID.")
