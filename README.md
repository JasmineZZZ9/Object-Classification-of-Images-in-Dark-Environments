# Object-Classification-of-Images-in-Dark-Environments
It's a final project of CS545 conducted by Mingjie Zeng, Shuwen Liu, and Yang Wu.

The project contains three parts:
- image enhencement : contains a folder analysis pics, analyze.py, dog_prob.csv, imageprocessing-Retinex.py, and imageprocessing_HDR.ipynb.
  - analysis pics folder: contains the pics used in the report
  - analyze.py & dog_prob.csv: analyze the results of Retinex methods
  - imageprocessing-Retinex.py: code for Retinex based methods
  - imageprocessing_HDR.ipynb: code for SDR to HDR

- Model_training.py & model_best.pth.tar: 
  - code for training model and the output model
  
- detect.py & evaluation.ipynb :
  - detect.py: get the prediction results of every image, creating prediction_result.xlsx
  - evaluation.ipynb: input the file get by detect.py, getting the accuracy results for model

This is the link of our image data, including the original dark image and processed images:
https://drive.google.com/drive/folders/15vJClOcllwb5Qh71M0zDP55IxRvz14eq?usp=sharing

