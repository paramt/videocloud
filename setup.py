import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="videocloud",
    version="2.0",
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
        "youtube-transcript-api==0.1.4"
    ],
    python_requires=">= 3.6",
	entry_points={
        'console_scripts': [
            'videocloud=videocloud.main:main'
        ]
    }
)
