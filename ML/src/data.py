import pandas as pd

from . import features_info


def clean_dataset(in_path: str) -> pd.DataFrame:
    df_raw = pd.read_csv(in_path, dtype=features_info.types)
    df = df_raw[features_info.useful_columns]
    df = df.dropna(subset=["area", "offer_type_of_building"])
    df = df.where(df["rooms"] <= 4, 4)

    return df
