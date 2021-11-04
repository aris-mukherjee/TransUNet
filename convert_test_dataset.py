import h5py
import numpy as np
import os
from PIL import Image
import nibabel as nib

for i in range(300, 999):

    save_path = 'data/Synapse/test_vol_h5/case%s.npy.h5' % (i)
    img_path = 'Synapse_Dataset/test_set/synapse_test/DET0000%s_avg.nii' % (i)

    if os.path.isfile(img_path): 
        print('image size: %d bytes'%os.path.getsize(img_path))
        hf = h5py.File(save_path, 'a') # open a hdf5 file

        img = nib.load(img_path)
        img_np= np.array(img.dataobj)

        dset = hf.create_dataset('default', data=img_np)  # write the data to hdf5 file
        hf.close()  # close the hdf5 file
        print('hdf5 file size: %d bytes'%os.path.getsize(save_path)) 


    else:
        pass

for i in range(1000, 10000):

    save_path = 'data/Synapse/test_vol_h5/case%s.npy.h5' % (i)
    img_path = 'Synapse_Dataset/test_set/synapse_test/DET000%s_avg.nii' % (i)

    if os.path.isfile(img_path): 
        print('image size: %d bytes'%os.path.getsize(img_path))
        hf = h5py.File(save_path, 'a') # open a hdf5 file

        img = nib.load(img_path)
        img_np= np.array(img.dataobj)

        dset = hf.create_dataset('default', data=img_np)  # write the data to hdf5 file
        hf.close()  # close the hdf5 file
        print('hdf5 file size: %d bytes'%os.path.getsize(save_path)) 


    else:
        pass
 
for i in range(10002, 44903):

    save_path = 'data/Synapse/test_vol_h5/case%s.npy.h5' % (i)
    img_path = 'Synapse_Dataset/test_set/synapse_test/DET00%s_avg.nii' % (i)

    if os.path.isfile(img_path): 
        print('image size: %d bytes'%os.path.getsize(img_path))
        hf = h5py.File(save_path, 'a') # open a hdf5 file

        img = nib.load(img_path)
        img_np= np.array(img.dataobj)

        dset = hf.create_dataset('default', data=img_np)  # write the data to hdf5 file
        hf.close()  # close the hdf5 file
        print('hdf5 file size: %d bytes'%os.path.getsize(save_path)) 

        

    else:
        pass