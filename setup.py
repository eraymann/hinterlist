import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(
    name="hinterlist",
    version="0.0.5",
    description="INTERLIS Tools Collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eraymann/hinterlist",
    author="Elias Raymann",
    author_email="elias.raymann@swisstopo.ch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=2.7",
    install_requires="requests"
)
