from PIL import Image


def resize_image(size1, size2):
    image = Image.open('test.jpeg')

    print(f"Current size : {image.size}")

    resized_image = image.resize((500, 500))

    resized_image.save('test' + str(size1)+'x'+str(size2) + '.jpeg')


size1 = int(input("Enter width: "))
size2 = int(input("Enter length: "))
resize_image(size1, size2)
