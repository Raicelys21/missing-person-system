import os 

KNOWN_IMAGES_FOLDER_PATH = "C:/Users/Raicelys Suero/Documents/CST-10/Prog. Web Avanz/Missing Person System/missingperson/media/gallery"
KNOWN_IMAGES_FOLDER_PATH2 = "C:/Users/Raicelys Suero/Documents/CST-10/Prog. Web Avanz/Missing Person System/missingperson/media/identify"


def load_images() -> tuple[str, str]:
    image_files = os.listdir(KNOWN_IMAGES_FOLDER_PATH)
    images_path: list[str] = []

    image_files2 = os.listdir(KNOWN_IMAGES_FOLDER_PATH2)
    images_path2: list[str] = []

    for file in image_files:
        images_path.append(f"{KNOWN_IMAGES_FOLDER_PATH}/{file}")
        images_path.append(f"{KNOWN_IMAGES_FOLDER_PATH2}/{file}")

    return (image_files, images_path, image_files2, images_path2)

result = load_images()

print(result)