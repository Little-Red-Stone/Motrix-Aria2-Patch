# Motrix-Aria2-Patch

#### 编译增强版Aria2添加到Motrix中使得下载速度加快

----

## 关于

此脚本是本人在学业之余开发的，欢迎借鉴与指出不足。~~由于本人Shell是废的，所以是用Python写的简短代码~~。代码很简单，无论你编程水平是高是低，配合注释应该是能看懂了（~~不是吧不是吧，你都知道GitHub了，难道这点代码都看不懂？~~）

#### 注意，本人是在Mac OS上写的脚本，用Linux的小伙伴可能需要微调，~~用Win的小伙伴...~~

## 如何使用

### HomeBrew安装

首先，如果你的电脑上没有HomeBrew，请先自行安装，脚本里要用到。这里给一个国内大神的脚本

```sh
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```

换源的话随意，推荐腾讯源（貌似更快一点）

```sh
# 替换 Homebrew 的 formula 索引的镜像（即 brew update 时所更新内容）
git -C "$(brew --repo)" remote set-url origin https://mirrors.cloud.tencent.com/homebrew/brew.git
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.cloud.tencent.com/homebrew/homebrew-core.git

# 替换 Homebrew 二进制预编译包的镜像
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.cloud.tencent.com/homebrew-bottles' >> ~/.bash_profile
source ~/.bash_profile

#（可选）禁用“自动更新” —— 执行`brew install xxx`时会自动执行`brew update`，导致安装过程比较慢。
# 通过此方法禁用后，选择合适时机手动执行`brew update`
echo 'export HOMEBREW_NO_AUTO_UPDATE=1' >> ~/.bash_profile
source ~/.bash_profile

# 更新
brew update
```

复原：

```sh
git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git

git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core

brew update

# Homebrew-bottles: 需要去`~/.bash_profile`中删除'HOMEBREW_BOTTLE_DOMAIN'
```

### Python3安装

用HomeBrew或者自己去官网下 [Python官网下载](https://www.python.org/downloads/)

### 运行脚本

首先下载源码后解压，在终端运行：python3 <你的下载位置>Patch.py

比如：

```sh
python3 /Users/???/Desktop/Patch.py
```

然后你的代码就运行起来了。你一步步按它的操作来，当出现

```sh
下载完成后请运行 python3 /Users/xzh/aria2/Patch.py
点击回车以退出
```

这两句话后，点按回车退出并运行接下来的代码

```sh
python3 /Users/???/aria2/Patch.py
```

好了，按照它的要求一步步地继续就好了！

最后你会发现Motrix的**连接限制解除了**，**而且不报错了**！！
