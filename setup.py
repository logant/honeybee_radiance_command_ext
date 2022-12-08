import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='honeybee_radiance_command_ext',
    version='1.0.1',
    author='HKS LINE',
    author_email='tlogan@hksinc.com',
    description='Extending Honeybee Radiance to include additional commands',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/logant/honeybee_radiance_command_ext',
    license='AGPL-3.0',
    packages=['honeybee_radiance_command_ext'],
    install_requires=['honeybee_radiance'],
)