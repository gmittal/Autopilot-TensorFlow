# GolfPilot
End to End Learning for Self-Driving Golf Carts. All datasets used [available here](https://drive.google.com/file/d/1B4k9wPRQIxCCGWMb_6O_v4cNaNqkVlyg/view?usp=sharing).

Initial code heavily based on [Sully Chen](https://github.com/SullyChen)'s implementation of [NVIDIA's *End to End Learning for Self-Driving Cars*](https://arxiv.org/pdf/1604.07316.pdf).

### Training
To train the end-to-end model, change the dataset path (if need be) in ```driving_data.py``` and run:
```
$ python train.py
```

### Testing a Dataset