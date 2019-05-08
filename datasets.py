import glob
import random
import os

from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms

class ImageDataset(Dataset):
    def __init__(self, root, transforms_=None, unaligned=False, mode='train',system="windows"):
        self.transform = transforms.Compose(transforms_)
        self.unaligned = unaligned

        if system=="linux":
            self.files_A = sorted(glob.glob(os.path.join(root, '%s/A' % mode) + '/*.*'))
            self.files_B = sorted(glob.glob(os.path.join(root, '%s/B' % mode) + '/*.*'))
        else:
            self.files_A_folder=os.path.join(root,mode+'A')
            self.files_B_folder=os.path.join(root,mode+'B')
            self.files_A=sorted(os.listdir(self.files_A_folder))
            self.files_B=sorted(os.listdir(self.files_B_folder))

    def __getitem__(self, index):
        item_A = self.transform(Image.open(os.path.join(self.files_A_folder,self.files_A[index])))
        print(type(item_A))
        if self.unaligned:
            item_B = self.transform(Image.open(os.path.join(self.files_B_folder,self.files_B[random.randint(0, len(self.files_B) - 1)])))
        else:
            item_B = self.transform(Image.open(os.path.join(self.files_B_folder,self.files_B[index ])))

        return {'A': item_A, 'B': item_B}

    def __len__(self):
        return max(len(self.files_A), len(self.files_B))