import rasterio
import numpy as np


def calculate_iou(ground_truth_path, prediction_path):
    """ Calculate the intersection over union of two raster images.
    Args:
        ground_truth_path (str): Path to the ground truth raster image.
        prediction_path (str): Path to the prediction raster image.
    Returns:
        float: The intersection over union of the two raster datasets.
    """
    with rasterio.open(ground_truth_path) as ground_truth_dataset:
        with rasterio.open(prediction_path) as prediction_dataset:
            ground_truth_array = ground_truth_dataset.read(1)
            prediction_array = prediction_dataset.read(1)
            intersection = np.logical_and(ground_truth_array, prediction_array)
            union = np.logical_or(ground_truth_array, prediction_array)
            iou = np.sum(intersection) / np.sum(union)
            return iou


iou = calculate_iou('IS002_GT.tif', 'IS002_NDSI.tif')
