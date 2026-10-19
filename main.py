import pandas as pd
# TODO: Tuo data_tansform-paketin transform-moduulin funktiot
from data_transform.transform import (
	clean_strings,
	handle_missing,
	remove_duplicates,
	fix_types_and_sort,
)

def main():
	file_path = "data/countries_noisy.json"
	save_path = "data/countries_cleaned.json"

	# TODO: Lue data JSON-tiedostosta DataFrameen
	data = pd.read_json(file_path)

	# TODO: Tulosta 10 ensimmäistä riviä datasta ja rivimäärä ennen siivousta
	print("Original data sample:")
	print(data.head(10))
	print(f"Rows before cleaning: {len(data)}")


	# Suorittaa kaikki siivousvaiheet peräkkäin
	data = clean_strings(data)
	data = handle_missing(data)
	data = remove_duplicates(data)
	data = fix_types_and_sort(data)

	# TODO: Tallenna puhdistettu data uuteen JSON-tiedostoon, käytä save_path-muuttujaa
	data.to_json(save_path, orient="records", indent=4)

	# TODO: Tulosta 10 ensimmäistä riviä puhdistetusta datasta ja rivimäärä siivouksen jälkeen
	print("Cleaned data sample:")
	print(data.head(10))
	print(f"Rows after cleaning: {len(data)}")

if __name__ == "__main__":
	main()
