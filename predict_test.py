import joblib
import numpy as np

try:
    model = joblib.load('fishing_model.pkl')
    locations = {0: "جازان", 1: "فرسان", 2: "بيش"}

    def predict_fishing_status(temp, chloro, depth_m, loc_id):
        input_data = np.array([[temp, chloro, depth_m, loc_id]])
        predicted_score = model.predict(input_data)[0]
        
        if loc_id == 1:
            fish_types = ["ناجل", "هامور", "شعور"]
        elif depth_m > 40:
            fish_types = ["كنعد", "بياض"]
        else:
            fish_types = ["باغة", "سيجان"]

        return {
            "location": locations.get(loc_id, "غير معروف"),
            "fishing_score": round(predicted_score, 1),
            "recommended_fish": fish_types,
            "status": "ممتاز للصيد" if predicted_score > 70 else "متوسط" if predicted_score > 40 else "ضعيف"
        }

    result = predict_fishing_status(temp=27.5, chloro=3.8, depth_m=25.0, loc_id=1)
    print("📊 نتيجة التنبؤ الاختبارية:")
    print(result)

except Exception as e:
    print("❌ خطأ: يرجى تشغيل ملف train_fishing_model.py أولاً لإنشاء نموذج الذكاء الاصطناعي!")
