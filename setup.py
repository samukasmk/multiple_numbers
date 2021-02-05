import setuptools

import multiple_numbers

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multiple_numbers",
    version=multiple_numbers.__version__,
    author="Samuel Sampaio",
    author_email="samukasmk@gmail.com",
    license="Apache 2.0",
    description="A command line tools that tells if is multiple numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samukasmk/multiple_numbers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
