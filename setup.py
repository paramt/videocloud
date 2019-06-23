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
videocloud <link to youtube video> [filepath]
```
If no filepath is given, the wordcloud will be generated in `./videocloud.png`

## Development
This project is maintained by [paramt](https://github.com/paramt) on [GitHub](https://github.com/paramt/videocloud).
'''

setuptools.setup(
    name="videocloud",
    version="2.3.1",
    url="https://github.com/paramt/VideoCloud",
    license="MIT",
    author="Param Thakkar",
    author_email="contact@param.me",
    description="A command line tool that generates word clouds from YouTube video captions",
    long_description=long_description,
	long_description_content_type="text/markdown",
    packages=["videocloud"],
    install_requires=[
        "pillow==6.0.0",
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
