# Developer Notes

1. Ensure that APT dependencies are installed.
    ```shell
    ~$ sudo apt install python3-venv libffi-dev libssl-dev
    ```
1. Clone repo.
    ```shell
    ~$ git clone git@github.com:n8marti/cipher-kivy.git
    ```
1. Enter repo folder.
    ```shell
    ~$ cd cipher-kivy
    ```
1. Create virtual environment.
    ```shell
    ~/cipher-kivy$ python3 -m venv env
    ```
1. Activate virtual environment.
    ```shell
    ~/cipher-kivy$ source env/bin/activate
    ```
1. Install enviroment dependencies from requirements.txt.
    ```shell
    (env) ~/cipher-kivy$ pip3 install --requirement requirements.txt
    ```
1. Run the app.
  - EITHER: Build the APK package. (You will need to create a buildozer.spec file first.)
    ```shell
    # First run will download Android SDK, NDK, etc. (~1.5 GB)
    (env) ~/cipher-kivy$ buildozer android debug deploy run
    ```
  - OR: Run the app locally.
    ```shell
    (env) ~/cipher-kivy$ python3 cipher/main.py
    ```
1. Deactivate enviroment when done.
    ```shell
    (env) ~/cipher-kivy$ deactivate
    ~/cipher-kivy$
    ```
