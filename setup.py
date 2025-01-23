from setuptools import find_packages, setup

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = [line.strip() for line in f if line.strip()]

setup(
    name="chatbot",                  # Package name
    version="0.0.1",                 # Package version
    description="Chatbot Interaction",  # Short description
    install_requires=requirements,   # Dependencies from requirements.txt
    packages=find_packages(),        # Automatically include all packages
    zip_safe=False,                  # Disable zip packaging for easier debugging
)
