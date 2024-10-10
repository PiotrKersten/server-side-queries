import pandas as pd
import datetime

# Sample DataFrame with datetime values
data = {
    'timestamp': pd.to_datetime(['2024-03-06 12:00:00', '2024-03-06 13:00:00', '2024-03-06 14:00:00']),
    'value': [1, 2, 3]
}
df = pd.DataFrame(data)
datetime_values = df['timestamp'].tolist()


