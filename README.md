## version and build

本仓库用于实践版本与构建的一些技巧，所以是多项目结构，所有项目通过 `script` 目录下的构建脚本进行构建，比如 `project_a` 就是一个 `python` 项目它可以通过 `script/build_project_a` 下的 `package` 或者 `package_exec` 脚本去构建发行版。
从 [版本控制](https://blog.witchc.io/posts/version-control/) 可以了解更多相关详情。