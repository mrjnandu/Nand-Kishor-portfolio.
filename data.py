"""
data.py : tumhara saara portfolio data yahan hai. Sirf is file ko edit karo.
[brackets] wali jagah apni real details likho. Text hamesha " " ke andar, aur har item ke baad comma.
"""

PROFILE = {
    "name": "Nand Kishor Vishwakarma",
    "roles": ["B.Tech CSE (AI) Student", "Machine Learning Enthusiast",
              "Python Developer", "Problem Solver"],
    "intro": "I build intelligent systems: from cleaning raw data to training models and deploying them as working products.",
    "about": [
        "I am a B.Tech student in Computer Science and Engineering (Artificial Intelligence) at Babu Banarasi Das University, Lucknow. I enjoy machine learning, deep learning and turning ideas into projects people can actually use.",
        "Beside classes I practise problem solving, build projects on GitHub and keep learning new tools. I am looking for internships and opportunities in AI, ML and data science.",
    ],
    "stats": [["[n]", "Projects"], ["[n]", "Certificates"], ["[n]", "Hackathons"], ["8.63", "CGPA (Sem I-IV)"]],
    "skills": [
        {"g": "Languages", "items": [["Python", 85], ["C / C++", 70], ["SQL", 70], ["JavaScript", 55]]},
        {"g": "ML and Deep Learning", "items": [["scikit-learn", 75], ["TensorFlow / Keras", 65], ["PyTorch", 60], ["OpenCV", 60]]},
        {"g": "Data and Tools", "items": [["Pandas / NumPy", 85], ["Git and GitHub", 75], ["Flask / FastAPI", 60], ["Jupyter / Colab", 85]]},
    ],
    "projects": [
        {"t": "[Project 1: Spam Classifier]", "problem": "[What problem does it solve?]",
         "approach": "[CNN / transfer learning, dataset used, how you deployed it]",
         "result": "[Accuracy or impact, e.g. 92% test accuracy]",
         "tags": ["Python", "TensorFlow", "Flask"], "gh": "https://email-sms-spam-classifier-for-ml.onrender.com/", "demo": "",
         "img": "assets/projects/project1.png",   # screenshot (optional)
         "file": ""},   # report/PPT PDF ka path, jaise "assets/projects/report1.pdf" (optional)
        {"t": "Account-Management-System", "problem": "Account management system project.",
         "approach": "View the project source code on GitHub.", "result": "",
         "tags": ["Account Management"], "gh": "https://github.com/mrjnandu/Account-Management-System", "demo": "",
         "img": "", "file": ""},
        {"t": "customer-churn-prediction", "problem": "Predicting which customers may stop using a service.",
         "approach": "Customer churn prediction project; see the repository for implementation details.",
         "result": "Project source code available on GitHub.",
         "tags": ["Machine Learning", "Customer Churn Prediction"],
         "gh": "https://github.com/mrjnandu/customer-churn-prediction", "demo": "",
         "img": "", "file": ""},
    ],
    "exp": [
        {"when": "[Month Year to Month Year]", "t": "[Internship / Role]", "org": "[Company]",
         "pts": ["[What you built or learned]", "[Result or impact]"]},
    ],
    "edu": [
        {"when": "[Start] to [End]", "t": "B.Tech, Computer Science and Engineering (AI)",
         "org": "Babu Banarasi Das University, Lucknow",
         "d": "CGPA: 8.63 (credit-weighted across Semesters I-IV). Semester SGPAs: I 8.46, II 8.50, III 8.67, IV 8.92. Machine Learning, Deep Learning, Automata Theory, Data Structures, DBMS."},
        {"when": "[2023]", "t": "Class 12", "org": "[D.D.I.College Bhitauli Bazar Maharajganj,273302]", "d": "[Percentage 70.02% or grade 'A']"},
        {"when": "[2021]", "t": "Class 10", "org": "[D.D.I.College Bhitauli Bazar Maharajganj,273302]", "d": "[Percentage 85% or grade 'A']"},
    ],
    "certs": [
        # Image/PDF wala certificate (file ko assets/certs/ mein rakho). "link" mein verify link (optional).
        {"name": "Certificate of Excellence — 2nd Position, Software Category (Tech Expo 2026)",
         "org": "IEEE Student Branch, BBD University, Lucknow", "year": "2026",
         "file": "assets/certs/tech-expo-2026.jpg", "link": ""},
        {"name": "Data Analytics Essentials", "org": "Cisco Networking Academy", "year": "2026",
         "file": "assets/certs/data-analytics-essentials-update.jpg", "link": ""},
        {"name": "Data Analytics Essentials Certificate", "org": "Cisco Networking Academy", "year": "2026",
         "file": "assets/certs/data-analytics-essentials.jpg", "link": ""},
        # Sirf naam likhna ho to aise bhi chalega:
        "[Certificate 3], [Platform]",
    ],
    "ach": ["2nd Position, Software Category — Tech Expo 2026, Babu Banarasi Das University, Lucknow",
            "[Coding profile: LeetCode / Kaggle rank]", "[College award or activity]"],
    "learning": ["Deep Learning", "Large Language Models", "MLOps and Deployment"],
    "photo": "assets/photo.jpg",   # photo ko assets/ folder mein photo.jpg naam se rakho
    "chips": ["Python", "Machine Learning", "Deep Learning"],   # photo ke paas floating tags (max 3)
    "email": "nandkishor2303@gmail.com",
    "links": [["GitHub", "https://github.com/mrjnandu"],
              ["LinkedIn", "https://www.linkedin.com/in/mrjnandu/"],
              ["Instagram", "https://www.instagram.com/mrj__nandu/"],
              ["Resume (PDF)", "assets/resume.pdf"]],
}
