import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(df, column, bins=50, save=False, filename=None):
    sns.histplot(df[column].dropna(), bins=bins, kde=True)
    plt.title(f'Distribution of {column}')
    if save and filename:
        plt.savefig(filename)
    plt.show()
def plot_correlation_matrix(df, save=False, filename=None):
    plt.figure(figsize=(12, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    if save and filename:
        plt.savefig(filename)
    plt.show()