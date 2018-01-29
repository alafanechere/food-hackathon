# We used this script to load all kind of csv into proper table in our Postgres db

import sqlalchemy as sa
import pandas as pd
con = sa.create_engine('postgres://user:password@host/hackathon')
chunks = pd.read_csv('./weather-data.csv', sep=';')
# for chunk in chunks:
chunks.to_sql(name='weather_data', if_exists='replace', con=con, index=False)
