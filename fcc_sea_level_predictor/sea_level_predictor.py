import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    #print(df.info())
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    results1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2051, 1)

    print(len(x1))
    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    results2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = np .arange(df2['Year'].min(), 2051, 1)

    plt.plot(x1, x1 * results1.slope + results1.intercept)
    plt.plot(x2, x2 * results2.slope + results2.intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    #plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()