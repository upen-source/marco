from setuptools import setup, find_packages

setup(
    name="marco",
    packages=find_packages(include=['marco'], exclude=['examples']),
    version="0.1.0",
    license="MIT",
    description="Statistics class automation",
    author="Andres Galvan",
    author_email="adfelipegalvan@gmail.com",
    url="https://github.com/afgalvan/marco",
    download_url="https://github.com/afgalvan/marco/archive/v_01.tar.gz",
    keywords=["statistics", "pandas", "numpy"],
    install_requires=[
        "pandas",
        "numpy"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
