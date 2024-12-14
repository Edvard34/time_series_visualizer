import pandas as pd

# Імпортуємо дані з CSV
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Очищаємо дані, видаляючи екстремальні значення (2.5% найменших і найбільших значень)
lower_percentile = df['page_views'].quantile(0.025)
upper_percentile = df['page_views'].quantile(0.975)
df_clean = df[(df['page_views'] >= lower_percentile) & (df['page_views'] <= upper_percentile)]
