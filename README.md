# Image-Compression
Goal of this project was to achieve user defined level of compression for any given image.


Used Quad Tree datastructure to store the RGB values of all the pixels at leaf nodes and recursively filled the parent nodes by averaging the value of group of (here 4) nodes of the current level until the root node.


Level of compression can be chosen by user by selecting the level in the tree, thus all the leaves will have their RGB values as the value of their ancestor node of the selected level.


And thus the image is rendered with this updated RGB values of pixels.

******************************************************************************************************************************************************************************
Quadtrees are used in image compression, where each node contains the average colour of each of its children. The deeper you traverse in the tree, the more the detail of the image.
Quadtrees are also used in searching for nodes in a two-dimensional area. 
