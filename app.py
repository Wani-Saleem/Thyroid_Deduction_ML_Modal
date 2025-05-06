from flask import Flask, request, render_template
import pickle
import re
import mysql.connector

# Load pre-trained model and vectorizer
with open('models/symptom_severity_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/count_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Flask app initialization
app = Flask(__name__)

# List of thyroid symptoms
THYROID_SYMPTOMS = [
    "fatigue", "tired", "weight gain", "weight loss", "hair loss", "dry skin",
    "cold intolerance", "heat intolerance", "constipation", "depression",
    "anxiety", "irritability", "palpitations", "muscle weakness", "hoarseness",
    "swelling", "goiter", "difficulty concentrating", "brain fog",
    "menstrual irregularities", "insomnia", "increased appetite",
    "decreased appetite", "thinning hair", "puffy face", "hot flashes",
    "tremors", "heart racing", "restlessness", "sleep issues", "forgetfulness"
]

# MySQL connection config (update with your actual DB credentials)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Saleem@123#',
    'database': 'patient_database'
}

def extract_thyroid_symptoms(user_story):
    user_story = user_story.lower()
    return list(set([s for s in THYROID_SYMPTOMS if re.search(rf'\b{s}\b', user_story)]))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        story = request.form.get('story')

        symptoms = extract_thyroid_symptoms(story)
        story_vector = vectorizer.transform([story])
        severity = model.predict(story_vector)[0]

        # Store in MySQL
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO patient_entries (name, age, gender, story, extracted_symptoms, severity)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, age, gender, story, ', '.join(symptoms), int(severity)))
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            return f"Database error: {err}"

        return render_template(
            'result.html',
            name=name,
            age=age,
            gender=gender,
            symptoms=symptoms,
            severity=severity
        )

    return render_template('form.html')

if __name__ == '__main__': 
    app.run(debug=True)
