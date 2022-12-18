# DATA
The dataset is composed of 1599 samples wine with 12 features each. The features are:
- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- density
- pH
- sulphates
- alcohol
- quality (score between 0 and 10)

Each wine has a unique Id in the dataset.
# MODELS
The models used are:
- Random Forest Classifier (RFC) with 300 estimators, trained on the whole dataset resampled with SMOTE to balance the classes.


# APP SETUP

# TECHNICAL CHOICES
- Traget transformation: 
    - the target is transformed into a binary variable ("bad" or "good") to predict if the wine is good or not. The threshold is set to 7, which means that the wine is good if the quality is higher than 7.
    We made this choice because we wanted to have a balanced dataset to train the model. Indeed, the dataset is unbalanced, with 983 wines with a quality lower than 7 and 159 wines with a quality higher than 7.
   
- Model selection:
    - The model is a Random Forest Classifier (RFC) with 300 estimators, trained on the whole dataset resampled with SMOTE to balance the classes.
    We made this choice because we wanted to have a model that is easy to train and to interpret. Indeed, the RFC is a model that is easy to train and to interpret. Moreover, it is a model that is robust to outliers and to unbalanced dataset. Finally, it is a model that is not sensitive to the scale of the features. It was trained using GridSearchCV to find the best parameters.

- Model evaluation:
    - The model is evaluated using : 
        - the accuracy score, which is the ratio of the number of correct predictions to the total number of predictions.
        - the precision score, which is the ratio of the number of correct positive predictions to the total number of positive predictions.
        - the recall score, which is the ratio of the number of correct positive predictions to the total number of positive samples.
        - the f1 score, which is the harmonic mean of the precision and recall scores.

- Best Wine selection:
    - The best wine is selected using the following criteria:
        - the wine is good (quality > 7)
        - the wine has the highest level of alcohol of all the good wines. We made this choice because the data analysis showed that the alcohol level is a good indicator of the quality of the wine. We can verify this assumption by looking at the correlation between the alcohol level and the quality on the following graph:
        ![alt text](app/datasource/importance.png)