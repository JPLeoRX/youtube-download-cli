from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme_text = readme_file.read()


setup_args = dict(
    entry_points = {
        'console_scripts': ['youtube-download-cli=youtube_download_cli.command_line:main'],
    },
    name='youtube-download-cli',
    version='0.0.0.3',
    description="",
    keywords=[],
    long_description=readme_text,
    long_description_content_type="text/markdown",
    license='Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License',
    packages=find_packages(),
    author="Leo Ertuna",
    author_email="leo.ertuna@gmail.com",
    url="https://github.com/jpleorx/youtube-download-cli",
    download_url='https://pypi.org/project/youtube-download-cli/'
)


install_requires = [
    'argparse',
    'colorama',
    'pytube',
    'moviepy'
]


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
