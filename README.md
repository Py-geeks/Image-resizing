# Image-resizing
Image Resizing with Python

## Tools and Languages:
<img align="left" alt="OpenCV" width="26px" src="opencv.png" >
<img align="left" alt="VS Code" width="26px" src="visual-studio-code.png" >
<img align="left" alt="pip" width="26px" height="34px" src="pip.png" >
<img align="left" alt="Python" width="26px" src="python.png" >
<br>

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cv2 and numpy.


```bash
pip install cv2
pip install numpy
```

## Import

```python
import cv2
import numpy as np
```

## Reading image from file

```python
img = cv2.imread("cat.png")
```


## Img resizing

```python
scale_percent = 0.60
width = int(img.shape[1]*scale_percent)
height = int(img.shape[0]*scale_percent)
dim = (width,height)
```

## Implementing interpolation 
```python
resized = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
```

## Comparing original vs resized

```python
cv2.imshow('ORIGINAL',img)
cv2.imshow('RESIZED',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Images
<p align="center">
	<img src="cat.png" alt="Logo", height=250px,width=350px>
	<img src="resized.PNG" alt="Resized", height=250px,width=350px>
</p>

### Developed by
 [Ashish ku. Behera](https://github.com/ashish-max "Github Id")
