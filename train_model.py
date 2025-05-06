import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Sample data for training (user stories and their severity labels)
user_stories = [
    "I feel tired all the time and my skin is dry.",
    "I have trouble concentrating and my weight is increasing.",
    "I get hot flashes and feel irritable."
]
severity_labels = [1, 2, 3]  # Severity labels: 1 = mild, 2 = moderate, 3 = severe

# Vectorize the user stories
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(user_stories)
y = severity_labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the model and vectorizer
with open('models/symptom_severity_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('models/count_vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model and vectorizer saved successfully!")
