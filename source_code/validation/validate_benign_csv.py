import datetime
import pandas as pd
import source_code.project_config as CONFIG


def load_dataset(path):
    """Load the dataset and change the type of the "TIME" column to datetime.

    Keyword arguments:
    path -- path to the dataset
    """
    data = pd.read_csv(path)
    validate_time(data)
    validate_node(data)
    # data["TIME"] = pd.to_datetime(data["TIME"], yearfirst=True, errors='coerce')
    # data["NODE"] = data["NODE"].astype(int)
    # data = data.sort_values(by=["NODE"]).reset_index(drop=True)

    return data


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

def validate_node(data):
    error_row_list = []
    for index, x in enumerate(data["NODE"].values):
        try:
            x = int(x)
        except:
            error_row_list.append(index)
    
    print("Following are the rows that are not validated for node")
    print(error_row_list)

if __name__ == "__main__":
    benign_dataset_path = CONFIG.OUTPUT_DIRECTORY + "\\clean_dataset\\Output\\benign_data\\benign_data_2021-01-02_00_00_00_2021-02-01_23_59_58_time_step_120_num_ids_60.csv"
    benign_data = load_dataset(benign_dataset_path)
    # now = datetime.datetime.now()

    # current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # print("Current Time =", current_time)
    