# k-means-clustering
<div id="header" align="center">
  <img src="https://media.giphy.com/media/12vVAGkaqHUqCQ/giphy.gif" width="200"/>
</div>

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/sakabuana31/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" height="25px" alt="LinkedIn Badge"/>
  </a>
  <a href="mailto:sakabuana.pa@gmail.com">
  <img src="https://img.shields.io/badge/-Email-c14438?style=flat-square&logo=Gmail&logoColor=white" height="25px" alt="Email Badge">
  </a>
</div>

<h1 align="center">
  hey there
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>

### :dart: Goals :
> Customer analysis by clustering customers based on the Income and Spending they spend while shopping and determining the number of cluster data clustering.

### :newspaper: Documentation :
1. Generate sample data in [create-data.py](create-data.py) using faker with 200 data results in [input_data/sales_data.csv](input_data/sales_data.csv)
2. Determine optimum cluster number for raw data in [calculate-elbow.ipynb](calculate-elbow.ipynb) using elbow method, with the output of the elbow method results below

    ![The-Elbow-Method.png](output_data/The-Elbow-Method.png)

3. From the output above the silhouette show the best cluster number are 4
4. Create clustering data points in [k-means-cluster.ipynb]() based on similarities in their features with the results below

    ![Clustered-Mall-Using-K-Means.png](output_data/Clustered-Mall-Using-K-Means.png)

5. From the graphic output above with 4 cluster we can conclude
    - There are people that have high spend with high income which are shown in green clusters, we must maintain cluster of these people.
    - There are people that have low spend with high income which are shown in red clusters, cluster of these people is the main target of our customer.
    - There are people that have low spend with low income which are shown in yellow clusters, cluster of these people is the secondary target of our customer.
    - There are people that have low spend with high income which are shown in blue clusters, cluster of these people is easly maintain with promo.