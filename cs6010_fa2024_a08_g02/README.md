## KMean Clustering

### Evaluation

1. StandardScaler

- StandardScaler produced moderate Silhouette scores of 0.171 in the dataset.
- Limitations: It might not be as effective if the data is non-normally distributed, as it doesn't address skewness.

2. MinMaxScaler

- K-Means and other algorithms performed relatively well with MinMaxScaler; for instance, K-Means achieved a Silhouette Score of 0.301, indicating decent cluster cohesion​.
- Limitations: MinMaxScaler can be sensitive to outliers and may not be suitable for data with extreme values.

3. Normalizer

- Especially beneficial for data where features are of different units or when the importance lies in the ratio of features rather than their values.
- Limitations: Not ideal for clustering tasks where absolute feature scales are relevant.

### Impact

1. StandardScaler

- Helps K-Means perform better when the data has features with different scales. This ensures that all features contribute equally to distance calculations.
- Reduces the impact of outliers by scaling features to have similar variances.
- Can distort the shape of the original distribution, potentially affecting the clustering results.

2. MinMaxScaler

- Preserves the relationships between data points, which helps when features are on drastically different scales.

3. Normalizer

- Normalizer resulted in the highest Silhouette Scores for all clustering algorithms, indicating better-defined and cohesive clusters. For example, K-Means had a Silhouette Score of 0.766
- Works well when the clustering focus is on the direction of data points rather than their absolute scale, which can be advantageous for datasets with large variations in magnitude.

### Conclusion

#### Overall

Normalizer work best with the dataset, producing the highest Silhouette Scores across all clustering algorithms. This suggests that Normalizer is effective for clustering tasks where the direction of data points is more important than their scale. However, the choice of scaler depends on the specific characteristics of the dataset and the clustering algorithm used.

1. StandardScaler:

- Is a good choice for K-Means if the data has high variance.

2. MinMaxScaler:

- Useful when data is not centered around the mean but needs normalization for clustering.

3. Normalizer

- Provided the best clustering scores in the analysis, indicating it’s effective for data needing normalization of direction rather than scale.

## Hierarchical Clustering
### Evaluation
1.  The dendrograms generated from different linkage methods (e.g., complete, average, single) consistently indicated that a cut-off at 3 clusters best captures the natural grouping of the data.
2. The Silhouette Score, which measures the cohesion and separation of clusters, was calculated for various cluster counts. The score was highest when the data was divided into 3 clusters, confirming that this configuration provides the most cohesive and well-separated clustering for the dataset.
### Impact
1. PCA: With fewer dimensions, clustering algorithms (especially computationally intensive ones like hierarchical clustering) run faster and are less affected by the curse of dimensionality. PCA relies on linear transformations and may not fully capture non-linear relationships, potentially impacting clustering quality if the data has complex structures.
2. StandardScaler: Hierarchical clustering often benefits from maintaining the natural scales of data, especially when absolute distances between points are meaningful. By standardizing, features that originally had larger ranges (e.g., DC in the forest fires dataset) lose their proportional influence, potentially diluting key differences between data points.
3. MinMaxScaler: Like StandardScaler, MinMaxScaler can distort the influence of features that originally had larger or smaller ranges, effectively equalizing all features’ importance. 
### Conclusion
-   The most effective methodology for hierarchical clustering on this dataset was to use approriately transformed data rather than aggressive scaling techniques like StandardScaler or MinMaxScaler.
-   Additionally, applying PCA helped to simplify the dataset by reducing dimensionality, which improved clustering interpretability and efficiency.

We're going to use the elbow method to determine the optimal number of clusters for the KMeans algorithm. The elbow method consists of plotting the sum of squared distances between the data points and their assigned clusters. The optimal number of clusters is the point where the sum of squared distances starts to decrease in a linear fashion.

## GMM Clustering
### Evaluation
1.  Based on the log-likelihood values (Obj Func), the model showed consistent improvement up to 3 clusters. Beyond that, the log-likelihood gains were little or fluctuating, which suggest that 3 clusters offer the most optimal and most balanced between model complexity and goodness of fit.
### Impact
1.  PCA: PCA was used to reduce the dataset to 2 principal components, enabling effective visualization of clusters.
2.  StandardScaler and MinMaxScaler:  Cluster distributions were imbalanced across four random states. Some clusters contained only a handful of points, while others dominated. Therefore, standardizing features might have overly homogenized their influence, potentially skewing cluster assignments toward outlier groups.
3.  Normalizer: Clustering with Normalizer yielded slightly more balanced distributions but showed inconsistencies across random states. This approach likely masked absolute differences between data points, resulting in less distinct cluster assignments.
### Conclusion
-   Use 3 clusters, as both log-likelihood and visual analysis supported this as the optimal number.
-   Avoid scaling methods like StandardScaler or MinMaxScaler for GMM on this specific dataset. Instead, consider using log-transformed data to preserve meaningful feature contributions.

# Reflection

This assignment provided insights into hierarchical clustering, especially its sensitivity to data preprocessing and scaling methods. We learned that using approriately transformed data could produces better cluster structures compared to aggressive scaling techniques like StandardScaler which can obscure meaningful patterns. Using dendrograms helped us understand how clusters merge and identify the optimal number of clusters, reinforcing the importance of balancing quantitative metrics like the Silhouette Score with interpretability. Applying PCA highlighted the trade-offs between dimensionality reduction and preserving data variance for clustering.

We learned about the elbow method for determining the optimal number of clusters in KMeans, which helped us identify the most suitable cluster count for our dataset. We also explored the impact of different scaling methods on clustering algorithms, such as StandardScaler, MinMaxScaler, and Normalizer. We found that the choice of scaler can significantly affect clustering results, with Normalizer producing the best clustering scores in our analysis. Additionally, we applied PCA to reduce the dimensionality of the dataset and visualize the clusters effectively.

Centroid selection is a crucial step in KMeans clustering, as it determines the initial cluster centers. We learned that KMeans is sensitive to the initial centroid positions and that multiple random starts can help improve the stability of the clustering results. By comparing the Silhouette Scores and log-likelihood values of different clustering methods, we were able to evaluate the quality of the clusters and determine the optimal number of clusters for each algorithm.

We learned about the basic math of the Gausian Mixture Model where it clusters data points based on their probability distributions. We also learned about the Expectation-Maximization algorithm, which iteratively estimates the parameters of the model to maximize the likelihood of the data.

For Gausian Mixture Model, we noticed that the selection of means, covariances, and weights of the Gaussian distributions would affect the effectiveness of the clustering algorithm (just like the selection of centroids in KMeans).

We also learned about the meaning of log-likelihood and how it can be used to evaluate the quality of the clustering model. A higher log-likelihood value indicates a better fit of the model to the data.
This assignment provided insights into hierarchical clustering, especially its sensitivity to data preprocessing and scaling methods. We learned that using approriately transformed data could produces better cluster structures compared to aggressive scaling techniques like StandardScaler which can obscure meaningful patterns. Using dendrograms helped us understand how clusters merge and identify the optimal number of clusters, reinforcing the importance of balancing quantitative metrics like the Silhouette Score with interpretability. Applying PCA highlighted the trade-offs between dimensionality reduction and preserving data variance for clustering. 

## Reflection Questions

1. What do I believe I did well on this assignment?

- We applied elbow method to determine the optimal number of clusters for the KMeans algorithm.
- We did great on exploring the data and implementing different clustering methods.  we applied different scalars and evaluated their impact on clustering methods.
- We tried different random states to ensure the stability of the clustering results. 
- We also used PCA to reduce the dimensionality of the dataset and visualize the clusters effectively.
- We did great on exploring the data and implementing different clustering methods.  we applied different scalars and evaluated their impact on clustering methods.

2. What was the most challenging part of this assignment?

- Understanding the nuances of how scaling methods like StandardScaler and MinMaxScaler interact with GMM was difficult. It was challenging to interpret why some scalers led to imbalanced cluster distributions. Choosing the optimal number of clusters was tricky, especially when different metrics like log-likelihood and Silhouette Score suggested conflicting results.
- We also found it challenging to decide which columns to drop from the dataset before applying the clustering algorithms.

3. What would have made this assignment a better experience?

- More guidance on how to evaluate GMM models beyond log-likelihood and Silhouette Scores would have helped. Examples of real-world use cases for GMM clustering might have also provided better context.

4. What do I need help with?

- We would like to have more insights on which columns to drop from the dataset before applying clustering algorithms because we know that not all columns are suitable for clustering.
- We would like to have more help on learning more about the mathematic behind GMM, sillhoutte score and log-likelihood.