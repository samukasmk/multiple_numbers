import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def test_suite():
    import unittest
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setuptools.setup(
    name="multiplicable-numbers",
    version="0.1.4",
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
    python_requires='>=3.11',
    scripts=["multiple_numbers/multiple_numbers"],
    install_requires=["num2words>=0.5.13"],
    test_suite='setup.test_suite',
)