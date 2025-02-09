from setuptools import setup, find_packages

setup(
    name="file-merger",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'merge-files=file_merger.cli:main',
        ],
    },
    author="Pratik Pakhale",
    description="A CLI tool to merge files matching patterns while preserving directory structure",
    python_requires=">=3.6",
)
