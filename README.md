# 🏦 Face Recognition KYC Verification System

🚀 A deep learning–powered KYC verification system that compares an ID card photo with a live selfie to authenticate user identity.

---

## ✨ Project Highlights

This project simulates a real-world banking/fintech onboarding workflow using face recognition technology. Users upload an ID card image and capture a selfie through their device camera. The system verifies whether both images belong to the same person using a deep learning face recognition model.

The app provides instant verification results along with similarity confidence metrics in a clean and interactive interface.

---

## 🎯 Features

- ✔️ Upload ID card image  
- ✔️ Capture selfie using device camera  
- ✔️ Deep learning face verification (ArcFace)  
- ✔️ Similarity distance & threshold metrics  
- ✔️ Real-time verification result  
- ✔️ Error handling for invalid inputs  
- ✔️ User-friendly Streamlit interface  

---

## 🧠 Tech Stack

| Category | Technologies |
|----------|-------------|
| Language | Python |
| Framework | Streamlit |
| AI Model | DeepFace (ArcFace) |
| Computer Vision | CNN |
| Libraries | NumPy, OS |

---

## 📂 Project Structure
face-kyc-verification/
│── app.py # Streamlit application
│── verifier.py # Face verification logic
│── requirements.txt # Dependencies
│── temp/ # Temporary image storage
│── README.md


---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/Muralidharan-ramachandran/KYC_Verification.git

# Navigate to folder
cd KYC_Verification

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

# ▶️ Run Application
streamlit run app.py

## 📸 Demo

Add screenshots or GIF here:

![Demo](demo.png)

---

## 🔬 How It Works

1️⃣ User uploads ID card image  
2️⃣ User captures live selfie via camera  
3️⃣ Images are temporarily stored  
4️⃣ Deep learning model compares facial features  
5️⃣ System returns verification result with confidence score  

---

## 🌍 Real-World Use Cases

- Banking & FinTech eKYC  
- Digital Identity Verification  
- Secure User Onboarding  
- Fraud Detection Systems  
- Remote Authentication  

---

## 🔮 Future Enhancements

- ⭐ Liveness Detection  
- ⭐ Face Alignment & Quality Checks  
- ⭐ Multi-Factor Authentication  
- ⭐ Cloud Deployment (AWS / GCP / Azure)  
- ⭐ REST API Integration  
- ⭐ Mobile App Integration  

---

## 👨‍💻 Author

**R Muralidharan**  
🎓 Data Science & Machine Learning Enthusiast  

🔗 GitHub: https://github.com/Muralidharan-ramachandran  
🔗 LinkedIn: https://www.linkedin.com/in/muralidharan-r-568007343/  

---

## ⭐ Support

If you found this project useful:

👉 Give it a **Star ⭐**  
👉 Fork it  
👉 Share with others  
