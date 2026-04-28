python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load the beneficiaries dataset from a file."""
    return pd.read_excel(file_path)

def generate_trend_analysis(df):
    """Generate a time-series line plot for beneficiary trends."""
    df['Quarter'] = pd.to_datetime(df['Quarter'], format='%Y-Q%q')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Quarter', y='Total Beneficiaries', hue='Type', marker='o')
    plt.title('Quarterly Beneficiary Trends by Type')
    plt.xlabel('Quarter')
    plt.ylabel('Total Beneficiaries')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def gender_distribution_pie_chart(df):
    """Generate a pie chart for gender distribution."""
    gender_data = df.groupby('Gender')['Count'].sum()
    gender_data.plot.pie(autopct='%1.1f%%', figsize=(8, 8), startangle=140, title='Gender Distribution of Beneficiaries')
    plt.ylabel('')
    plt.show()

# Main execution
if __name__ == "__main__":
    dataset_path = 'path_to/Distribution of Benefeciaries 2022.xlsx'
    data = load_data(dataset_path)
    
    # Generate time-series analysis
    generate_trend_analysis(data)

    # Generate gender distribution pie chart
    gender_distribution_pie_chart(data)
