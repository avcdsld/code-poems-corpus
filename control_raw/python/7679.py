def random_size_crop(src, size, min_area=0.25, ratio=(3.0/4.0, 4.0/3.0)):
    """Randomly crop src with size. Randomize area and aspect ratio"""
    h, w, _ = src.shape
    area = w*h
    for _ in range(10):
        new_area = random.uniform(min_area, 1.0) * area
        new_ratio = random.uniform(*ratio)
        new_w = int(new_area*new_ratio)
        new_h = int(new_area/new_ratio)

        if random.uniform(0., 1.) < 0.5:
            new_w, new_h = new_h, new_w

        if new_w > w or new_h > h:
            continue

        x0 = random.randint(0, w - new_w)
        y0 = random.randint(0, h - new_h)

        out = fixed_crop(src, x0, y0, new_w, new_h, size)
        return out, (x0, y0, new_w, new_h)

    return random_crop(src, size)