import io

from setuptools import find_packages
from setuptools import setup

setup(
    name="App",
    version="1.0.0",
    license="BSD",
    maintainer="eocode",
    maintainer_email="hola@eliasojedamedina.com",
    description="Your project description.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
