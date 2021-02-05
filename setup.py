import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multiple-numbers-samukasmk",
    version="0.0.1",
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
    scripts=['scripts/detects-multiplicable-numbers.py'],
)