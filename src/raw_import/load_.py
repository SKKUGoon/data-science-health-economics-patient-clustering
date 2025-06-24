import msoffcrypto
import os
from io import BytesIO
import pandas as pd

def load_inpatient_data(root_dir, year: int):
    """
    Load inpatient data for a specific year.
    
    Args:
        year: The year to load data for.

    Returns:
        A pandas DataFrame containing the outpatient data.
    """
    # Define files per year
    filenames = [
        f"{year}.01~12_입원.xlsx",
    ]

    dfs = []
    for fn in filenames:
        print("Opening file: ", fn)
        file_path = os.path.join(root_dir, "data", "20250512", fn)

        with open(file_path, "rb") as f:
            office_file = msoffcrypto.OfficeFile(f)
            office_file.load_key(password="0269251111")
            decrypted = BytesIO()
            office_file.decrypt(decrypted)
        
        df = pd.read_excel(decrypted, engine='openpyxl')
        dfs.append(df)
        
    return pd.concat(dfs)


def load_outpatient_data(root_dir, year: int):
    """
    Load outpatient data for a specific year.
    
    Args:
        year: The year to load data for.

    Returns:
        A pandas DataFrame containing the outpatient data.
    """
    # Define files per year
    filenames = [
        f"{year}.01~03_외래.xlsx",
        f"{year}.04~06_외래.xlsx",
        f"{year}.07~09_외래.xlsx",
        f"{year}.10~12_외래.xlsx",
    ]

    dfs = []
    for fn in filenames:
        print("Opening file: ", fn)
        file_path = os.path.join(root_dir, "data", "20250512", fn)

        with open(file_path, "rb") as f:
            office_file = msoffcrypto.OfficeFile(f)
            office_file.load_key(password="0269251111")
            decrypted = BytesIO()
            office_file.decrypt(decrypted)
        
        df = pd.read_excel(decrypted, engine='openpyxl')
        dfs.append(df)
        
    return pd.concat(dfs)