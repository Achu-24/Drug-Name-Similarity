import pandas as pd
from fuzzywuzzy import process

# Load dataset of drug names
df = pd.read_csv("data/drug_names.csv")
drug_names = df['drug_name'].dropna().tolist()

def get_similar_drugs(user_input, limit=5):
    """
    Suggests similar drug names based on user input using fuzzy string matching.
    """
    matches = process.extract(user_input, drug_names, limit=limit)
    return [m[0] for m in matches if m[1] > 60]  # return names with similarity >60%
