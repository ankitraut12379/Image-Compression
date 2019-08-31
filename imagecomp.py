from PIL import Image
import math

#Coordinates of the nodes.
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Defining a class for holding Pixels for each node. 
class Pixel(object):
    def __init__(self, color = [0, 0, 0], 
            topLeft = Point(0, 0), 
            bottomRight = Point(0, 0)):
        self.R = color[0]
        self.G = color[1]
        self.B = color[2]
        self.topLeft = topLeft
        self.bottomRight = bottomRight
 
#Implementing the Quad-tree using arrays. 
class quadtree():
    def __init__(self, image):
 
        # Total number of nodes of tree.
        self.size = 0
 
        # Store image pixelmap.
        self.image = image.load()
 
        # Array of nodes.
        self.tree = []
        self.x = image.size[0]
        self.y = image.size[1]
 
        # Total number of leaf nodes.
        size = image.size[0] * image.size[1]
 
        # Count the number of nodes.
        while(size >= 1):
            self.size += size
            size /= 4
            size=int(size)
 
        size = image.size[0] * image.size[1]
 
        # Initializing the array elements.
        for i in range(self.size):
            self.tree.append(Pixel())
 
        # Store leaves into the array first.
        count = 0
        for i in range(image.size[0] - 1, 0, -2):
            for j in range(image.size[1] - 1, 0, -2):
                self.tree[self.size - 1 - 4 * count] = Pixel(self.image[i, j], 
                        Point(i, j), 
                        Point(i, j))
                self.tree[self.size - 2 - 4 * count] = Pixel(self.image[i, j - 1], 
                        Point(i, j - 1),
                        Point(i, j - 1))
                self.tree[self.size - 3 - 4 * count] = Pixel(self.image[i - 1, j], 
                        Point(i - 1, j), 
                        Point(i - 1, j))
                self.tree[self.size - 4 - 4 * count] = Pixel(self.image[i - 1, j - 1], 
                        Point(i - 1, j - 1), 
                        Point(i - 1, j - 1))
                count += 1
 
        # Then calculate and create parent nodes.
        for i in range(self.size - 4 * count - 1, -1, -1):

            self.tree[i] = Pixel(
                [(self.tree[4 * i + 1].R + self.tree[4 * i + 2].R + self.tree[4 * i + 3].R + self.tree[4 * i + 4].R) / 4,
                 (self.tree[4 * i + 1].G + self.tree[4 * i + 2].G + self.tree[4 * i + 3].G + self.tree[4 * i + 4].G) / 4,
                 (self.tree[4 * i + 1].B + self.tree[4 * i + 2].B + self.tree[4 * i + 3].B + self.tree[4 * i + 4].B) / 4],
                self.tree[4 * i + 1].topLeft,
                self.tree[4 * i + 4].bottomRight)
        

    #Takes the compression level as input and creates a new image.
    def disp(self, level):
        start = 0
 
        # Calculating the position of starting node of height.
        for i in range(0, level):
            start = 4 * start + 1
 
        # Ends the code if invalid height (Compression level) is given.
        if (start > self.size):
            print('Invalid level; Please enter a lower compression level.')
            return
 
        # Creates a new image.
        img = Image.new("RGB", (self.x, self.y), "black")
        pixels = img.load()
 
        # Moving from starting to the last node at the given height.
        for i in self.tree[start : 4 * start]:
            x1 = i.topLeft.x
            y1 = i.topLeft.y
            x2 = i.bottomRight.x
            y2 = i.bottomRight.y
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    # Sets colour at each point.
                    pixels[x, y] = (int(0), int(0), int(0))
 
        # Displays the new image.
        img.show();

        #Saves the new image in the local directory.
        img.save('CompressedImage.jpg')



def main():

    I=Image.open("Image.jpg")
    Tree=quadtree(I)        
    Tree.disp(8)

if __name__=="__main__":
    main()
