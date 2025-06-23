import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_social_ads.csv")

# 1. Purchase Distribution
sns.countplot(data=df, x='Purchased')
plt.title("Purchase Distribution")
plt.savefig("purchase_distribution.png")
plt.clf()

# 2. Age Distribution by Purchase
sns.histplot(data=df, x='Age', hue='Purchased', multiple='stack')
plt.title("Age vs Purchase")
plt.savefig("age_vs_purchase.png")
plt.clf()

# 3. Salary vs Purchase
sns.histplot(data=df, x='EstimatedSalary', hue='Purchased', multiple='stack')
plt.title("Estimated Salary vs Purchase")
plt.savefig("salary_vs_purchase.png")
plt.clf()

# 4. Age Group Purchase Rate
grouped = df.groupby('AgeGroup')['Purchased'].mean().reset_index()
sns.barplot(data=grouped, x='AgeGroup', y='Purchased')
plt.title("Purchase Rate by Age Group")
plt.ylabel("Purchase Rate")
plt.savefig("agegroup_purchase_rate.png")
