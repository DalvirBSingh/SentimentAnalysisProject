from django.test import TestCase

from apps.ml.classifier.LogisticRegression import LogisticRegressionClassifier

class MLTests(TestCase):
    def test_LG_algorithm(self):
        my_alg = LogisticRegressionClassifier()
        response = my_alg.compute_prediction(["I love this kindle!"])
        print("Check here....")
        print(response)
        self.assertEqual('OK', response['status'])
