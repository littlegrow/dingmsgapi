import setuptools
from ding_msg_api import name, version, description

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='dingding',
    install_requires=[],
    packages=setuptools.find_packages(),
    author='littlegrow',
    author_email='kfliuleigang@sina.com',
    url='https://github.com/littlegrow/dingmsgapi',
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    project_urls={
        'Blog': 'https://littlegrow.top',
    },
)
