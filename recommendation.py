from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity

def content_based_recommendations(user_history, data):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(data['tags'])
    user_videos = data[data['post_id'].isin(user_history)]
    user_profile = tfidf_matrix[user_videos.index].mean(axis=0)
    similarity_scores = cosine_similarity(user_profile, tfidf_matrix)
    data['similarity_score'] = similarity_scores.flatten()
    return data.nlargest(10, 'similarity_score')[['post_id', 'title']]
