# file backend/server/apps/ml/income_classifier/random_forest.py
import joblib
import pandas as pd

class LogisticRegressionClassifier:
    def __init__(self):
        path_to_artifacts = "../machine-learning/"
        #Dataset 1 predictive models
        self.lg_model_1 =  joblib.load("/Users/ds070111/Documents/GitHub/SentimentAnalysisProject/backend-service/server/machine-learning/lg_model_1.joblib")
        self.vectorizer_1 = joblib.load("/Users/ds070111/Documents/GitHub/SentimentAnalysisProject/backend-service/server/machine-learning/vectorizer_1.joblib")
        self.tfidf_1 = joblib.load("/Users/ds070111/Documents/GitHub/SentimentAnalysisProject/backend-service/server/machine-learning/tfidf_1.joblib")
        
        #Dataset 2 predictive models

    def processing(self, input_data):
        # JSON to pandas DataFrame
        
        print(input_data)
        data = [input_data]

        user_data_df = pd.DataFrame(data, columns = ['text']) 
        
        user_data_features = self.vectorizer_1.transform(user_data_df['text'])

        user_data_tfidf_features = self.tfidf_1.fit_transform(user_data_features)

        return self.lg_model_1.predict(user_data_tfidf_features)
        
        
    def compute_prediction(self, input_data):
        try:
            print(input_data)
            prediction = self.processing(input_data)

            if(prediction[0] == 1):
                return {"label": "Happy", "status": "OK"}
            elif(prediction[0] == 2):
                return {"label": "Neutral", "status": "OK"}
            else:
                return {"label": "Sad", "status": "OK"}
        except Exception as e:
            return {"status": "Error", "message": str(e)}
