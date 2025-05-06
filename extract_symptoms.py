import re

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

def extract_thyroid_symptoms(user_story):
    """
    Extract thyroid-related symptoms from the user story using keyword matching.
    """
    user_story = user_story.lower()
    extracted_symptoms = [symptom for symptom in THYROID_SYMPTOMS if re.search(rf'\b{symptom}\b', user_story)]
    return list(set(extracted_symptoms))

# Example user stories
user_stories = [
    "I feel tired all the time and my skin is dry.",
    "I have trouble concentrating and my weight is increasing.",
    "I get hot flashes and feel irritable."
]

for idx, story in enumerate(user_stories, start=1):
    print(f"User Story {idx}: {story}")
    symptoms = extract_thyroid_symptoms(story)
    print(f"Extracted Symptoms: {symptoms}\n")
