import datetime
import pandas as pd
import source_code.project_config as CONFIG


def load_dataset_and_validate(path):
    """Load the dataset and change the type of the "TIME" column to datetime.

    Keyword arguments:
    path -- path to the dataset
    """
    data = pd.read_csv(path)
    validate_node(data)
    validate_time(data)
    validate_lat_lang(data)

    # data["TIME"] = pd.to_datetime(data["TIME"], yearfirst=True, errors='coerce')
    # data["NODE"] = data["NODE"].astype(int)
    # data = data.sort_values(by=["NODE"]).reset_index(drop=True)

    return data

def validate_node(data):
    error_row_list = []
    for index, x in enumerate(data["NODE"].values):
        try:
            x = int(x)
        except:
            error_row_list.append(index)
    
    print("Following are the rows that are not validated for node")
    print(error_row_list)

def validate_lat_lang(data):
    error_row_lat_list = []
    for index, x in enumerate(data["LAT"].values):
        try:
            x = float(x)
        except:
            error_row_lat_list.append(index)
    
    print("Following are the rows that are not validated for LATITUDE")
    print(error_row_lat_list)

    error_row_lng_list = []
    for index, x in enumerate(data["LNG"].values):
        try:
            x = float(x)
        except:
            error_row_lng_list.append(index)
    
    print("Following are the rows that are not validated for LONGITUDE")
    print(error_row_lng_list)


def validate_time(data):
    error_row_list = []
    for index, x in enumerate(data["TIME"].values):
        try:
            newDate = datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
            print(newDate)
        except:
            error_row_list.append(index)
    
    print("Following are the rows that are not validated for time")
    print(error_row_list)



if __name__ == "__main__":
    original_dataset_path = CONFIG.ORIGINAL_DATASET_PATH
    benign_data = load_dataset_and_validate(original_dataset_path)
    