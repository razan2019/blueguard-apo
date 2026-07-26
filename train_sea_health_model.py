import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. إنشاء بيانات وهمية لتدريب مودل صحة البحر
np.random.seed(42)
n_samples = 1000

sea_temp = np.random.uniform(15.0, 35.0, n_samples)      # درجة حرارة البحر
chlorophyll = np.random.uniform(0.01, 2.0, n_samples)   # نسبة الكلوروفيل
depth = np.random.uniform(5.0, 200.0, n_samples)         # العمق بالمتر

# حالة صحة البحر (1 = صحي، 0 = غير صحي)
health_status = [
    1 if (20 <= t <= 28 and 0.1 <= c <= 1.0) else 0 
    for t, c in zip(sea_temp, chlorophyll)
]

df = pd.DataFrame({
    'sea_temp': sea_temp,
    'chlorophyll': chlorophyll,
    'depth': depth,
    'health_status': health_status
})

X = df[['sea_temp', 'chlorophyll', 'depth']]
y = df['health_status']

# 2. تدريب النموذج
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 3. حفظ ملف المودل
joblib.dump(model, 'sea_health_model.pkl')
print("Done: Sea Health Model trained and saved as 'sea_health_model.pkl'")
