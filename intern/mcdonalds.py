# Install or update Matplotlib library
!pip install -U matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram

# Read McDonald's dataset
df = pd.read_csv("mcdonalds_dataset.csv")

# Get a glimpse of the data (first few rows and data types)
print(df.head())
print(df.info())

# Analyze customer preference for "Like" category
print(df['Like'].value_counts())

# Analyze customer age distribution
print(df['Age'].value_counts())

# Analyze customer visit frequency
print(df['VisitFrequency'].value_counts())

# Prepare data for further analysis (converting "Yes/No" to numeric values)
MD_x = df.iloc[:, 0:11].values  # Select columns 1 to 11
MD_x = (MD_x == "Yes").astype(int)  # Convert "Yes" to 1, others to 0

# Calculate average preference for each feature ("yummy", "convenient", etc.)
col_means = np.round(MD_x.mean(axis=0), 2)
print("Average preference for each feature:", col_means)

# Analyze customer demographics - Gender
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", 1  shadow=True)
plt.title("Gender Distribution")
plt.show()

# Analyze customer demographics - Age
plt.figure(figsize=(25, 8))
sns.countplot(x=df['Age'], palette="viridis")
plt.title("Age Distribution of Customers")
plt.show()

# Prepare data for model building (excluding non-binary features)
df_new = df.drop(labels=['Like', 'Age', 'VisitFrequency', 'Gender'], axis=1)
print(df_new.head())

# Encode binary features ("yummy", "convenient", etc.) using LabelEncoder
df_encoded = df_new.apply(LabelEncoder().fit_transform)
print(df_encoded.head())

# Apply PCA (Principal Component Analysis) for dimensionality reduction
pca_data = preprocessing.scale(df_encoded)  # Standardize data
pca = PCA(n_components=11)  # Number of principal components (equal to original features)
pc = pca.fit_transform(pca_data)

# Create DataFrame with principal components
names = ['PC' + str(i) for i in range(1, 12)]  # Adjust for 11 components
pf = pd.DataFrame(data=pc, columns=names)
print(pf.head())

# Analyze explained variance ratio by each principal component
print("Variance explained by each principal component:", pca.explained_variance_ratio_)

# Analyze correlation between original features and principal components
loadings = pca.components_
pc_list = ["PC" + str(i) for i in range(1, pca.n_features_ + 1)]
loadings_df = pd.DataFrame.from_dict(dict(zip(pc_list, loadings)))
loadings_df['feature'] = df_encoded.columns.values
loadings_df = loadings_df.set_index('feature')
print(loadings_df)

# Customer segmentation using K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=1234)  # Define 4 clusters
clusters = kmeans.fit_predict(df_encoded)
df['Cluster'] = clusters  # Add cluster labels to the DataFrame

# Visualize clusters using PCA
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=clusters, cmap='viridis', alpha=0.5)
plt.xlabel('PC1')  # Adjust for chosen principal components
plt.ylabel('PC2')  # Adjust for chosen principal components
plt.title('Clusters based on PCA')
plt.show()

# Hierarchical clustering using Ward's method
linkage_matrix = linkage(df_encoded, method='ward')
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix, labels=clusters)
plt.title('Hierarchical Clustering Dendrogram')