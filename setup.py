import setuptools, os

readme_path = os.path.join(os.getcwd(), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        long_description = f.read()
else:
    long_description = 'swagger_scraper'

setuptools.setup(
    name="swagger_scraper",
    version="0.0.1",
    author="Kristof",
    description="scrape swagger htmls into python files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/swagger_scraper",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)