import pandas as pd
from mbmutils import mu

common_cols = [
    "date", "ymd", "ym", "y",
    "dead", "injured", "total",
    "state"
]

def read_mass_shooting() -> pd.DataFrame:
    df = pd.read_csv(mu.get_full_path("data/mass-shootings-20182022/shootings_2018.csv"))

    # some common renames
    df["injured"] = df["Injured"]
    df["dead"] = df["Dead"]
    df["total"] = df["Total"]

    df["state"] = df["State"]

    df["date"] = pd.to_datetime(df.Date)
    df["y"] = df.date.apply(lambda x: x.strftime("%Y"))
    df["ym"] = df.date.apply(lambda x: x.strftime("%Y-%m"))
    df["ymd"] = df.date.apply(lambda x: x.strftime("%Y-%m-%d"))

    return df[common_cols]


def read_gun_violence() -> pd.DataFrame:
    df = pd.read_csv(mu.get_full_path("data/gun-violence-20142022/gun-violence-20142022.csv"))

    # some common renames
    df["dead"] = df["killed"]

    df["total"] = df.injured + df.dead

    df["date"] = pd.to_datetime(df.incident_date)
    df["y"] = df.date.apply(lambda x: x.strftime("%Y"))
    df["ym"] = df.date.apply(lambda x: x.strftime("%Y-%m"))
    df["ymd"] = df.date.apply(lambda x: x.strftime("%Y-%m-%d"))

    df["y"] = df["y"].astype("int")

    return df[common_cols]


def read_state_population() -> pd.DataFrame:
    return pd.read_csv(mu.get_full_path("data/state_population.csv"))


def read_state_population_by_year() -> pd.DataFrame:
    return pd.read_csv(mu.get_full_path("data/state_population_by_year_items.csv"))
    # return pd.read_csv(mu.get_full_path("data/state_population_columns.csv"))




