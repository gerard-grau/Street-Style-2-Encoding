import pandas as pd


PATH = '/home/pol/Desktop'
IMAGES_PATH = f"{PATH}/archive/images/images/"
CSV_PATH = f"{PATH}/archive/"
HEIGHT = 224
WIDTH = 160


def add_attribute_columns(products_df, attributes_df):
    # Get unique attribute names
    unique_attributes = attributes_df['attribute_name'].unique()


    # Create a copy of the products dataframe
    result_df = products_df.copy()
    
    # For each attribute type
    for attr in unique_attributes:
        # Create a mapping dictionary for this attribute
        attr_mapping = attributes_df[attributes_df['attribute_name'] == attr].set_index('cod_modelo_color')['des_value']
        # Add the column with the attribute values, filling missing values with empty string
        result_df[attr] = result_df['cod_modelo_color'].map(attr_mapping).fillna("INVALID")
    return result_df


# read csv
products_df = pd.read_csv(CSV_PATH + 'product_data.csv')
# remove column
products_df.drop(columns= ["cod_color"], inplace=True)

attributes_df = pd.read_csv(CSV_PATH + 'attribute_data.csv')
result = add_attribute_columns(products_df, attributes_df)

print(result.head(10))
# Save the result to a new CSV file
result.to_csv(CSV_PATH + 'product_with_attributes.csv', index=False)
