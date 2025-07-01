def add_snow(img, snow_point, brightness_coeff):
    """Bleaches out pixels, mitation snow.

    From https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library

    Args:
        img:
        snow_point:
        brightness_coeff:

    Returns:

    """
    non_rgb_warning(img)

    input_dtype = img.dtype
    needs_float = False

    snow_point *= 127.5  # = 255 / 2
    snow_point += 85  # = 255 / 3

    if input_dtype == np.float32:
        img = from_float(img, dtype=np.dtype('uint8'))
        needs_float = True
    elif input_dtype not in (np.uint8, np.float32):
        raise ValueError('Unexpected dtype {} for RandomSnow augmentation'.format(input_dtype))

    image_HLS = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    image_HLS = np.array(image_HLS, dtype=np.float32)

    image_HLS[:, :, 1][image_HLS[:, :, 1] < snow_point] *= brightness_coeff

    image_HLS[:, :, 1] = clip(image_HLS[:, :, 1], np.uint8, 255)

    image_HLS = np.array(image_HLS, dtype=np.uint8)

    image_RGB = cv2.cvtColor(image_HLS, cv2.COLOR_HLS2RGB)

    if needs_float:
        image_RGB = to_float(image_RGB, max_value=255)

    return image_RGB