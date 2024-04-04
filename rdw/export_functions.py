from rdw import EXPORT_FOLDER
import os


def export_df(df, plate):

    # define the folder name
    folder_name = f"{EXPORT_FOLDER}/{plate}"

    # create the folder
    os.makedirs(folder_name, exist_ok=True)

    # compose the file path
    file_path = f"{folder_name}/export_{plate}.csv"

    # export the data frame
    df.to_csv(file_path, index=False)

    print(f"✅ Succesfully exported to {file_path}")
