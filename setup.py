# setup.py
from setuptools import setup

setup(
    name="paris-saclay-edt-parser",
    version="0.0.1",
    py_modules=["browser", "config", "event", "main"],  
    install_requires=[
        "selenium>=4.0",
        "undetected-chromedriver>=3.0",
    ],
    python_requires=">=3.9",
)
