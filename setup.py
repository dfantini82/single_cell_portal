from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='single_cell_portal',
    version='0.1rc1',
    description='Convenience scripts for Single Cell Portal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/broadinstitute/single_cell_portal',
    author='Single Cell Portal team',
    author_email='scp-support@broadinstitute.zendesk.com',
    install_requires=['pandas', 'requests', 'scp-ingest-pipeline',],
    packages=find_packages(),
    entry_points={'console_scripts': ['manage-study=scripts.manage_study:main'],},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.7',
)
