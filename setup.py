from setuptools import setup
from setuptools import find_packages

# Load the README file.
# with open(file="README.md", mode="r") as readme_handle:
#     long_description = readme_handle.read()

setup(
    name='streamlit_login_auth_ui',

    author='SOVDEVS DEv1',

    author_email='sovdevs0@gmail.com',

    version='0.2.0',

    description='A streamlit library which provides a Login/Sign-Up UI with an option to reset password, also supports cookies.',

    # long_description=long_description,

    long_description_content_type="text/markdown",

    url='https://github.com/sovdevs/st_login_auth_ui_23',

    install_requires=[
        'streamlit',
        'streamlit_lottie',
        'extra_streamlit_components',
        'streamlit_option_menu',
        'trycourier',
        'streamlit_cookies_manager',
    ],

    keywords='streamlit, machine learning, login, sign-up, authentication, cookies',

    packages=find_packages(),


    include_package_data=True,

    python_requires='>=3.10',

    classifiers=[

        # 'Intended Audience :: Developers',
        # 'Intended Audience :: ML Engineers',
        # 'Intended Audience :: Streamlit App Developers',

        'License :: OSI Approved :: MIT License',

        'Natural Language :: English',

        'Operating System :: OS Independent',

        # 'Programming Language :: Python :: 3.10.12',

        # 'Topic :: Streamlit',
        # 'Topic :: Authentication',
        # 'Topic :: Login/Sign-Up'

    ]
)