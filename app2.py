# Save this as app.py
# Note: You would typically use joblib.dump(best_model, 'model.pkl') 
# to save your model from Colab and joblib.load('model.pkl') locally.

from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# --- Mock Logic (Replace with your actual loaded model logic) ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    return re.sub(r"\s+", " ", text).strip()

@app.route('/')
def index2():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    review_text = data.get('text', '')
    
    # In a real local app, you would use: 
    # prediction = model.predict([clean_text(review_text)])[0]
    
    # Example logic for demo:
    is_defect = "broken" in review_text.lower() or "damage" in review_text.lower()
    
    result = {
        "sentiment": "negative" if is_defect else "positive",
        "defect_flag": is_defect,
        "risk_tier": "HIGH RISK" if is_defect else "SAFE"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)