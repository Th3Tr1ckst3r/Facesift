<p align="center">
  <img src="https://i.imgur.com/YCWFdAH.png" alt="Facesift Logo" width="300">
</p>

# Facesift

[![License](https://img.shields.io/badge/License-GPL%203.0%20with%20AGPL%203.0-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Th3Tr1ckst3r/Facesift)](https://github.com/Th3Tr1ckst3r/Facesift/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Th3Tr1ckst3r/Facesift)](https://github.com/Th3Tr1ckst3r/Facesift/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/Th3Tr1ckst3r/Facesift)](https://github.com/Th3Tr1ckst3r/Facesift/issues)

## About

A lightweight, cross-platform, & accurate image sorter with facial recognition capabilities.

## Why Use Facesift?

Facesift comes in handy for a variety of reasons. Wether your doing digital forensics, or just backing up only
important images off of your phone. It allows you to take a single image, & perform facial recognition scans on files,
folders, directories, you name it. Quickly, & efficiently.

## Features

- Find full matching images, & differentiating images.
- Output all matching, or differentiating images to a specific directory with ease.
- Automatically verifies image data with Magic.
- Automatically, & efficiently use facial recognition [face_recognition](https://pypi.org/project/face-recognition/) library.
- Automatic face detection works efficiently, even when sampling against a group photo.

## To-Do

- [ ] Add multiprocessing optionally.
- [x] Add pre-compiled Linux, & Windows binaries.
- [ ] Add demo video.
- [ ] Add a GUI(graphical user interface) optionally.

## Screenshots

This is the command line(CLI) interface for Facesift. Its meant to be easy, & minimal.

![Facesift_CLI](https://i.imgur.com/uM3JyJO.png)

## Installation Notice

Facesift uses Python3 natively, so you will need to have it installed before proceeding. Once you have done that
you can follow the steps below. Alternatively, I'll also be releasing binaries for Linux, & hopefully Window.

## Required Libraries

To use Facesift, the following Python3 libraries will need to be installed. You can install them using the Python package manager `pip`.
Facesift utilizes the latest Python 3.11 so compatibility wont be an issue. Below are the installation
instructions for each library:

```bash
# Face Recognition (face_recognition)
pip install face_recognition

# Python-Magic (magic)
pip install python-magic

# Argparse (argparse)
pip install argparse

# Pillow (PIL)
pip install Pillow
```

With these libraries installed, you can proceed.

<a name="Contributors"></a>
## Contributors

<p align="center">
    <a href="https://github.com/Th3Tr1ckst3r"><img src="https://avatars.githubusercontent.com/u/21149460?v=4" width=75 height=75></a>
</p>


I welcome you to contribute code to Facesift, and thank you for your contributions, feedback, and support.

