from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str] :
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="my_package",
    version="0.1.0",
    author="Venu Madhav",
    author_email="venumadhav592@example.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires='>=3.6',
)