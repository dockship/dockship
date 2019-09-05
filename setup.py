from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dockship',
    author_email='nishchal@unrealai.xyz',
    author='Unreal AI Technologies Pvt. Ltd.',
    url='https://github.com/dockship/dockship',
    version='0.0.2',
    description='Test Module',
    py_modules=["hellotest"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description = long_description,
    long_description_content_type = "text/markdown",
)