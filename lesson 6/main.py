from PIL import Image, ImageFilter, ImageEnhance

orange_cat = Image.open(r"lesson 6\orange_cat.jpg")

blurry_cat = orange_cat.filter(ImageFilter.GaussianBlur(20))
blurry_cat.save("blurry_cat.jpg")
blurry_cat.show()
#bw_cat = ImageEnhance.Color(orange_cat).enhance(0) # 0 takes away all color
# can't do save and .show at the same time
# if you wanted to save it would be .save(r"path")
bright_cat = ImageEnhance.Color(orange_cat).enhance(10)
#bw_cat.show()
bright_cat.show()