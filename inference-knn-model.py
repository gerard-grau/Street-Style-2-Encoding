import pandas as pd
import numpy as np
import torch
from sklearn.neighbors import NearestNeighbors


def split_features_and_labels(dataframe: pd.DataFrame) -> pd.DataFrame:
    features = dataframe.iloc[:, :-11]  # All columns except the last eleven
    labels = dataframe.iloc[:, -11:]    # The last eleven columns
    return features, labels


def main() -> None:
    # Load embeddings data
    embeddings_file = "image_embeddings.pt"

    embeddings_dict = torch.load(embeddings_file)

    products = pd.read_csv('data/product_with_attributes.csv')
    embeddings = [embeddings_dict[filename] for filename in products['des_filename']]
    
    # embeddings = [embedding.numpy() for embedding in embeddings]
    
    
    
    features, labels = split_features_and_labels(products)
    
    # Convert the list of embeddings to a NumPy array
    embeddings_array = np.array(embeddings)

    # Add each dimension as a separate feature
    for i in range(512):
        features[f'embedding_dim_{i}'] = embeddings_array[:, i]
    # products = pd.concat([products, embedding_columns], axis=1)

    




    # Initialize NearestNeighbors model
    nn_model = NearestNeighbors(n_neighbors=1, algorithm='auto')
    nn_model.fit(embeddings)



    # Given a fashion clip embedding
    # input_embedding = np.array([...])  # Replace with the actual embedding
    embeddings_file_test = "image_embeddings.pt"

    embeddings_dict_test = torch.load(embeddings_file)


    # Find the nearest neighbor for each label
    for label in labels.columns:
        distances, indices = nn_model.kneighbors([input_embedding])
        nearest_index = indices[0][0]
        nearest_neighbor = embeddings_df.iloc[nearest_index]
        print(f"Nearest neighbor for label {label}: {nearest_neighbor}")

if __name__ == '__main__':
    main()