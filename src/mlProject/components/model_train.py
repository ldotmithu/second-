from mlProject.config.configuration import ModelTrainConfig
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib
import os

class ModelTrain:
    def __init__(self, config: ModelTrainConfig):
        self.config = config

    def preprocess_task(self):
        num_col = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                   'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
                   'density', 'pH', 'sulphates', 'alcohol']
        
        num_pipeline = Pipeline([
            ('scaler', StandardScaler())
        ])
        
        preprocess = ColumnTransformer([
            ('num_pipeline', num_pipeline, num_col)
        ])
        
        return preprocess

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        target_col = 'quality'
        
        X_train = train_data.drop(columns=[target_col])
        X_test = test_data.drop(columns=[target_col])
        y_train = train_data[target_col]
        y_test = test_data[target_col]
        
        preprocess_obj = self.preprocess_task()
        
        X_train = preprocess_obj.fit_transform(X_train)
        X_test = preprocess_obj.transform(X_test)  # Use transform here
        
        # Initialize models
        models = {
            'Linear Regression': LinearRegression(),
            'ElasticNet': ElasticNet(),
            'SVR': SVR()
        }
        
        # Example: Hyperparameter tuning for ElasticNet
        param_grid = {
            'alpha': [0.1, 1.0, 10.0],
            'l1_ratio': [0.1, 0.5, 0.9]
        }
        grid_search = GridSearchCV(ElasticNet(), param_grid, cv=5)
        grid_search.fit(X_train, y_train)
        best_elasticnet = grid_search.best_estimator_
        
        # Training and saving models
        for name, model in models.items():
            model.fit(X_train, y_train)
            joblib.dump(model, os.path.join(self.config.root_dir, f"{name}.joblib"))
            print(f"{name} model saved at {os.path.join(self.config.root_dir, f'{name}.joblib')}")
            
        
        # Print best parameters for ElasticNet
        print(f"Best parameters for ElasticNet: {best_elasticnet}")

