import pandas as pd
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix
import seaborn as sns
import numpy as np

matches = pd.read_csv("allmatches.csv", index_col=0)
pd.set_option("display.max_columns", None)

# Data preprocessing
matches["date"] = pd.to_datetime(matches["date"])
matches["venue_code"] = matches["venue"].astype("category").cat.codes
matches["opp_code"] = matches["opponent"].astype("category").cat.codes
matches["hour"] = matches["time"].str.replace(":.+", "", regex=True).astype(int)
matches["day_code"] = matches["date"].dt.dayofweek
matches["round_code"] = matches["round"].astype("category").cat.codes
matches["target"] = (matches["result"] == "W").astype(int)

predictors = ["venue_code", "opp_code", "hour", "day_code"]

# Define function to calculate rolling averages
def rolling_averages(group, cols, new_cols):
    group = group.sort_values("date")
    rolling_stats = group[cols].rolling(3, closed="left").mean()
    group[new_cols] = rolling_stats

    #Drop missing values when rolling averages aren't available
    group = group.dropna(subset=new_cols)
    return group

cols = ["gf", "ga", "sh", "sot", "dist", "fk", "pk", "pkatt", "target"]
new_cols = [f"{c}_rolling" for c in cols]

# Calculate rolling averages for each team
matches_rolling = matches.groupby("team").apply(lambda x: rolling_averages(x, cols, new_cols))
matches_rolling = matches_rolling.droplevel("team")
matches_rolling.index = range(matches_rolling.shape[0])
print(matches_rolling)
# Define function to make predictions
def make_predictions(data, predictors):

    rf = RandomForestClassifier(n_estimators=100, min_samples_split=250, random_state=1)

    train_set = data[data["date"] < '2023-01-01']
    test_set = data[data["date"] > '2023-01-01']
    
    rf.fit(train_set[predictors], train_set["target"])
    preds = rf.predict(test_set[predictors])

    combined = pd.DataFrame(dict(actual=test_set["target"], predicted=preds), index=test_set.index)
    precision = precision_score(test_set["target"], preds)
    feature_importances = rf.feature_importances_

    return combined, precision, feature_importances

combined, precision, features = make_predictions(matches_rolling, predictors + new_cols)


combined = combined.merge(matches_rolling[["date", "team", "opponent", "result"]], left_index=True, right_index=True)

print(precision)

import seaborn as sns
import matplotlib.pyplot as plt

