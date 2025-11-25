from PIL import Image
img = Image.open("download.jpg")
crop_img = (100, 50, 400, 300)
cropped_img = img.crop(crop_img)
cropped_img.save("cropped_pic.jpg")
print("Image Cropped And Saved")
