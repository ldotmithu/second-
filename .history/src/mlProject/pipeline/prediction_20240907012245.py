import joblib
from pathlib import Path
import os

class PredictionPipeline:
    def __init__(self) -> None:
        self.model=joblib.load(Path('artifacts/model_training/model.joblib'))