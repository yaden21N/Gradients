# Gradient Image Generator

This program creates a beautiful gradient image in BMP format by blending colors between two points.

## What It Does

The program generates a 100x100 pixel image where colors smoothly transition between two points you specify. Each point has:
- A position (x, y coordinates)
- A color (red, green, blue values)

The program calculates the distance from each pixel to both points and blends the colors based on how close the pixel is to each point. Pixels closer to the first point will be more like the first color, and pixels closer to the second point will be more like the second color.

## How to Use

Run the program from the command line with 4 arguments:

```bash
python gradient.py <point1> <point2> <output_file>
```

### Arguments:
1. **point1**: First point in format `x,y=r,g,b` (coordinates and color)
2. **point2**: Second point in format `x,y=r,g,b` (coordinates and color)
3. **output_file**: Name of the BMP file to create (e.g., `image.bmp`)

### Example:
```bash
python gradient.py 10,20=255,0,0 90,80=0,0,255 image.bmp
```

This creates a gradient from:
- Point at (10, 20) with red color (255, 0, 0)
- Point at (90, 80) with blue color (0, 0, 255)

## Output

The program creates a BMP image file with a smooth color gradient blending between your two specified points and colors.
