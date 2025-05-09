# train_intent_model.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
from latihan_program import training_sentences, training_labels

# Buat pipeline NLP + ML
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Latih model
model.fit(training_sentences, training_labels)

# Simpan model
joblib.dump(model, "intent_model.pkl")

print("✅ Model intent selesai dilatih dan disimpan.")
