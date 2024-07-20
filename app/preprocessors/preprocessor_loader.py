import pickle

def load_preprocessor():
    with open('app/preprocessors/preprocessor.pkl', 'rb') as f:
        preprocessor = pickle.load(f)
    return preprocessor
