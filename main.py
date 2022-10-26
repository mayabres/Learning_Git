import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("Almog.xlsx")
sns.lineplot(data=data, x="End frequency", y='positions')
plt.show()
