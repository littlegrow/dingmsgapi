import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dingmsgapi',
    version='0.0.2',
    description='Python dingding msg api',
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
