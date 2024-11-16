import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.neighbors import NearestNeighbors

def main():
    st.title("Fashion Image Nearest Neighbor Finder")

    # Centered image upload section
    st.markdown(
        """
        <style>
        .center {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='center'><h3>Upload an Image</h3></div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Compute the embedding of the uploaded image
        # input_embedding = compute_embedding(image)  # Implement this function

        # Placeholder embedding for demonstration
        input_embedding = np.random.rand(128)  # Replace with actual embedding

        # Load embeddings data
        embeddings_df = pd.read_csv('embeddings.csv')  # Embeddings stored in a CSV file
        embeddings = embeddings_df.values

        # Initialize NearestNeighbors model
        nn_model = NearestNeighbors(n_neighbors=1, algorithm='auto')
        nn_model.fit(embeddings)

        # Find the nearest neighbor
        distances, indices = nn_model.kneighbors([input_embedding])
        nearest_index = indices[0][0]
        nearest_embedding = embeddings_df.iloc[nearest_index]

        # Display the nearest neighbor image
        # Assuming embeddings_df has a column 'image_path' with image file paths
        # neighbor_image_path = embeddings_df['image_path'].iloc[nearest_index]
        # neighbor_image = Image.open(neighbor_image_path)
        # st.image(neighbor_image, caption='Nearest Neighbor Image', use_column_width=True)

        st.success("Nearest neighbor found!")

if __name__ == '__main__':
    main()