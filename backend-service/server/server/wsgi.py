# file backend/server/server/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.classifier.registry import MLRegistry
from apps.ml.classifier.LogisticRegression import LogisticRegressionClassifier
from apps.ml.classifier.LogisticRegression2 import LogisticRegressionClassifier2

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    lg = LogisticRegressionClassifier()
    lg2 = LogisticRegressionClassifier2()
    # add to ML registry
    registry.add_algorithm(endpoint_name="consumer-reviews-of-amazon-products_classifier",
                            algorithm_object=lg,
                            algorithm_name="Logistic Regression Classifier",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Dalvir Singh",
                            algorithm_description="Logistic Regression Classifier trained on Consumer Reviews of Amazon Products",
                            algorithm_code=inspect.getsource(LogisticRegressionClassifier))
    registry.add_algorithm(endpoint_name="food_review_classifier",
                            algorithm_object=lg2,
                            algorithm_name="Logistic Regression Classifier",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Dalvir Singh",
                            algorithm_description="Logistic Regression Classifier trained on Food Reviews on Amazon",
                            algorithm_code=inspect.getsource(LogisticRegressionClassifier2))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
