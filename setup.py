import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="honeybee-radiance-command-ext",
    version="1.0.0",
    setup_requires=['setuptools_scm'],
    author="HKS LINE",
    author_email="tlogan@hksinc.com",
    description="Python wrapper around Radiance commands.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(exclude=["tests*"]),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent"
    ],
    license="AGPL-3.0"
)