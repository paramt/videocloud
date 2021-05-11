import setuptools

long_description = '''
# VideoCloud
[![Build Status](https://travis-ci.org/paramt/videocloud.svg?branch=master)](https://travis-ci.org/paramt/videocloud)
[![License](https://img.shields.io/github/license/paramt/videocloud.svg)](https://github.com/paramt/videocloud/blob/master/LICENSE)

Generate word clouds from YouTube video captions

## Installation
```
pip install videocloud
```
*Note: A C compiler is required for the installation process.*

## Usage
```
videocloud <link to YouTube video> [options]
```

```
videocloud www.youtu.be/MHTizZ_XcUM --language=es --color=#eee
```

### Options

#### `--filepath`
Where on disk to save the generated videocloud

Default: <kbd>videocloud.png</kbd>

#### `--language`
2-letter language code of the captions

Default: <kbd>en</kbd>

#### `--color`
Hex color code of the videocloud's background color

Default: <kbd>#d1d1d1</kbd>

#### `--font`
Link to a TTF font file

Default: [Noto Sans](assets/fonts/NotoSans/NotoSans.ttf)

#### `--mask`
Link to a PNG mask file

Default: [Cloud](https://github.com/paramt/videocloud/blob/v2.5/assets/masks/cloud.png)

## Development
This project is maintained by [paramt](https://github.com/paramt) on [GitHub](https://github.com/paramt/videocloud).
'''

setuptools.setup(
    name="videocloud",
    version="3.0.0",
    url="https://github.com/paramt/VideoCloud",
    license="MIT",
    author="Param Thakkar",
    author_email="contact@param.me",
    description="A command line tool that generates word clouds from YouTube video captions",
    long_description=long_description,
	long_description_content_type="text/markdown",
    packages=["videocloud"],
    install_requires=[
        "pillow==8.1.0",
        "wordcloud==1.8.1",
        "youtube-transcript-api==0.3.1",
		"numpy==1.20.3",
		"click==7.1.2",
		"requests==2.25.1"
    ],
    python_requires=">= 3.6",
	entry_points={
        'console_scripts': [
            'videocloud=videocloud.main:videocloud'
        ]
    }
)
