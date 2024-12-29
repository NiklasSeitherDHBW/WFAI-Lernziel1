import matplotlib.pyplot as plt
import seaborn as sns

def test(df, categories):
    df["period"] = df["published_date"].dt.year

    df['categories'] = df['categories'].str.lower().str.split(',')
    df = df.explode('categories')
    df['categories'] = df['categories'].str.strip()

    df_filtered = df[df['categories'].isin(categories)]

    counts = df_filtered.groupby(['categories', "period"]).size().reset_index(name='count')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 7))

    sns.lineplot(data=counts, x='period', y='count', hue='categories', marker='o', ax=ax1)
    ax1.set_title("Publication Counts by Period and Category (Linear Scale)")
    ax1.set_xlabel("Period")
    ax1.set_ylabel("Count of Papers Published")
    ax1.legend(title='Category')
    ax1.tick_params(axis='x', rotation=45)

    sns.lineplot(data=counts, x='period', y='count', hue='categories', marker='o', ax=ax2)
    ax2.set_yscale('log')
    ax2.set_title("Publication Counts by Period and Category (Logarithmic Scale)")
    ax2.set_xlabel("Period")
    ax2.set_ylabel("Count of Papers Published (Log Scale)")
    ax2.legend(title='Category')
    ax2.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

    df['categories'] = df['categories'].str.lower().str.split(',')
    df = df.explode('categories')
    df['categories'] = df['categories'].str.strip()

    df_filtered = df[df['categories'].isin(categories)]

    counts = df_filtered.groupby(['categories', "period"]).size().unstack(fill_value=0)

    plt.figure(figsize=(25, 8)) 
    sns.heatmap(counts, annot=True, fmt="d", cmap="crest")
    plt.title("Publication Counts by Period and Category")
    plt.xlabel("Period")
    plt.xticks(rotation=45)
    plt.ylabel("Category")
    plt.yticks(rotation=0)
    plt.show()