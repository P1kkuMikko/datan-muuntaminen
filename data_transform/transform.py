import pandas as pd

def clean_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: Siivoa tekstisarakkeet kuten 'name' ja 'capital'.

    Ohjeet:
    - Käytä pandasin `.str`-metodeja
    - Poista ympäröivät välilyönnit
    - Muuta title-caseen (iso alkukirjain aina)

    Palauta siivottu DataFrame.
    """
    df = df.copy()
    for col in ["name", "capital"]:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip().str.title()

    return df


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: Käsittele puuttuvat arvot.

    Ohjeet:
    - Lisää funktioon type hint, joka kertoo, että funktio ottaa syötteenä on DataFramen ja myös palautettaa DataFramen
    - Tee df-kopio, jotta funktio ei muokkaa alkuperäistä DataFramea
    - Korvaa "N/A" ja vastaavat merkeillä `pd.NA`
    - Tulosta kuinka monta puuttuvaa arvoa sarakkeissa on

    Palauta DataFrame, jossa puuttuvat arvot käsitelty.
    """
    df = df.copy()
    df = df.replace(["N/A", "n/a", "NA", "null", "None", ""], pd.NA)
    print(df.isna().sum())
    df = df.dropna()

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    # TODO: Poista duplikaatit.

    Ohjeet:
    - Lisää funktioon type hint, joka kertoo, että funktio ottaa syötteenä on DataFramen ja myös palautettaa DataFramen
    - Tee df-kopio, jotta funktio ei muokkaa alkuperäistä DataFramea
    - Poista päällekkäiset rivit perustuen 'name'-sarakkeeseen
    - Palauta puhdistettu DataFrame
    """
    df = df.copy()
    df = clean_strings(df)
    df = df.drop_duplicates(subset=["name"], keep="first")

    return df


def fix_types_and_sort(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: Korjaa sarakkeiden tyypit ja järjestä.

    Ohjeet:
    - Lisää funktioon type hint, joka kertoo, että funktio ottaa syötteenä on DataFramen ja myös palautettaa DataFramen
    - Tee df-kopio, jotta funktio ei muokkaa alkuperäistä DataFramea
    - Muunna numeromuotoiset sarakkeet numeerisiksi
    - Järjestä DataFrame nimen mukaan
    """
    df = df.copy()
    if "population" in df.columns:
        df["population"] = pd.to_numeric(df["population"], errors="coerce")
    df = df.sort_values(by="name").reset_index(drop=True)

    return df


"""
Alla oleva lista määrittelee moduulin julkiset funktiot, eli mitkä funktionimet tuodaan mukaan, 
kun käytetään from module import * -syntaksia.
"""
__all__ = [
    "clean_strings",
    "handle_missing",
    "remove_duplicates",
    "fix_types_and_sort"
]
