import pandas as pd
from itertools import product

def load_data(filepath):
    return pd.read_csv(filepath)

def generate_color_pairs(df):
    # Group by 'cod_color' and 'des_color' and count occurrences
    pair_counts = df.groupby(['cod_color', 'des_color']).size().reset_index(name='count')
    
    # Get all unique cod_colors and des_colors
    cod_colors = df['cod_color'].unique()
    des_colors = df['des_color'].unique()
    
    # Create all possible pairs
    all_pairs = pd.DataFrame(list(product(cod_colors, des_colors)), columns=['cod_color', 'des_color'])
    
    # Merge with pair_counts to ensure all pairs are included, filling missing counts with 0
    result = all_pairs.merge(pair_counts, on=['cod_color', 'des_color'], how='left').fillna(0)
    
    # Remove pairs with 0 occurrences
    result = result[result['count'] > 0]
    
    return result

if __name__ == "__main__":
    filepath = "data/product_with_attributes.csv"
    data = load_data(filepath)
    color_pairs = generate_color_pairs(data)
    output_filepath = "color_pairs.csv"
    color_pairs.to_csv(output_filepath, index=False)
    print(f"Color pairs saved to {output_filepath}")