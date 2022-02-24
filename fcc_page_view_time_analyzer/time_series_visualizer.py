import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
dt_parser = lambda x: pd.to_datetime(x)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'],
                 date_parser=dt_parser, index_col=['date'])

#print(len(df))
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

#print(len(df))
def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10,6))

    ax.plot(df.index, df.value)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')


    #plt.show()
    # Save image and return fig (don't change this part)
    #fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year'] = df.index.year
    df_bar['months'] = df.index.strftime('%B')

    df_bar = df_bar.groupby(['year', 'months']).agg('mean').reset_index()

    month_list = pd.date_range('2021-01', '2021-12', freq='MS').strftime('%B').tolist()

    # Draw bar plot

    fig = plt.figure(figsize=(10,6))

    sns.barplot(data=df_bar, x='year', y='value',
                hue='months', hue_order=month_list,
                palette='bright')

    plt.legend(loc='upper left')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    month_list = pd.date_range('2021-01', '2021-12', freq='MS').strftime('%b').tolist()
    # Draw box plots (using Seaborn)

    fig, (ax, bx) = plt.subplots(1,2, figsize=(14,6))

    sns.boxplot(data=df_box, x='year', y='value', ax=ax)
    sns.boxplot(data=df_box, x='month', y='value',
                order=month_list, ax=bx)

    ax.set_xlabel('Year')
    ax.set_ylabel('Page Views')
    ax.set_title('Yer-Wise Box Plot (Trend)')

    bx.set_xlabel('Month')
    bx.set_ylabel('Page Views')
    bx.set_title('Month-Wise Bos Plot (Seasonality)')

    #plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
