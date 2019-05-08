import os
import glob
from PIL import Image
from datasets import ImageDataset
import torchvision.transforms as transforms

root="datasets/apple2orange"
mode="train"
p=os.path.join(root,'%s/A' % mode)

image_folder=os.path.join(root,mode+'A')
image_path=os.listdir(os.path.join(root,mode+'A'))


d=ImageDataset(root)


img=Image.open(os.path.join(image_folder,image_path[10 % 1019]))
print(img)
l=list(range(1,20))
print(l[3%20])
print(l[2])
print(d[1])
