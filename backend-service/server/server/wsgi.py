# file backend/server/server/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.classifier.registry import MLRegistry
from apps.ml.classifier.LogisticRegression2 import LogisticRegressionClassifier2

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    lg2 = LogisticRegressionClassifier2()
    # add to ML registry

    registry.add_algorithm(endpoint_name="food_review_classifier",
                            algorithm_object=lg2,
                            algorithm_name="Logistic Regression Classifier",
                            algorithm_status="production",
                            algorithm_version="0.23.2",
                            owner="Dalvir Singh",
                            algorithm_description="Logistic Regression Classifier trained on Food Reviews on Amazon",
                            algorithm_code=inspect.getsource(LogisticRegressionClassifier2))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
