import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns

planet_masses = []
planet_radiuses = []

planet_masses.append(df["Mass"])
planet_radiuses.append(df["Radius"])

X = []
for index, planet_mass in enumerate(planet_masses):
  temp_list = [
                  planet_radiuses[index],
                  planet_mass
              ]
  X.append(temp_list)

wcss =[]  

for i in range(1,11):
  kmeans = KMeans(n_clusters = i , init = "k-means++" , random_state = 42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
