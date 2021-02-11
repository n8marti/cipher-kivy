# Developer Notes

1. Ensure that APT dependencies are installed.
```shell
$ sudo apt install python3-venv libffi-dev libssl-dev
```
1. Clone repo.
```shell
$ git clone git@github.com:n8marti/cipher-kivy.git
```
1. Enter repo folder.
```shell
$ cd cipher-kivy
```
1. Create virtual environment.
```shell
$ python3 -m venv env
```
1. Activate virtual environment.
```shell
$ source env/bin/activate
```
1. Setup env from requirements.txt.
```shell
(env) $ pip3 install --requirement requirements.txt
```
1. Build APK package.
```shell
# First run will download Android SDK, NDK, etc. (~1 GB)
(env) $ buildozer android debug deploy run
```
