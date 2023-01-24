import math
from typing import Dict

from sklearn.dummy import DummyRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.linear_model import (BayesianRidge, ElasticNet, Lasso,
                                  LinearRegression, Ridge, SGDRegressor)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR, LinearSVR
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor, XGBRFRegressor

from ._models import _EasyModel


class EasyRegressor(_EasyModel):
    """ """
    DEFAULT_REGRESSORS = {
        'Dummy Regressor': DummyRegressor,
        'Linear Regressor': LinearRegression,
        'Lasso Regressor': Lasso,
        'Ridge Regressor': Ridge,
        'Bayesian Ridge Regressor': BayesianRidge,
        'Elastic Net Regressor': ElasticNet,
        'SGD Regressor': SGDRegressor,
        'Decision Tree Regressor': DecisionTreeRegressor,
        'Gaussian Process Regressor': GaussianProcessRegressor,
        'Support Vector Regressor': SVR,
        'Linear SVR': LinearSVR,
        'XGB Regressor': XGBRegressor,
        'XGBRF Regressor': XGBRFRegressor,
        'MLP Regressor': MLPRegressor
    }
    METRICS = {
        "Mean Absolute Error": mean_absolute_error,
        "Mean Squared Error": mean_squared_error,
        "Root Mean Squared Error": lambda X, y: math.sqrt(mean_squared_error(X, y)),
        "R2 Score": r2_score
    }

    def __init__(self, models_dict: Dict = None,
                 include_defaults: bool = True):
        super().__init__(self.DEFAULT_REGRESSORS, models_dict,
                         include_defaults=include_defaults)

    def fit(self, X, y):
        """
        Fit classifiers in self._models on features X with targets y\n
        Calls method fit for each model in self._models

        Parameters
        ----------
        X : array of features

        y : array of targets

        Returns
        -------
        None
        """
        super().fit(X, y)

    def predict(self, X):
        """
        Make predictions for features in X\n
        Call predict method for each model in self._models

        Parameters
        ----------
        X : array of features


        Returns
        -------
        preds: Dict
            Dictionary with same keys in self._models and predictions for each
            model of features in X

        """
        return super().predict(X)

    def score(self, X, y, as_df=False, sorted=True):
        """
        Calculate score for each model in self._models\n
        Calls score method for each model in self._models\n
        Return mean accuracy for each model on the given data and labels

        Parameters
        ----------
        X : array of features

        y : array of targets

        as_df : boolean
            - if True: return results in pd.DataFrame
            - if False: return results in dictionary
            (Default value = False)
        sorted: boolean
            - if True: returns results sorted in discending order by score
            - if False: returns results in the original order of models
            (Default value = True)

        Returns
        -------
        results: Dict (as_df=False) or pd.Dataframe (as_df=True)
        """
        return super().score(X, y, as_df=as_df, sorted=sorted)

    def evaluate(self, X, y, as_df=False, model_first=True, from_preds=False):
        """
        Returns models results on each of the metrics in self.METRICS
        dictionary

        Parameters
        ----------
        X : array of features

        y : array of targets

        as_df : boolean
            - if True: return results in pd.DataFrame
            - if False: return results in dictionary
            (Default value = False)
        model_first : boolean
            - if True: returns models at axis=0 (rows), results at axis=1 (columns)
            - if False: returns models at axis=1 (columns), results at axis=0 (rows)
            (Default value = True)
        from_preds : boolean
            - if True: make preditions then calacuate metrics (X holds input features)
            - if False: calcualte metrics from predictions (X holds predictions)
            (Default value = False)

        Returns
        -------
        results: Dict (as_df=False) or pd.Dataframe (as_df=True)

        """
        return super().evaluate(X, y, as_df=False, model_first=True,
                                from_preds=False)

    def get_model(self, model_key):
        """
        Get specific model from self._models

        Parameters
        ----------
        model_key : the key for model in self._models

        Returns
        -------
        model object corrseponding to key if key exist
        None if key does not exist

        """
        return self._models.get(model_key, None)
