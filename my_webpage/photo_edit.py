# The functions take the images stored in the database and formats their sizes before displaying
# them as either the portfolio cover image on the home page or the image on the porfolio details page.
# urllib.request.urlretrieve is used to convert and save the url of the image to a jpeg. The saved jpeg
# is then resized for either the home page or portfolio details page.Is this still needed?


from PIL import Image
import urllib.request


def portfolio_item_image(img_one, img_two):
    """Convert the image urls from database and store them as jpeg. Resize the save jpeg to fit portfolio item on portfolio details page"""
    urllib.request.urlretrieve(
        f"http://127.0.0.1:8000{img_one}", "my_webpage\static\webpage\pic-uploads\original-img-one.jpg")
    raw_image_one = Image.open(
        "my_webpage\static\webpage\pic-uploads\original-img-one.jpg")

    urllib.request.urlretrieve(
        f"http://127.0.0.1:8000{img_two}", "my_webpage\static\webpage\pic-uploads\original-img-two.jpg")
    raw_image_two = Image.open(
        "my_webpage\static\webpage\pic-uploads\original-img-two.jpg")

    new_width = 550
    new_height = 300

    new_image_one = raw_image_one.resize((new_width, new_height))
    new_image_two = raw_image_two.resize((new_width, new_height))

    new_image_one.save("my_webpage\static\webpage\pic-uploads\image-one.jpg")
    new_image_two.save("my_webpage\static\webpage\pic-uploads\image-two.jpg")
    return
