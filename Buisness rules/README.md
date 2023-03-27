

# Business rules voor Recommendation Engine

In this program we recommend product to the user based on the products they have in their cart (content_filtering.py)), or based on their profile(collab_filtering.py).

If you want to run this file, make sure to have installed the full database of the op is op voordeelshop and make sure that you have created the tables in recommendations.sql to make the code insert values into the databse. When you've done this you can continue:

To use content_filtering, simply run the content_filtering.py add in a profile_id to keep track of the productst that were recommended. Standard profile is 5a393d68ed295900010384ca. Then enter the product (or products) where you want recommendations on.

To use collab_filtering, simply run the collab_filtering.py and add in a desired profile_id. Standard is profile: 5a393d68ed295900010384ca, one's you've done that continue with the program and let it's do it's magic. After a couple seconds the recommendations are ready in the collab_recommendations table. 
