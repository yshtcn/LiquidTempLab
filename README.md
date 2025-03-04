# 液体温度实验模拟系统 (LiquidTempLab)

这是一个用于模拟热水和冷牛奶混合过程的温度变化实验系统。

## 在线体验

您可以直接访问在线版本：[LiquidTempLab在线演示](https://ai.ysht.me/class/chat.html)

## 功能特点

- 实时模拟热水和冷牛奶的温度变化过程
- 使用折线图直观展示温度变化趋势
- 支持交互式操作和实验数据展示
- 提供完整的实验过程分析

## 本地运行

1. 克隆仓库：
```bash
git clone [仓库地址]
```

2. 直接打开 `chat.html` 文件即可运行

## 打包版本

如果您需要独立的可执行文件，我们提供了打包版本：

1. 使用 `LiquidTempLab.spec` 进行打包：
```bash
pyinstaller LiquidTempLab.spec
```

2. 打包后的文件将在 `dist` 目录中生成

## 技术栈

- HTML5
- JavaScript
- CSS3
- Chart.js (图表展示)

## 许可证

MIT License 