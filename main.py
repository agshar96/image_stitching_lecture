from src import extract_features, read_images, extract_descriptors, get_matches
from src.viz import plot_images, viz_features

# Read the images
images = read_images(
    [
        "input_images/scene1_a.jpg",
        "input_images/scene1_b.jpg",
    ]
)
# Plot the images just for basic test
plot_images(images)
