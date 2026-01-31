from PIL import Image, ImageChops
import os

def image_eq(image_path1, image_path2):
    try:
        img1 = Image.open(image_path1).convert("RGB")
        img2 = Image.open(image_path2).convert("RGB")

        if img1.size != img2.size:
            return False

        diff = ImageChops.difference(img1, img2)
        # print(diff.getextrema())
        return diff.getbbox() is None
    except FileNotFoundError:
        print("Error: One or both image files not found.")
        return False



def image_eq_img(image1, image_path2):
    try:
        img1 = image1.convert("RGB")
        img2 = Image.open(image_path2).convert("RGB")

        if img1.mode != img2.mode or img1.size != img2.size:
            print("Size or mode mismatch")
            return False

        diff = ImageChops.difference(img1, img2)
        #print(diff.getbbox())
       # diff.show()
        return diff.getbbox() is None
    except FileNotFoundError:
        print("Error: One or both image files not found.")
        return False

def check_with_alpha(image1, folder="letters3"):
    for letter in os.listdir(folder):
        subfolder_path = os.path.join(folder, letter)

        if not os.path.isdir(subfolder_path):
            continue

        files = os.listdir(subfolder_path)
        if not files:
            continue
        for image in files:
            # print(image)
            if image_eq_img(image1, os.path.join(subfolder_path, image)):
                return letter  # return the folder name (the letter)

    return None  # no match found


from PIL import Image, ImageChops
import os

def check_with_similarity(crop, training_dir="letters3", threshold=0.7):
    def image_similarity(img1, img2):

        img1 = img1.convert("RGB")
        img2 = img2.convert("RGB")

        if img1.size != img2.size:
            img2 = img2.resize(img1.size)

        diff = ImageChops.difference(img1, img2)
        histogram = diff.histogram()

        squares = (value * (idx % 256) ** 2 for idx, value in enumerate(histogram))
        sum_of_squares = sum(squares)
        rms = (sum_of_squares / float(img1.size[0] * img1.size[1])) ** 0.5

        return max(0.0, 1.0 - rms / 255.0)

    best_letter = None
    best_score = 0

    # Loop through all letters
    for letter in os.listdir(training_dir):
        letter_dir = os.path.join(training_dir, letter)
        if not os.path.isdir(letter_dir):
            continue

        for file in os.listdir(letter_dir):
            file_path = os.path.join(letter_dir, file)
            try:
                training_img = Image.open(file_path)
            except:
                continue

            score = image_similarity(crop, training_img)
            if score > best_score:
                best_score = score
                best_letter = letter

    if best_score >= threshold:
        return [best_letter, best_score]
    return [best_letter, best_score]

