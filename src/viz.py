import matplotlib.pyplot as plt


def plot_images(images, titles=None):
    num_images = len(images)

    if num_images == 0:
        raise ValueError("Expected at least one image to plot.")

    if titles is None:
        titles = [f"Image {index + 1}" for index in range(num_images)]

    fig, axes = plt.subplots(1, num_images, figsize=(5 * num_images, 5))

    if num_images == 1:
        axes = [axes]

    for axis, image, title in zip(axes, images, titles):
        axis.imshow(image)
        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.show()


def viz_features(images, feature_sets, titles=None, marker_size=18, color="red"):
    """Plot detected feature locations on top of the input images."""
    num_images = len(images)

    if num_images == 0:
        raise ValueError("Expected at least one image to plot.")

    if len(feature_sets) != num_images:
        raise ValueError("The number of feature sets must match the number of images.")

    if titles is None:
        titles = [f"Image {index + 1}" for index in range(num_images)]

    fig, axes = plt.subplots(1, num_images, figsize=(5 * num_images, 5))

    if num_images == 1:
        axes = [axes]

    for axis, image, feature_set, title in zip(axes, images, feature_sets, titles):
        axis.imshow(image)
        locations = feature_set.get("locations", [])

        if locations:
            x_coords, y_coords = zip(*locations)
            axis.scatter(x_coords, y_coords, s=marker_size, c=color, marker="o")

        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.show()
