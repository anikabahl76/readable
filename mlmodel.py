from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

PREDICTIVE_CHARACTERISTICS = ["rank_last_week", "weeks_on_list", "publisher", "author"]
PREDICTION_CHARACTERISTIC = "rank"


def train_knn_model(data, num_neighbors):
    train_df, test_df = train_test_split(data, test_size=0.2)
    ohe = OneHotEncoder(handle_unknown='ignore')
    knn_model = KNeighborsClassifier(num_neighbors)
    knn_model.fit(ohe.fit_transform(train_df[PREDICTIVE_CHARACTERISTICS]), train_df[PREDICTION_CHARACTERISTIC])
    return knn_model, ohe, train_df, test_df

def get_model_accuracy(model, data, ohe):
    all_adjusted = ohe.transform(data[PREDICTIVE_CHARACTERISTICS])
    predicted_y = model.predict(all_adjusted)
    target_y = data[PREDICTION_CHARACTERISTIC].to_numpy()
    accuracy = (predicted_y == target_y).sum() / len(predicted_y)    
    return accuracy, predicted_y, target_y

def get_accurate_knn_model(data):
    for i in range(3, 20):
        model, ohe, train_df, test_df = train_knn_model(data, 5)
        accuracy, predicted_y, target_y = get_model_accuracy(model, test_df, ohe)
        if accuracy > 0.7:
            print("found k nearest neighbors model that uses " + str(i) + " neighbors to predict " + PREDICTION_CHARACTERISTIC + " with a " + str(accuracy * 100) + "%% accuracy")
            return model, i, accuracy

