import logging
import subprocess

def docker_compose_up(logger: logging.Logger):
    subprocess.run(
    ["docker", "compose", "up", "-d"], check=True)
    result = subprocess.run(
        ["docker", "compose", "ps", "--status", "running", "-q"],
        capture_output=True,
        text=True,
        check=True,
    )
    if result.stdout.strip():
        logger.info(f'Docker container started')
    else:
        raise RuntimeError(f"Docker container not started")

def docker_down(logger: logging.Logger):
    logger.info("Stopping Docker containers")

    result = subprocess.run(
        ["docker", "compose", "down"],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        logger.info("Docker containers stopped successfully")
    else:
        logger.error(
            f"Failed to stop Docker containers: {result.stderr.strip()}"
        )
        raise RuntimeError("Failed to stop Docker containers")