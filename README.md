<p align="center">
<img src="./images/inter4k.png" width="300" />
</p>

![GitHub issues](https://img.shields.io/badge/licence-CC--NC--SA-lightgrey.svg)

# Inter4K Tools
Official repository for hosting tools for creating Inter4K video interpolation dataset.

Project website: [Inter4K/index.html](https://alexandrosstergiou.github.io/datasets/Inter4K/index.html)

Paper: _AdaPool: Exponential Adaptive Pooling for Information-Retaining Downsampling_

## Requirements

- FFmpeg ([https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html))

## Dataset creation instructions

1. You will first need to download the 4K 60fps video clips (~15GB in total). Use the link [https://tinyurl.com/interUHD](https://tinyurl.com/interUHD) either through the browser or with `wget` on terminal:
```
wget https://tinyurl.com/interUHD
```

2. Clone the repository:
```
git clone git@github.com:alexandrosstergiou/Inter4K.git
```

3. Unzip the folder inside the repository:
```
unzip Inter4K.zip -d Inter4K
```

4. Perform a check to all files by running:
```
cd Inter4K/
python check.py
```

5. Finally, create the full dataset by running:
```
python resolution_changes.py
```

> ! Note: By default, the program will use 16 workers to create the dataset. If you are interested on speeding-up things (and given that you have a capable CPU) you can change the number of workers by editing [`resolution_chanes.py line #42`](https://github.com/alexandrosstergiou/Inter4K/blob/c3469f9439e85403177c12250ab75716c5b4772c/resolution_changes.py#L42). This can also be the case that a less powerful CPU is used.

## Reference

```
@article{stergiou2021adapool,
  title={AdaPool: Exponential Adaptive Pooling for Information-Retaining Downsampling},
  author={Stergiou, Alexandros and Poppe, Ronald},
  booktitle={arXiv},
  year={2021}
}
```
