from setuptools import setup, find_packages

setup(
    name="medical_chatbox",
    version="0.1",
    packages=find_packages(),  # this will include 'medical_chatbox'
    install_requires=[
        # add dependencies from requirements.txt if needed
    ],
    python_requires='>=3.10',
)
