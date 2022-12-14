from pydantic import BaseModel
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
from imblearn.over_sampling import SMOTE

#FIXME: Verify the class attributes for the model
class Model():
    name: str
    version: str
    model : RandomForestClassifier
    model_path : str
    data_path : str
    parameters: dict
    metrics: dict

    def __init__(self, name, version, model_path, data_path, parameters, metrics):
        self.name = name
        self.version = version
        self.data_path = data_path
        self.parameters = parameters
        self.load_model(model_path)

    def load_model(self, model_path):
        """ load the model from the pkl file
        
        Args:
            model_path (str): path of the pkl file
        """
        self.model = pickle.load(open(model_path, "rb"))

    def save_model(self, model_path: str):
        """ save the model in a pkl file 

        Args:
            model_path (str): path of the pkl file
        """
        pickle.dump(self.model, open(model_path, "wb"))

    def train_model(self, data_path: str):
        """ train the model with the data from the csv file

        Args:
            data_path (str): path to the csv file
        """
        data = pd.read_csv(data_path)
        data['quality'] = data['quality'].apply(lambda x: 'good' if x >= 7 else 'bad')
        data.drop('Id', axis=1, inplace=True)
        target = data['quality']
        data.drop('quality', axis=1, inplace=True)
        sm = SMOTE(random_state=42)
        X_res, y_res = sm.fit_resample(data, target)
        X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        metrics = {'accuracy': accuracy_score(y_test, self.model.predict(X_test)),
                    'precision': precision_score(y_test, self.model.predict(X_test), average='weighted'),
                    'recall': recall_score(y_test, self.model.predict(X_test), average='weighted'),
                    'f1': f1_score(y_test, self.model.predict(X_test), average='weighted')}
        self.metrics = metrics
    
    def get_metrics(self):
        """ returns the metrics of the model

        Returns:
            dict : dictionnary of the metrics, i.e accuracy, precision, recall, f1
        """
        return self.metrics

    def get_parameters(self):
        """ returns the hyperparameters of the model

        Returns:
            dict : dictionary of the hyperparameters
        """
        return self.model.get_params(deep=True)
    
    def predict(self, wine):
        """ predict the quality of the wine

        Args:
            wine (_type_): the wine to predict

        Returns:
            str : a string containing the quality of the wine, e.g 'good' or 'bad'
        """
        return self.model.predict([wine])