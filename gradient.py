
import sys
import struct

class ValueError(Exception):
    pass

def gradient():

    bmp_width=100
    bmp_height=100

    if len(sys.argv) != 5 :
        print(ValueError("Incorrect arguements"))

    point1=sys.argv[1]
    point2=sys.argv[2]
    bmp_file=sys.argv[4]

    try:
        # Split "10,20=10,50,255"
        coords1, colors1 = point1.split('=')
        x1_str, y1_str = coords1.split(',')
        r1_str, g1_str, b1_str = colors1.split(',')
        
        x1 = int(x1_str)
        y1 = int(y1_str)
        r1 = int(r1_str)
        g1 = int(g1_str)
        b1 = int(b1_str)
    except:
        print("Error parsing first point. Use format: x,y=r,g,b")

    try:
        coords2, colors2 = point2.split('=')
        x2_str, y2_str = coords2.split(',')
        r2_str, g2_str, b2_str = colors2.split(',')
        
        x2 = int(x2_str)
        y2 = int(y2_str)
        r2 = int(r2_str)
        g2 = int(g2_str)
        b2 = int(b2_str)
    except:
        print("Error parsing second point. Use format: x,y=r,g,b")

    
        
    print(f"Point 1: ({x1},{y1}) = ({r1},{g1},{b1})")
    print(f"Point 2: ({x2},{y2}) = ({r2},{g2},{b2})")



    # Create empty image (2D list)
    image = []
    for row in range(bmp_height): 
        current_row = []
        for col in range(bmp_width):
            
            # Calculating distances
            dx1 = col - x1
            dy1 = row - y1
            dx2 = col - x2
            dy2 = row - y2
            
            dist1 = (dx1*dx1 + dy1*dy1) ** 0.5  
            dist2 = (dx2*dx2 + dy2*dy2) ** 0.5
            
            weight1 = dist2 / (dist1 + dist2)
            weight2 = 1 - weight1
            
            # Mix colors
            r = r1 * weight1 + r2 * weight2
            g = g1 * weight1 + g2 * weight2
            b = b1 * weight1 + b2 * weight2
            
            # Clamp to 0-255
            if r < 0: r = 0
            if r > 255: r = 255
            if g < 0: g = 0
            if g > 255: g = 255
            if b < 0: b = 0
            if b > 255: b = 255
            
            current_row.append((int(r), int(g), int(b)))
        image.append(current_row)

    
# Notes for bmp
#   PIXEL ARRAY - BOTTOM ROW FIRST!
# First pixel row in file = bottom row of image
# READING BMP:
# 1. Check 'BM' signature
# 2. Read DIB header for width, height, bpp
# 3. If bpp <= 8, read color palette
# 4. Calculate row padding: ((width * bpp/8 + 3) / 4) * 4
# 5. Read pixels bottom-up, skip padding per row
# 6. Convert BGR to RGB if needed

# WRITING BMP:
# 1. Write 'BM' signature
# 2. Fill DIB header (40 bytes, positive height for bottom-up)
# 3. If bpp <= 8, write palette (256 entries max)
# 4. For each row (bottom to top):
#    - Write BGR pixels
#    - Add padding zeros to reach multiple of 4



    image = image[::-1]
    
    with open(bmp_file, 'wb') as f:
        f.write(b'BM')  # Signature
        
        
        row_size = bmp_width * 3
        padding = (4 - (row_size % 4)) % 4
        row_size_with_padding = row_size + padding
        file_size = 54 + row_size_with_padding * bmp_height
        
        f.write(struct.pack('<I', file_size)) 
        f.write(b'\x00\x00') 
        f.write(b'\x00\x00')  
        f.write(struct.pack('<I', 54)) 
        
        # DIB header (40 bytes)
        f.write(struct.pack('<I', 40))  # Header size
        f.write(struct.pack('<I', bmp_width))  # Width
        f.write(struct.pack('<I', bmp_height))  # Height
        f.write(struct.pack('<H', 1))  # Planes
        f.write(struct.pack('<H', 24))  # Bits per pixel
        f.write(struct.pack('<I', 0))  # Compression
        f.write(struct.pack('<I', 0))  # Image size
        f.write(struct.pack('<I', 2835))  # X pixels per meter
        f.write(struct.pack('<I', 2835))  # Y pixels per meter
        f.write(struct.pack('<I', 0))  # Colors used
        f.write(struct.pack('<I', 0))  # Important colors
        
        # Pixel data
        for row in image:
            for r, g, b in row:
                # BMP stores as BGR
                f.write(struct.pack('BBB', b, g, r))
            # Padding
            if padding > 0:
                f.write(b'\x00' * padding)
    
    print(f"Gradient saved to {bmp_file}")




if __name__ == "__main__":
    gradient()
