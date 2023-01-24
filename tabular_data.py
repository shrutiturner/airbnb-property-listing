import pandas as pd


def remove_rows_with_missing_ratings(dataframe) -> pd.DataFrame:
    """Identifies any rating columns and removes rows where any of the values
    in these columns are missing.

    Args:
        dataframe (pd.DataFrame): dataframe of raw data to be cleaned.

    Returns:
        pd.DataFrame: cleaned dataframe with no missing values in the ratings
                      columns.
    """
    column_list = dataframe.columns
    ratings_columns = [column_name for column_name in column_list if
                       column_name.endswith('_rating')]

    clean_dataframe = dataframe.dropna(subset=ratings_columns)

    return clean_dataframe


if __name__ == '__main__':
    data = pd.read_csv('assets/AirBnbData.csv')

    clean_df = remove_rows_with_missing_ratings(data)

    # print(clean_df.isna().sum())
