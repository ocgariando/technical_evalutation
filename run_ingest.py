import csv_to_sqlite

# all the usual options are supported
options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
input_files = ["admissions.csv", "codes.csv","members.csv"] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "lifespark.sqlite", options)