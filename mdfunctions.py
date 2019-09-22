import math
At step 0 PE is -2099.29  KE is 1532.51 TE is -566.78
At step 10 PE is -2096.18  KE is 1529.40 TE is -566.78
At step 20 PE is -2087.13  KE is 1520.34 TE is -566.79
# Function to produce distance between two list points
def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
# Function to produce square magnitude of vector
def sqmag(a):
    return (a[0]**2+a[1]**2+a[2]**2)
# Function to return unit vector pointing between two points
def vector(a,b):
    r=dist(a,b)
    x=(a[0]-b[0])/r
    y=(a[1]-b[1])/r
    z=(a[2]-b[2])/r
    return [x,y,z]