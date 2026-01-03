"""
This program moves all images (png, jpg, gif) from the ROOT DIR to the `attachments` DIR for better organization, of 
the VAULT. 
Gero Zayas - JAN 2025 
"""

from pathlib import Path
import glob
import shutil
from loguru import logger
from typing import List
from rich import print

# ==============================================================================
# EXCEPTIONS
# ==============================================================================
class NoImagesFoundWarning(Exception):
    pass

# ==============================================================================
# CONSTANTS
# ==============================================================================
ROOT_DIR = Path.cwd()

logger.info(ROOT_DIR)

# ==============================================================================
# Functions
# ==============================================================================

def get_all_images(root_dir: Path) -> List[str]:
    logger.info("Getting all the images")
    try:
        images =    list(root_dir.glob("*.png")) + \
                    list(root_dir.glob("*.jpg")) + \
                    list(root_dir.glob("*.jpeg")) + \
                    list(root_dir.glob("*.webm")) + \
                    list(root_dir.glob("*.webp")) + \
                    list(root_dir.glob("*.gif"))

        logger.info("🖼️ IMAGES FOUND:")
        logger.info(images)
        return images
    
    except Exception as e:
        logger.error(e)
    
    return []


def move_images_to_destination(*, elements_to_move: list, from_dir: Path, to_dir: Path):
    if not elements_to_move or elements_to_move == []:
        logger.info("🟡 NO IMAGES FOUND.")
        return

    logger.info(f"Checking if {to_dir} exists, if not, creating it")
    Path.mkdir(to_dir, exist_ok=True)

    counter = 0
    logger.info(f"Iterating over each element to move it to {to_dir}")
    for e in elements_to_move:
        try:
            logger.info(f"➡️ Moving element: {e}")
            shutil.move(from_dir / e, to_dir / e)
            counter += 1
        except Exception as e:
            logger.error(f"🔴 Error moving element {e}")
    logger.info(f"✅ Moved {counter} elements from {from_dir} to {to_dir}")

def main():
    images: list = get_all_images(ROOT_DIR)
    if not images:
        logger.info("🟡 NO IMAGES FOUND.")
        exit()
    move_images_to_destination(elements_to_move = images, from_dir = ROOT_DIR, to_dir = Path("attachments"))

if __name__ == '__main__':
    main()