<p align="center">
    <img alt="logo" src="assets/logos/red-border.png" width="250px" align="center">
    <h1 align="center">VideoCloud</h1>
    <p align="center">
      <a href="https://travis-ci.org/paramt/videocloud"><img alt="Build Status" src="https://travis-ci.org/paramt/videocloud.svg?branch=master"></a>
      <a href="https://pypi.org/project/VideoCloud"><img alt="PyPI" src="https://img.shields.io/pypi/v/videocloud.svg"></a>
      <a href="https://requires.io/github/paramt/videocloud/requirements/?branch=master"><img src="https://requires.io/github/paramt/videocloud/requirements.svg?branch=master" alt="Requirements Status" /></a>
      <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/paramt/videocloud.svg?"></a>
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
videocloud <link to YouTube video> [filepath] [language code] [font]
```

If no filepath is given, the wordcloud will be generated as <kbd>videocloud.png</kbd> in the current directory. 
The lanuage code defaults to <kbd>en</kbd> and the fontpath defaults to [Noto Sans](assets/fonts/NotoSans).
To use a custom font, provide the HTTP link for its TTF file


## License 

All the code in this repo is licensed under the [MIT License](LICENSE) unless otherwise specified. You are free to use, modify, and distribute the source code as long as you include the original license file. [Some fonts](assets/fonts) are licensed separately under the [SIL Open Font License](https://github.com/paramt/videocloud/blob/master/assets/fonts/NotoSans/SIL%20Open%20Font%20License.txt). 
