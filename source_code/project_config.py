from pathlib import Path
import os

full_path = os.getcwd()

DATASET_PATH = str(Path(full_path).parents[0])
ORIGINAL_DATASET_PATH = os.path.join(DATASET_PATH + '\dataset', 'original_data.csv')
ORIGINAL_DATASET_SORTED_PATH = os.path.join(DATASET_PATH + '\dataset', 'original_data_sorted.csv')

OUTPUT_DIRECTORY = os.path.join(str(Path(full_path)))

print(ORIGINAL_DATASET_PATH)
print(OUTPUT_DIRECTORY)
