
import joblib
import pandas as pd
import os

class LogisticRegressionClassifier2:
    def __init__(self):
        path_to_artifacts = os.getcwd() 
        #Dataset 1 predictive models
        self.lg_model =  joblib.load(path_to_artifacts +"/machine-learning/lg_model2.joblib")
        self.vectorizer = joblib.load(path_to_artifacts +"/machine-learning/vectorizer2.joblib")
        self.tfidf = joblib.load(path_to_artifacts +"/machine-learning/tfidf2.joblib")
        
        #Dataset 2 predictive models

    def processing(self, input_data):
        # JSON to pandas DataFrame
        print("Logging here")
        print(input_data)
        data = [input_data]

        user_data_df = pd.DataFrame(data, columns = ['text']) 
        
        user_data_features = self.vectorizer.transform(user_data_df['text'])

        user_data_tfidf_features = self.tfidf.fit_transform(user_data_features)

        return self.lg_model.predict(user_data_tfidf_features)
        
        
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
