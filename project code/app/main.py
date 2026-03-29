import pickle
import subprocess

with open('../model/model.pkl', 'rb') as f:
    model = pickle.load(f)

def get_prediction(study_hours, attendance):
    prediction = model.predict([[study_hours, attendance]])
    return round(prediction[0], 2)

def get_prolog_advice(attendance, marks):
    try:
        result = subprocess.run(
            ['swipl', '-s', '../prolog/rules.pl',
             '-g', f"suggestion({attendance},{marks},Advice),write(Advice),halt."],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except:
        return "Prolog not working. Install SWI-Prolog."

def main():
    print("=== Smart Student Assistant ===")

    study_hours = float(input("Enter study hours: "))
    attendance = float(input("Enter attendance (%): "))

    predicted_marks = get_prediction(study_hours, attendance)
    print(f"\nPredicted Marks: {predicted_marks}")

    advice = get_prolog_advice(attendance, predicted_marks)
    print(f"Advice: {advice}")

if __name__ == "__main__":
    main()
