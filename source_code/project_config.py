from pathlib import Path
import os

full_path = os.getcwd()
print(full_path)

DATASET_PATH = str(Path(full_path))
ORIGINAL_DATASET_PATH = os.path.join(DATASET_PATH + '\dataset', 'original_data.csv')

OUTPUT_DIRECTORY = os.path.join(str(Path(full_path)) + '\source_code')

print(ORIGINAL_DATASET_PATH)
print(OUTPUT_DIRECTORY)
