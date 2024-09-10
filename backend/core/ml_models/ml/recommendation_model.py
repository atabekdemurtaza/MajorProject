import os
import joblib


class RecommendationModel:
    def __init__(self):
        self.model = None
        self.vectorizer = None

    def load_model(self):
        model_path = os.path.join(os.path.dirname(__file__), '../saved_models/logistic_regression_model.pkl')
        vectorizer_path = os.path.join(os.path.dirname(__file__), '../saved_models/tfidf_vectorizer.pkl')

        with open(model_path, 'rb') as file:
            self.model = joblib.load(file)

        with open(vectorizer_path, 'rb') as file:
            self.vectorizer = joblib.load(file)

        # Выводим словарь векторизатора для проверки
        print(f"TF-IDF Vocabulary: {self.vectorizer.vocabulary_}")

    def predict(self, review_text):
        if self.model is None:
            raise Exception("Model is not loaded, please call load_model() first")
        if self.vectorizer is None:
            raise Exception("Vectorizer is not loaded, please call load_model() first")

        transformed_X = self.vectorizer.transform([review_text])

        print(f"Transformed text: {transformed_X}")

        prediction = self.model.predict(transformed_X)

        print(f"Prediction: {prediction}")

        return prediction
