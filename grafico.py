import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("iris")

# Plot
sns.scatterplot(x="sepal_length", y="sepal_width", data=data, hue="species")
plt.title("Scatter Plot with Seaborn")
plt.show()