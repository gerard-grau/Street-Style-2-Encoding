import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors


def split_features_and_labels(dataframe: pd.DataFrame) -> pd.DataFrame:
    features = dataframe.iloc[:, :-11]  # All columns except the last eleven
    labels = dataframe.iloc[:, -11:]    # The last eleven columns
    return features, labels


def main() -> None:
    # Load embeddings data
    embeddings_df = pd.read_csv('embeddings.csv')
    embeddings = embeddings_df.values

    products = pd.read_csv('data/product_with_attributes.csv')
    features, labels = split_features_and_labels(products)
    
    features['embeddings'] = list(embeddings)

    




    # Initialize NearestNeighbors model
    nn_model = NearestNeighbors(n_neighbors=1, algorithm='auto')
    nn_model.fit(embeddings)



    # Given a fashion clip embedding
    input_embedding = np.array([...])  # Replace with the actual embedding


    # Find the nearest neighbor for each label
    for label in labels.columns:
        distances, indices = nn_model.kneighbors([input_embedding])
        nearest_index = indices[0][0]
        nearest_neighbor = embeddings_df.iloc[nearest_index]
        print(f"Nearest neighbor for label {label}: {nearest_neighbor}")

if __name__ == '__main__':
    main()