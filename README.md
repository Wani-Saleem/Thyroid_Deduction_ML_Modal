# Thyroid Symptom Tracker

The **Thyroid Symptom Tracker** is a Flask-based web application designed to collect patient health stories, extract thyroid-related symptoms using Natural Language Processing (NLP), predict the severity of symptoms using a machine learning model, and store the data in a MySQL database. The application aims to assist healthcare professionals and patients in tracking symptoms and providing insights into thyroid-related health conditions.

## ✅ Features
- **Collects Optional Fields:** name, age, gender
- **Symptom Extraction:** Uses NLP to extract thyroid-related symptoms from user-submitted health stories.
- **Symptom Severity Prediction:** Predicts the severity of symptoms using a pre-trained machine learning model.
- **Database Storage:** Stores collected data in a MySQL database for future reference and analysis.

## ⚙️ Prerequisites
Before you begin, make sure you have the following installed on your system:
- **Python 3.x**
- **pip** (Python package installer)
- **MySQL Server** (for database setup)

## 📁 Folder Structure

```
project/
│
├── app.py                      # Main Flask application file
├── requirements.txt            # List of Python dependencies
├── models/                     # Folder containing machine learning models
│   ├── count_vectorizer.pkl    # Pre-trained vectorizer model
│   └── symptom_severity_model.pkl  # Pre-trained severity prediction model
├── templates/                  # HTML templates for the web application
│   ├── form.html               # HTML form to collect user data
│   └── result.html             # HTML page to display the results
```

## 📦 Install Requirements
To set up the environment and install the necessary dependencies, follow these steps:

1. Clone or download the project repository to your local machine.
2. Navigate to the project directory:
   ```bash
   cd project
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Setup MySQL
The application stores data in a MySQL database. Follow the steps below to set it up:

### 1. Login to MySQL:
```bash
mysql -u root -p
```

### 2. Create the database:
```sql
CREATE DATABASE patient_database;
USE patient_database;
```

### 3. Create the `patient_entries` table:
```sql
CREATE TABLE patient_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    story TEXT,
    extracted_symptoms TEXT,
    severity INT
);
```

## 🧠 Update app.py MySQL Connection
In your `app.py` file, update the MySQL connection settings. Locate this block of code:

```python
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)
```

And replace it with:

```python
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # or your MySQL username
    password='your_password',  # use your actual password
    database='patient_database'
)
```

## 🚀 Run the App
Once everything is set up, you're ready to run the application!

1. Start the Flask application by running:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to the following URL:
   ```
   http://127.0.0.1:5000
   ```

The web interface will allow users to enter their health stories, extract thyroid symptoms, and get the severity prediction.

## 📌 Notes
- **Symptom Extraction:** The system uses basic keyword matching for symptom extraction. It identifies thyroid-related symptoms from user-submitted stories.
- **Severity Prediction:** The symptom severity is predicted using a pre-trained machine learning model (`symptom_severity_model.pkl`), which has been trained on labeled data.
- **Data Storage:** The collected data (name, age, gender, health story, extracted symptoms, and severity) is saved in the `patient_entries` table within the `patient_database` MySQL database.
- **Optional Fields:** The application collects optional fields like name, age, and gender to better contextualize the user's health story.

## 🧑‍💻 Development and Contributions
If you'd like to contribute to the development of this project or suggest improvements, feel free to fork the repository and submit pull requests. Contributions are always welcome!

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍⚕️ Disclaimer
The Thyroid Symptom Tracker is intended for informational purposes only. It is not a replacement for medical advice, diagnosis, or treatment. Always consult with a healthcare professional for medical concerns.
