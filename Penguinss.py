import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Penguins Data.csv")
data.head()

sns.scatterplot(x="Culmen Length (mm)", y="Body Mass (g)", data=data)
plt.show()

sns.scatterplot(x="Culmen Depth (mm)", y="Body Mass (g)", data=data)
plt.show()

sns.pairplot(data, hue="Species")
plt.show()


plt.fill_between(data["Culmen Length (mm)"], data["Body Mass (g)"])
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()