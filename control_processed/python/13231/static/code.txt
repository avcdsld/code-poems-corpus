def eval_or_save_inference_results(self, results, dataset, output=None):
        """
        Args:
            results (list[dict]): the inference results as dicts.
                Each dict corresponds to one __instance__. It contains the following keys:

                image_id (str): the id that matches `load_inference_roidbs`.
                category_id (int): the category prediction, in range [1, #category]
                bbox (list[float]): x1, y1, x2, y2
                score (float):
                segmentation: the segmentation mask in COCO's rle format.

            dataset (str): the name of the dataset to evaluate.
            output (str): the output file to optionally save the results to.

        Returns:
            dict: the evaluation results.
        """
        continuous_id_to_COCO_id = {v: k for k, v in COCODetection.COCO_id_to_category_id.items()}
        for res in results:
            # convert to COCO's incontinuous category id
            res['category_id'] = continuous_id_to_COCO_id[res['category_id']]
            # COCO expects results in xywh format
            box = res['bbox']
            box[2] -= box[0]
            box[3] -= box[1]
            res['bbox'] = [round(float(x), 3) for x in box]

        assert output is not None, "COCO evaluation requires an output file!"
        with open(output, 'w') as f:
            json.dump(results, f)
        if len(results):
            # sometimes may crash if the results are empty?
            return COCODetection(cfg.DATA.BASEDIR, dataset).print_coco_metrics(output)
        else:
            return {}