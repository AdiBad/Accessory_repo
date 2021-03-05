#Convert csv to parquet
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
df=pd.read_csv(r"annotation_data.csv")
table=pa.Table.from_pandas(df)
pq.write_table(table,'converted.parquet')

#Read parquet into dataframe
table2 = pq.read_pandas('converted.parquet').to_pandas()
table2.head()
