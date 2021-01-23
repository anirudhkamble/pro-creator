from setuptools import setup, find_packages



params = dict(
    name="pro-manager",
    description="A simple project template creator.",
    version="0.1.0",
    author="Anirudh Kamble",
    python_requires='>=2.7,>=3.0',
    package_dir={"": "src"},
    packages=find_packages("src"),
    scripts=["scripts/project"]
)


def main():
    setup(**params)


if __name__ == "__main__":
    main()
