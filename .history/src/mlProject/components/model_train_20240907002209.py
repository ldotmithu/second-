from mlProject.config.configuration import *
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
import joblib
from mlProject import logging

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def train(self):
    # Load the training and testing data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        # Define the target column
        target_col = 'quality'
        
        # Split the features (X) and target (y) for training and testing
        X_train = train_data.drop(columns=[target_col])
        X_test = test_data.drop(columns=[target_col])
        y_train = train_data[target_col]
        y_test = test_data[target_col]
        
        # Define the RandomForestRegressor model
        rf = RandomForestRegressor(
            n_estimators=1000,
            criterion='squared_error',
            max_depth=6,
            min_samples_split=4,
            min_samples_leaf=2,
            max_features='sqrt',
            bootstrap=True,
            n_jobs=-1,
            random_state=42
        )
        
        # Train the model
        rf.fit(X_train, y_train)
        
        # Correct directory path creation
        model_dir = os.path.join(self.config.root_dir, 'artifacts', 'model_training')
        
        # Ensure the directory exists (use 'exist_ok=True' to avoid errors if it exists already)
        os.makedirs(model_dir, exist_ok=True)
        
        # Correct model path construction
        model_path = os.path.join(model_dir, self.config.model_name)
        
        # Save the trained model
        joblib.dump(rf, model_path)
        
        
        
        