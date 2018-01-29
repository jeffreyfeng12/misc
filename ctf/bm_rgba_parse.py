from PIL import Image

img1 = Image.open('bond.png')
rgb_img = img1.convert('RGB')

width, height = rgb_img.size

r_val = []
g_val = []
b_val = []

for x in range(width):
    for y in range(height):
        r, g, b = img1.getpixel((x,y))
        
        r_val.append(r)
        g_val.append(g)
        b_val.append(b)

img2 = Image.open('bondc.png')

rc_val = []
gc_val = []
bc_val = []
ac_val = []

for x in range(width):
    for y in range (height):
        r1, g1, b1, a1 = img2.getpixel((x,y))
        
        rc_val.append(r1)
        gc_val.append(g1)
        bc_val.append(b1)
        ac_val.append(a1)
        
pixels = 700*524
result = ""
diff = ""
max = 0

for i in range(0, pixels-1):
    r_diff = r_val[i] - rc_val[i]
    g_diff = g_val[i] - gc_val[i]
    b_diff = b_val[i] - bc_val[i]

    if (r_diff != 0 or g_diff != 0 or b_diff != 0):
        if r_diff > max:
            max = r_diff
        if g_diff > max:
            max = g_diff
        if b_diff > max:
            max = b_diff
print max
            