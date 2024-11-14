from app.tasks import add
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    for i in range(10000):
        logger.debug(f"calling task {i}...")
        add.delay(4, 4)


if __name__ == "__main__":
    main()
