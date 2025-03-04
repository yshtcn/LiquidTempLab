# 液体温度实验模拟系统 (LiquidTempLab)

这是一个用于物理实验教学的综合性工具，集成了温度记录、AI 辅助学习和编程实践功能。该工具旨在帮助学生通过实验记录、AI 对话和编程实践，深入理解物理实验原理。

## 在线体验

您可以直接访问在线版本：[LiquidTempLab在线演示](https://ai.ysht.me/class/chat.html)

## 功能特点

- 提供智能对话功能，帮助学生理解物理实验原理
- 展示AI编写的温度模拟程序，作为编程实践参考
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