import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(
    name="hinterlist",
    version="0.0.2",
    description="INTERLIS Check Launcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eraymann/hinterlist",
    author="Elias Raymann",
    author_email="elias.raymann@swisstopo.ch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
    install_requires="requests"
)
