import logging

import click
from pathlib import Path
import numpy as np
from tensorflow.keras.datasets import cifar10


@click.command()
def main():
    """Download Cifar10 dataset and save to (../raw).
    """
    logger = logging.getLogger(__name__)
    logger.info('Download Cifar10 datasets and save as ')
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    logger.info(f"# of training data: {len(x_train)} \n # of test data: {len(x_test)}")
    project_dir = Path(__file__).resolve().parents[2]
    np.savez("cifar10.npz", x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()

