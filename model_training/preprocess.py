import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(data):

    
    data = data.dropna()  

    
    if 'Type' in data.columns:
        label_encoder = LabelEncoder()
        data['Type'] = label_encoder.fit_transform(data['Type'])

    
    features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    target = 'Target'

    
    X = data[features]
    y = data[target]

    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

if __name__ == '__main__':

    data = pd.read_csv('../data.csv')

    
    X, y = preprocess_data(data)

    
    pd.DataFrame(X, columns=['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']).to_csv('data/preprocessed_features.csv', index=False)
    pd.DataFrame(y, columns=['Target']).to_csv('data/preprocessed_target.csv', index=False)

    print("Data preprocessing completed!")
