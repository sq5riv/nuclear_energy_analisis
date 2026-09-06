from python.get_logger import get_logger
from python import kaggle_utils
from python import docker_utils
from python import before_load_data_check

if __name__ == "__main__":
    logger = get_logger(__name__)
    data_path = kaggle_utils.data_download(logger)
#    docker_utils.docker_compose_up(logger)
    print(before_load_data_check.colum_check(data_path, logger))
#    docker_utils.docker_down(logger)
