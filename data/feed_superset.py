import sqlalchemy as sa
import pandas as pd
con = sa.create_engine('mysql://root:root@127.0.0.1/juckerfarm_data')
chunks = pd.read_csv('./weather-data.csv', sep=';')
# for chunk in chunks:
chunks.to_sql(name='weather_data', if_exists='replace', con=con, index=False)
