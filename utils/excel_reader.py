import pandas as pd


def get_login_test_data():

    file_path = "utils/login_test_data.xlsx"

    df = pd.read_excel(file_path)

    return df.values.tolist()