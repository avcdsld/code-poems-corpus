def get_data(img_path):
    """get the (1, 3, h, w) np.array data for the supplied image
                Args:
                    img_path (string): the input image path

                Returns:
                    np.array: image data in a (1, 3, h, w) shape

    """
    mean = np.array([123.68, 116.779, 103.939])  # (R,G,B)
    img = Image.open(img_path)
    img = np.array(img, dtype=np.float32)
    reshaped_mean = mean.reshape(1, 1, 3)
    img = img - reshaped_mean
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 1, 2)
    img = np.expand_dims(img, axis=0)
    return img