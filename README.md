# 🛡️ CautionX V2: AI-Powered URL Threat Detection Platform

CautionX V2 is a full-stack cybersecurity application that detects malicious URLs using a hybrid approach combining Machine Learning, heuristic analysis, and VirusTotal threat intelligence. The platform provides real-time URL analysis, explainable risk assessment, and actionable security recommendations through a modern React frontend and Flask backend.

---

## 🚀 Features

* AI-powered malicious URL detection using a Random Forest classifier
* Trained on **650K+ real-world URLs**
* **95.7% classification accuracy**
* Feature engineering using:

  * URL entropy
  * Suspicious keywords
  * Top-Level Domain (TLD) analysis
  * Path depth
  * IP address detection
  * URL length and structural features
* VirusTotal API integration for threat intelligence
* Explainable risk scores and security recommendations
* RESTful Flask backend
* Responsive React frontend
* Dockerized backend for portable deployment

---

## 🏗️ Tech Stack

### Frontend

* React
* JavaScript
* HTML
* CSS

### Backend

* Flask
* Python
* REST API

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* Pandas
* NumPy

### DevOps

* Docker

### External API

* VirusTotal API

---

## 📂 Project Structure

```text
CautionX_V2/
│
├── frontend/                 # React Frontend
│
├── ml/
│   ├── app.py                # Flask Backend
│   ├── train.py              # Model Training
│   ├── feature_extraction.py
│   ├── virustotal_service.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── url_model.pkl
│
└── README.md
```

---

## 🧠 Machine Learning Pipeline

1. Collect URL dataset (650K+ samples)
2. Perform feature engineering
3. Train Random Forest classifier
4. Evaluate model performance
5. Save trained model
6. Serve predictions through Flask REST API
7. Enhance predictions using VirusTotal threat intelligence

---

## 📊 Model Performance

| Metric    |     Value |
| --------- | --------: |
| Accuracy  | **95.7%** |
| Precision | **95.4%** |
| Recall    | **91.4%** |
| F1 Score  | **93.4%** |

---

## ⚙️ Running the Project Locally

### Clone the repository

```bash
git clone https://github.com/PodaMounitha/CautionX_V2.git
```

### Backend

```bash
cd CautionX_V2/ml
```

Create a `.env` file:

```text
VT_API_KEY=YOUR_VIRUSTOTAL_API_KEY
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

The backend will be available at:

```
http://localhost:5000
```

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The React application will be available at:

```
http://localhost:5173
```

---

## 🐳 Running with Docker

Build the image:

```bash
docker build -t cautionx-backend .
```

Run the container:

```bash
docker run -p 5000:5000 --env-file .env cautionx-backend
```

---

## 🔍 API Endpoint

### Analyze URL

**POST**

```
/predict
```

Example request:

```json
{
  "url": "google.com"
}
```

Example response:

```json
{
  "prediction": "Safe",
  "risk_level": "LOW",
  "risk_score": 15,
  "confidence": 99.6
}
```

---

## 🔐 Security Features

* Machine Learning-based URL classification
* Heuristic URL analysis
* VirusTotal threat intelligence integration
* Explainable risk assessment
* Runtime environment variable management for API keys
* Dockerized backend deployment

---

## 📌 Future Improvements

* Browser extension integration
* User authentication
* URL scan history
* Threat analytics dashboard
* Cloud deployment
* Continuous model retraining

---

## 👨‍💻 Author

**Poda Mounitha**

If you found this project useful, feel free to ⭐ the repository.
