import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

print("⏳ جاري توليد البيانات البحرية لمنطقة جازان...")
np.random.seed(42)
n_samples = 1200

sea_temp = np.random.uniform(24.0, 32.0, n_samples)
chlorophyll = np.random.uniform(0.1, 5.0, n_samples)
depth = np.random.uniform(5.0, 100.0, n_samples)
location_code = np.random.choice([0, 1, 2], n_samples)

score = (
    (chlorophyll * 15) + 
    (30 - np.abs(sea_temp - 28) * 4) + 
    (np.where(location_code == 1, 15, 5))
)
fishing_score = np.clip(score, 10, 99)

df = pd.DataFrame({
    'sea_temp': sea_temp,
    'chlorophyll': chlorophyll,
    'depth': depth,
    'location_code': location_code,
    'fishing_score': fishing_score
})

X = df[['sea_temp', 'chlorophyll', 'depth', 'location_code']]
y = df['fishing_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("⏳ جاري تدريب نموذج الذكاء الاصطناعي...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'fishing_model.pkl')
print("✅ تم حفظ النموذج بنجاح في ملف 'fishing_model.pkl'!")
