The original dataset used is a ~3 GB file, found compressed at:

https://s3.amazonaws.com/udacity-hosted-downloads/ud507/pisa2012.csv.zip&sa=D&ust=1485634742421000&usg=AFQjCNHGt-xBGFNSpFQKdWJixhMmhwUPZA

generate_truncated_pisa_data.py takes in the "pisa2012.csv" file and returns "truncatedPisa.csv", a csv file containing approximately 1/10ths of the columns.

shape_chart_data.py reads in "truncatedPisa.csv" and shapes the data to be used in the data visualization, returning as "math_averages.csv"
