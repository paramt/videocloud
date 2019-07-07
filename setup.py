import setuptools

long_description = '''
# VideoCloud
[![License](https://img.shields.io/github/license/paramt/videocloud.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/videocloud.svg)](https://pypi.org/project/VideoCloud/)

Generate word clouds from YouTube video captions

## Installation
```
pip install videocloud
```
*Note: A C compiler is required for the installation process.*

## Usage
```
videocloud <link to youtube video> [filepath] [language code] [font]
```
If no filepath is given, the wordcloud will be generated as `videocloud.png`.
The lanuage code defaults to `en` and the fontpath defaults to [Noto Sans](https://github.com/paramt/videocloud/blob/master/assets/fonts/NotoSans/NotoSans.ttf)
To use a custom font, provide the HTTP link for its TTF file. Similarly, you can provide an HTTP link to a PNG mask file. The mask defaults to
[a generic cloud](https://github.com/paramt/videocloud/blob/v2.5/assets/masks/cloud.png).

## Development
This project is maintained by [paramt](https://github.com/paramt) on [GitHub](https://github.com/paramt/videocloud).
'''

setuptools.setup(
    name="videocloud",
    version="2.5",
    url="https://github.com/paramt/VideoCloud",
    license="MIT",
    author="Param Thakkar",
    author_email="contact@param.me",
    description="A command line tool that generates word clouds from YouTube video captions",
    long_description=long_description,
	long_description_content_type="text/markdown",
    packages=["videocloud"],
    install_requires=[
        "pillow==6.1.0",
        "wordcloud==1.5.0",
        "youtube-transcript-api==0.1.5"
    ],
    python_requires=">= 3.6",
	entry_points={
        'console_scripts': [
            'videocloud=videocloud.main:main'
        ]
    }
)
