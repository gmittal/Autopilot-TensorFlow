# GolfPilot
End to End Learning for Self-Driving Golf Carts. All datasets used [available here](https://drive.google.com/file/d/1B4k9wPRQIxCCGWMb_6O_v4cNaNqkVlyg/view?usp=sharing).

Initial code heavily based on [Sully Chen](https://github.com/SullyChen)'s implementation of [NVIDIA's *End to End Learning for Self-Driving Cars*](https://arxiv.org/pdf/1604.07316.pdf).

### Training
To train the end-to-end model, change the dataset path (if need be) in ```driving_data.py``` and run:
```
$ python train.py
```

### Testing the Model
To test the model on a local dataset, run:
```
$ python run_dataset.py
```

### Using the Model in the Wild
If you want to try and run this model using an external camera in real-time, run:
```
$ python run.py
```

### Testing a Dataset
If you want to see the ground truth steering angles for a particular dataset visualized, run:
```
$ python test_dataset.py
```

### Additional Resources
Another resource that was extremely helpful, especially in the early days, was [```udacity-driving-reader```](https://github.com/rwightman/udacity-driving-reader) for unpacking ROS format datasets. We would also like to thank Udacity for providing training and testing data and for giving advice while working on this project.
