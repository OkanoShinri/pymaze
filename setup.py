from setuptools import setup, find_packages
  
setup(
    name='pymaze',
    version="0.1.0",
    description='maze game program.',
    author='Okano Shinri',
    url='https://github.com/OkanoShinri/pymaze',
    author_email='okano.shinri.24m@st.kyoto-u.ac.jp',
    license='MIT',
    install_requires=["readchar"],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)