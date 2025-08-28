import pickle
import numpy as np
tr = pickle.load(open("model.pkl", "rb"))
scalar = pickle.load(open("scalar.pkl", "rb"))


def predict_class(input_data : dict):
    gender = 1 if input_data['Gender'] == 'M' else 0
    input_data.pop('Gender')
    input_data = scalar.transform(np.array(list(input_data.values())).reshape(1, -1))
    data=np.insert(input_data, 0, gender)
    data = data.reshape(1, -1)
    prediction = tr.predict(data)[0]
    if prediction == 0:
        class_p='Negative'
    elif prediction == 1:
        class_p='Suspect'
    elif prediction == 2:
        class_p='Positive'
    return class_p