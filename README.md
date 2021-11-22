## version and build

本仓库用于实践版本与构建的一些技巧。为了实践不同语言的版本和构建方案，所以该仓库为多项目结构。每个目录都代表一个简单项目，目前存在的项目有：
### [python_demo](./python_demo)
这是一个命令行 python 项目，拥有 wheel 包和可执行程序两种构建方式，版本信息中携带 构建时间，仓库以及提交hash信息以及其它构建环境等信息：
```bash
(.venv) [root@WEN-PC version-and-build]# python3 python_demo/main.py version
{'Build date': 'unknown',
 'Build repo': 'unknown',
 'Build version': 'unknown',
 'CPython': '3.7.4',
 'Last commit date': 'unknown',
 'OpenSSL version': 'OpenSSL 1.0.2k-fips  26 Jan 2017',
 'platform': 'Linux-4.4.0-19041-Microsoft-x86_64-with-centos-7.6.1810-Core',
 'version-and-build demo version': '0.1.0'}
```
> 注：python 项目的构建需要手动准备好虚拟环境和 `PYTHONPATH` 环境变量。