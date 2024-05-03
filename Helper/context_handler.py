import pandas as pd


data = pd.read_csv('SQL_QA_Dataset_Expanded.csv')


unique_contexts = data['context'].drop_duplicates()


output_file_path = '../contexts.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    for context in unique_contexts:
        file.write(context + '\n')

print(f"Contexts have been saved to {output_file_path}")
