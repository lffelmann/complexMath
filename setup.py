import setuptools

VERSION = "0.0.1"
DESCRIPTION = "Use complex numbers in python."

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="complexNumbers",
    version=VERSION,
    author="lffelmann",
    desription=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/lffelmann/complexNumbers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires=">=3.10",
)
