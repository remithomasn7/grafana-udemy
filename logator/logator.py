import logging
import time
import random

# Configuration fichier + console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.StreamHandler(),  # console (stdout)
        logging.FileHandler("/var/log/logator.log")  # fichier dans le conteneur
    ]
)

levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
messages = {
    logging.DEBUG: "Debugging app state",
    logging.INFO: "Application is running smoothly",
    logging.WARNING: "Minor issue detected",
    logging.ERROR: "Something went wrong",
    logging.CRITICAL: "Critical failure!"
}

while True:
    level = random.choice(levels)
    logging.log(level, messages[level])
    time.sleep(1)
