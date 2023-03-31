"""Setup"""
from setuptools import setup, find_namespace_packages

setup(
    name='clean_insight_my_folder',
    version='0.0.2',
    description='Script, which sort the folder',
    author='Alex',
    author_email='Asmo@hotmail.com',
    url='https://github.com/AleksandrRevuka/clean_folder_Insighr.git',
    license='MIT',
# classifiers = [
#     "Programming Language :: Python :: 3",
#     "License :: OSI Approved :: MIT License",
#     "Operating System :: OS Independent",],
    packages=find_namespace_packages(),
    # data_files=[('clean_folder', [''])],
    include_package_data=True,
    entry_points={'console_scripts': ['clean-folder=clean_insight_my_folder.sort:main']}
)
