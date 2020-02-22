import os

import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="configue",
    version="DEV",
    url="https://github.com/illuin-tech/configue/",

    author="Illuin Technology",
    author_email="contact@illuin.tech",

    description="Helpers to load your application configuration from YAML files",
    long_description=long_description,
    long_description_content_type="text/markdown",

    zip_safe=False,
    platforms="any",

    install_requires=[
        "pyyaml>=5.1.0,<6.0.0",
    ],
    python_requires=">=3.6,<4.0",
    packages=setuptools.find_packages(include=["configue", "configue.*"]),

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
