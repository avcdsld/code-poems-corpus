def get_frames_mouth(self, detector, predictor, frames):
        """
        Get frames using mouth crop
        """
        mouth_width = 100
        mouth_height = 50
        horizontal_pad = 0.19
        normalize_ratio = None
        mouth_frames = []
        for frame in frames:
            dets = detector(frame, 1)
            shape = None
            for det in dets:
                shape = predictor(frame, det)
                i = -1
            if shape is None: # Detector doesn't detect face, just return None
                return [None]
            mouth_points = []
            for part in shape.parts():
                i += 1
                if i < 48: # Only take mouth region
                    continue
                mouth_points.append((part.x, part.y))
            np_mouth_points = np.array(mouth_points)

            mouth_centroid = np.mean(np_mouth_points[:, -2:], axis=0)

            if normalize_ratio is None:
                mouth_left = np.min(np_mouth_points[:, :-1]) * (1.0 - horizontal_pad)
                mouth_right = np.max(np_mouth_points[:, :-1]) * (1.0 + horizontal_pad)

                normalize_ratio = mouth_width / float(mouth_right - mouth_left)

            new_img_shape = (int(frame.shape[0] * normalize_ratio),
                             int(frame.shape[1] * normalize_ratio))
            resized_img = imresize(frame, new_img_shape)

            mouth_centroid_norm = mouth_centroid * normalize_ratio

            mouth_l = int(mouth_centroid_norm[0] - mouth_width / 2)
            mouth_r = int(mouth_centroid_norm[0] + mouth_width / 2)
            mouth_t = int(mouth_centroid_norm[1] - mouth_height / 2)
            mouth_b = int(mouth_centroid_norm[1] + mouth_height / 2)

            mouth_crop_image = resized_img[mouth_t:mouth_b, mouth_l:mouth_r]

            mouth_frames.append(mouth_crop_image)
        return mouth_frames