import logging
import kagglehub

def data_download(logger: logging.Logger) -> str:
    """
    Download kaggle dataset
    :return path
    """
    logger.info('Downloading kaggle dataset')
    path = kagglehub.dataset_download("alistairking/nuclear-energy-datasets",
                                      output_dir="./data")
    logger.info(f'Dataset dowlnowaded to {path}')
    return path

