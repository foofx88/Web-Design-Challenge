import pandas as pd

cities_df = pd.read_csv("Resources\cities.csv")

html_version = cities_df.to_html(index=False)

text_file = open ("output.html", "w")
text_file.write(html_version)
text_file.close()