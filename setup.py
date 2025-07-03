from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function returns a list of dependencies from requirements.txt
    """
    try:
        with open('requirements.txt', 'r') as file:
            return [
                line.strip()
                for line in file.readlines()
                if line.strip() and not line.startswith("-e .")
            ]
    except FileNotFoundError:
        print("requirements.txt file not found.")
        return []

setup(
    name="CHATBOT-ENGINEER-ASSESSMENT",
    version="0.0.1",
    author="Kanon Chua",
    author_email="geochua144@gmail.com",
    description="A trip planning package",
    packages=find_packages(),
    install_requires=get_requirements(),
)