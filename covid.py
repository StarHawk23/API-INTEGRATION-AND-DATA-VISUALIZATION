import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Fetching data from the API
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
data = response.json()

# Extract top 10 countries with highest cases
top_countries = sorted(data, key=lambda x: x['cases'], reverse=True)[:10]

# Prepare data for plotting
countries = [country['country'] for country in top_countries]
cases = [country['cases'] for country in top_countries]
deaths = [country['deaths'] for country in top_countries]

# Visualization using seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x=countries, y=cases, palette='coolwarm')
plt.title("Top 10 Countries by COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Optional: Add another plot for deaths
plt.figure(figsize=(12, 6))
sns.barplot(x=countries, y=deaths, palette='magma')
plt.title("Top 10 Countries by COVID-19 Deaths")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
