from reviews import get_reviewed_books
from mlmodel import get_accurate_knn_model

# change to the NYT bestseller list you want to develop a model for
list_name = "hardcover-fiction" 

model, num_neighbors, accuracy = get_accurate_knn_model(get_reviewed_books(list_name))