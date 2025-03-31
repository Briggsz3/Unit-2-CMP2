from PIL import Image, ImageFilter

Williams_car = Image.open(r"C:\Users\briggsz_wlhs\Documents\Coding II\Unit-2-CMP2\lesson 6\Williams_FW14B.jpg")

Williams_blurry = Williams_car.filter(ImageFilter.GaussianBlur(50))
Williams_blurry.save("Williams_car.jpg")
Williams_blurry.show()


Williams_rotate = Williams_car.rotate(-90)
Williams_rotate.show()