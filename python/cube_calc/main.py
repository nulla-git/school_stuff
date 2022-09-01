#Blake Reneau 09/01/2022
#a simple volume and surface area calculator for cubes

length_tb = int(input("what is top or bottom length? "))
width_tb = int(input("what is top or bottom width? "))
height_fb = int(input("what is front or back height? "))
width_fb = int(input("what is front or back width? "))
hight_lr = int(input("what is front or back height? "))
width_lr = int(input("what is front or back width? "))

surface_area = (((length_tb * width_tb) * 2) + ((width_fb * height_fb) * 2) + ((width_fb * height_fb) * 2))

print("volume is:",width_tb * length_tb * height_fb) 
print("surface area is:",surface_area)
