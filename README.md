# Smart-Student-Assistant
Name-Aryan Gupta

B.Tech -CSE (AI & ML)

VIT BHOPAL

##  Overview

The **Smart Student Assistant** is an intelligent system designed to help students analyze and improve their academic performance using concepts from **Artificial Intelligence and Machine Learning**.

This project combines:

* Machine Learning for prediction
* Prolog for logical reasoning
*  Python for system integration

---

##  Problem Statement

Students often struggle to understand how their **study habits and attendance** affect their academic performance. There is no simple tool that provides both:

* Performance prediction
*  Personalized improvement suggestions

This project aims to bridge that gap using AI techniques.

---

##  Key Features

*  Predicts student marks using **Linear Regression**
*  Provides intelligent advice using **rule-based reasoning (Prolog)**
*  Fast and simple command-line interface
*  Integration of ML model with logic programming
*  Beginner-friendly and easy to understand

---

##  System Architecture

1. User inputs study hours and attendance
2. ML model predicts expected marks
3. Prolog evaluates performance conditions
4. System generates appropriate advice

---

##  Technologies Used

* Python
* Scikit-learn
* SWI-Prolog
* Git & GitHub

---

##  Project Structure

Smart-Student-Assistant/
│
├── data/
│   └── student_data.csv        # Dataset
│
├── model/
│   └── train_model.py         # ML model training
│
├── prolog/
│   └── rules.pl               # Prolog rules
│
├── app/
│   └── main.py                # Main application
│
└── README.md
```

---

##  Installation Guide

###  Install Python

Make sure Python 3.8+ is installed.

---

### 2️⃣ Install Required Libraries


pip install pandas scikit-learn
```



###  Install SWI-Prolog

Download from:
https://www.swi-prolog.org/

✔ Ensure `swipl` runs in terminal

---

##  How to Run the Project

### Step 1: Train the Model


cd model
python train_model.py
```

This creates the trained model file.

---

### Step 2: Run the Application


cd ../app
python main.py
```

---

##  Usage Instructions

After running the program:


Enter study hours:
Enter attendance (%):
```

Example input:


Study hours: 6
Attendance: 80
```

---

##  Sample Output


Predicted Marks: 72.3
Advice: You are doing well, keep it up!
```

---

##  Working Explanation

* The **ML model** uses historical data to predict marks
* The **Prolog engine** applies rules such as:

  * Low attendance → Suggest improvement
  * Low marks → Recommend more study
* Python acts as a bridge between ML and Prolog

---

##  Common Issues & Solutions

** Prolog not working**
 Install SWI-Prolog and restart terminal
** Module errors**
 Run:


pip install pandas scikit-learn


Future Enhancements

*  Web-based interface using Flask
* Chatbot using NLP techniques
* Advanced ML models (Decision Tree, Random Forest)
* Real-world dataset integration
*  Graph-based performance visualization

---

##Learning Outcomes

This project demonstrates:

* Application of Machine Learning in real-world problems
* Use of Prolog for knowledge representation
* Integration of multiple AI techniques
* Understanding of prediction models and logic systems

---



---

## Conclusion

The Smart Student Assistant is a simple yet powerful example of how **AI and Machine Learning** can be used to build intelligent systems that provide meaningful insights and support decision-making in education.
