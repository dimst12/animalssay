from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="animalssay",
    version="0.1.2",
    packages=find_packages(),
    author="hunter",
    description="A simple example Python library where animals can say words",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
