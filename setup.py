import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="VideoCloud",
    version="1.1.1",
    url="https://github.com/paramt/VideoCloud",
    license="MIT",
    author="Param Thakkar",
    author_email="contact@param.me",
    description="A command line tool that generates word clouds from YouTube video captions",
    long_description=long_description,
	long_description_content_type="text/markdown",
    scripts=["./scripts/videocloud"],
    packages=["videocloud"],
    install_requires=[
        "setuptools",
        "pillow==6.0.0",
        "wordcloud==1.5.0",
        "youtube-transcript-api==0.1.4"
    ],
    python_requires=">= 3.6"
)
