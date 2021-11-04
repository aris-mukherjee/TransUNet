import h5py
import numpy as np
import os
from PIL import Image
import nibabel as nib
from sklearn.preprocessing import MinMaxScaler
from numpy import save

sample_counter = 0
    
for j in range(100, 1000):

    img_path = '/scratch-second/arismu/Master_Thesis_Codes/My_TransUNet/synapse_train/DET0000%s_avg.nii' % (j)
    
    if os.path.isfile(img_path): 
        print('image size: %d bytes'%os.path.getsize(img_path))
    

        img = nib.load(img_path)
        img_np= np.array(img.dataobj)
        print(img_np)

        img_np_clipped = np.ndarray.clip(img_np, -125, 275)

        
        img_np_norm = (img_np_clipped - np.min(img_np_clipped))/(np.max(img_np_clipped)- np.min(img_np_clipped))
        
        shape = np.shape(img_np_norm)
        

        list_2D_pil = []
        list_2D_np = []

        sample_counter = sample_counter + 1

        for i in range(shape[2]):
            img_2D = Image.fromarray(img_np_norm[:, :, i])  #obtain 2D PIL Images
            list_2D_pil.append(img_2D)
            list_2D_np = np.array(list_2D_pil[i]) #convert pil image to numpy array
            np.savez('/scratch-second/arismu/Master_Thesis_Codes/My_TransUNet/data/Synapse/train_npz/case%s_slice%s' % (sample_counter, i), list_2D_np[i])
        
    
    else:
        pass

for j in range(1000, 10000):

    img_path = '/scratch-second/arismu/Master_Thesis_Codes/My_TransUNet/synapse_train/DET000%s_avg.nii' % (j)

    if os.path.isfile(img_path): 
        print('image size: %d bytes'%os.path.getsize(img_path))
    

        img = nib.load(img_path)
        img_np= np.array(img.dataobj)
        print(img_np)

        img_np_clipped = np.ndarray.clip(img_np, -125, 275)

        
        img_np_norm = (img_np_clipped - np.min(img_np_clipped))/(np.max(img_np_clipped)- np.min(img_np_clipped))
        
        shape = np.shape(img_np_norm)

        list_2D_pil = []
        list_2D_np = []

        sample_counter = sample_counter + 1

        for i in range(shape[2]):
            img_2D = Image.fromarray(img_np_norm[:, :, i])  #obtain 2D PIL Images
            list_2D_pil.append(img_2D)
            list_2D_np = np.array(list_2D_pil[i]) #convert pil image to numpy array
            np.savez('/scratch-second/arismu/Master_Thesis_Codes/My_TransUNet/data/Synapse/train_npz/case%s_slice%s' % (sample_counter, i), list_2D_np[i])
            
    
    else:
        pass



for j in range(10000, 45000):

    img_path = '/scratch-second/arismu/Master_Thesis_Codes/My_TransUNet/synapse_train/DET00%s_avg.nii' % (j)

    if os.path.isfile(img_path): 
        print('image size: %d bytes'%os.path.getsize(img_path))
    

        img = nib.load(img_path)
        img_np= np.array(img.dataobj)
        print(img_np)

        img_np_clipped = np.ndarray.clip(img_np, -125, 275)

        
        img_np_norm = (img_np_clipped - np.min(img_np_clipped))/(np.max(img_np_clipped)- np.min(img_np_clipped))
        
        shape = np.shape(img_np_norm)

        list_2D_pil = []
        list_2D_np = []

        sample_counter = sample_counter + 1

        for i in range(shape[2]):
            img_2D = Image.fromarray(img_np_norm[:, :, i])  #obtain 2D PIL Images
            list_2D_pil.append(img_2D)
            list_2D_np = np.array(list_2D_pil[i]) #convert pil image to numpy array
            np.savez('/scratch-second/arismu/Master_Thesis_Codes/My_TransUNet/data/Synapse/train_npz/case%s_slice%s' % (sample_counter, i), list_2D_np[i])
            
    
    else:
        pass

print(f"Total: {sample_counter} samples")

