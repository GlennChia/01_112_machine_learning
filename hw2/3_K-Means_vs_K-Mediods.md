# 3. K-Means vs K-Medoids [10 points]

What are the advantages and disadvantages of K-medoids, compared to K-means?

<u>**Advantage 1 of K-medoids - available for more contexts**</u>

Context is an important factor to determine the relevance of K-Means vs K-Medoids. There are certain scenarios which do not allow for K Means clustering and only allows K-medoids. For example, if we want to classify 2 distinct movie genres, `Horror` and `Comedy`, it does not make sense to blend them together to evaluate the "mean" (K means clustering) as there should not be a `Horror-comedy` genre since the genres themselves are vastly different. Thus, in situations where there are 2 distinct groups that should not overlap, the K-Medoids algorithm is the only one that will work effectively. 

Thus, K-medoids is more flexible and can be used with any similarity measure 

<u>**Advantage 2 of K-medoids - Cluster representation**</u>

K-medoids can provide a better centroid to represent the cluster. This is best illustrated with an example. 

For example: We have a 1-Dimensional clusters [4,5,6,7,8,3000]

If we use K-means, the mean will be 505 which does not represent the bulk of the data points which are around the smaller values.

Alternatively, if we use K-medoids, we get the centroid as 8 which is a better representation for the set as it is closer to the bulk of the points.

<u>**Disadvantage 1 of K-medoids - More expensive**</u> 

The K medoids clustering algorithm requires us to iterate through all the points and calculate the loss for each one. The loss is found by comparing this point to all the other points in the cluster. Hence, the complexity for locating a centroid is O(n<sup>2</sup>). Including locating the clusters and the number of iterations, this becomes O(i * (n<sup>2</sup> + n*k)) where i is the number of iterations and k is the number of clusters.

On the other hand, during the search for centroids, the K means algorithm does not require us to iterate through all the data points twice. Instead, we just have to iterate through the data points for each cluster to compute the mean. Hence, the complexity of this operation is O(n). Including the number of clusters and iterations will produce a complexity of O(i * (n + n * k)) which is simplified to `O(i*n*k)` 

|                                      | K-Medoids        | K-Means |
| ------------------------------------ | ---------------- | ------- |
| Complexity of computing the centroid | O(n<sup>2</sup>) | O(n)    |

 To summarize, from the table we can see that the cost for K-medoids is higher and it will take a longer time for clustering

