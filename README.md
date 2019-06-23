<p align="center">
    <img alt="logo" src="assets/logos/red-border.png" width="250px" align="center">
    <h1 align="center">VideoCloud</h1>
    <p align="center">
      <a href="https://pypi.org/project/VideoCloud"><img alt="PyPI" src="https://img.shields.io/pypi/v/videocloud.svg"></a>
      <a href="https://requires.io/github/paramt/videocloud/requirements/?branch=master"><img src="https://requires.io/github/paramt/videocloud/requirements.svg?branch=master" alt="Requirements Status" /></a>
      <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/paramt/videocloud.svg"></a>
    </p>
    <h4 align="center">Generate word clouds from YouTube videos</h4>
</p>

## Installation

```
pip install videocloud
```

*Note: A C compiler is required for the installation process.*

## Usage

```
videocloud <link to youtube video> [filepath]
```
If no filepath is given, the wordcloud will be generated in `./videocloud.png`
