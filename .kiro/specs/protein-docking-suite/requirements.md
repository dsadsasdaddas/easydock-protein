# 需求文档

## 简介

EasyProDock是一款全中文、纯本地运行、可单文件分发的蛋白质结构预测与分子对接一体化桌面软件。该软件将分阶段开发，第一阶段专注于蛋白质结构预测功能，后续逐步添加其他功能模块。

## 术语表

- **EasyProDock系统**: 本软件的完整桌面应用程序
- **蛋白质结构预测模块**: 负责从氨基酸序列生成三级结构的组件
- **分子对接模块**: 执行配体与蛋白质结合位点对接计算的组件
- **可视化模块**: 提供3D分子结构交互式显示的组件
- **报告生成模块**: 创建包含分析结果的PDF报告的组件
- **配体库**: 内置的50种常见药物分子数据库
- **结合口袋**: 蛋白质表面可与小分子配体结合的区域
- **pLDDT**: 预测局部距离差异测试，用于评估结构预测置信度的指标
- **结合亲和力**: 配体与蛋白质结合强度的量化指标

## 需求

### 需求 1 - 蛋白质结构预测（第一阶段）

**用户故事:** 作为生物学研究人员，我希望能够输入蛋白质氨基酸序列并快速获得高精度的三级结构预测，以便进行后续的分子对接研究。

#### 验收标准

1. WHEN 用户输入单链蛋白氨基酸序列（≤800残基）THEN EasyProDock系统 SHALL 在5-12分钟内输出高精度三级结构
2. WHEN 用户输入双链蛋白氨基酸序列（≤800残基）THEN EasyProDock系统 SHALL 在5-12分钟内输出高精度三级结构
3. WHEN 用户输入超过800残基的序列 THEN EasyProDock系统 SHALL 拒绝处理并显示错误提示
4. WHEN 结构预测完成 THEN EasyProDock系统 SHALL 生成包含pLDDT置信度评分的结构文件
5. WHEN 用户输入无效的氨基酸序列 THEN EasyProDock系统 SHALL 验证序列格式并提供明确的错误信息

### 需求 2 - 结合口袋识别（第二阶段）

**用户故事:** 作为研究人员，我希望系统能够自动识别蛋白质的结合口袋并进行可视化标记，以便我能够快速定位潜在的药物结合位点。

#### 验收标准

1. WHEN 蛋白质结构预测完成 THEN EasyProDock系统 SHALL 使用P2Rank算法自动识别所有结合口袋
2. WHEN 结合口袋识别完成 THEN EasyProDock系统 SHALL 以彩虹色高亮显示识别出的口袋区域
3. WHEN 显示结合口袋 THEN EasyProDock系统 SHALL 提供每个口袋的详细参数信息
4. WHEN 用户选择特定口袋 THEN EasyProDock系统 SHALL 突出显示该口袋并显示其属性

### 需求 3 - 配体管理（第三阶段）

**用户故事:** 作为研究人员，我希望能够使用内置的药物分子库或上传自定义配体进行分子对接，以便筛选潜在的药物候选分子。

#### 验收标准

1. WHEN 用户访问配体选择界面 THEN EasyProDock系统 SHALL 显示包含50种常见药物分子的内置库
2. WHEN 用户选择内置配体 THEN EasyProDock系统 SHALL 加载选定分子的三维结构数据
3. WHEN 用户拖拽SDF格式文件到界面 THEN EasyProDock系统 SHALL 解析并加载自定义配体结构
4. WHEN 用户拖拽MOL2格式文件到界面 THEN EasyProDock系统 SHALL 解析并加载自定义配体结构
5. WHEN 上传的配体文件格式无效 THEN EasyProDock系统 SHALL 显示格式错误提示并拒绝加载

### 需求 4 - 分子对接（第四阶段）

**用户故事:** 作为研究人员，我希望系统能够执行高通量分子对接计算并按结合亲和力排序结果，以便我能够快速识别最有前景的配体-蛋白质复合物。

#### 验收标准

1. WHEN 用户启动分子对接计算 THEN EasyProDock系统 SHALL 使用AutoDock Vina算法执行对接
2. WHEN AutoDock Vina对接完成 THEN EasyProDock系统 SHALL 使用smina算法重新评分所有构象
3. WHEN 对接计算完成 THEN EasyProDock系统 SHALL 按结合亲和力从高到低排序所有构象
4. WHEN 排序完成 THEN EasyProDock系统 SHALL 输出Top10最佳结合构象
5. WHEN 显示对接结果 THEN EasyProDock系统 SHALL 提供每个构象的详细结合能量数据

### 需求 5 - 3D可视化（第五阶段）

**用户故事:** 作为研究人员，我希望能够通过交互式3D可视化查看分子结构和对接结果，以便更好地理解分子间的相互作用。

#### 验收标准

1. WHEN 用户打开3D可视化界面 THEN EasyProDock系统 SHALL 使用py3Dmol库显示分子的三维结构
2. WHEN 用户在3D视图中操作 THEN EasyProDock系统 SHALL 支持鼠标旋转、缩放和平移功能
3. WHEN 用户选择不同显示样式 THEN EasyProDock系统 SHALL 提供多种分子表示方式（线框、球棍、表面等）
4. WHEN 用户查看对接复合物 THEN EasyProDock系统 SHALL 同时显示蛋白质结构和配体分子
5. WHEN 3D视图更新 THEN EasyProDock系统 SHALL 保持流畅的交互响应性能

### 需求 6 - 报告生成（第六阶段）

**用户故事:** 作为研究人员，我希望能够生成包含完整分析结果的专业PDF报告，以便用于学术交流和实验记录。

#### 验收标准

1. WHEN 用户请求生成报告 THEN EasyProDock系统 SHALL 创建包含输入序列信息的PDF文档
2. WHEN 生成报告 THEN EasyProDock系统 SHALL 包含pLDDT置信度曲线图表
3. WHEN 生成报告 THEN EasyProDock系统 SHALL 包含所有识别口袋的详细参数表格
4. WHEN 生成报告 THEN EasyProDock系统 SHALL 包含Top10对接构象的结合能量数据表
5. WHEN 生成报告 THEN EasyProDock系统 SHALL 包含高清的3D结构截图
6. WHEN 生成报告 THEN EasyProDock系统 SHALL 在每页添加用户指定的学校水印

### 需求 7 - 中文界面（贯穿所有阶段）

**用户故事:** 作为最终用户，我希望使用一个全中文的图形界面，以便更容易理解和操作软件功能。

#### 验收标准

1. WHEN 软件启动 THEN EasyProDock系统 SHALL 显示完全中文化的用户界面
2. WHEN 用户与界面交互 THEN EasyProDock系统 SHALL 使用PySide6框架提供现代化的GUI体验
3. WHEN 显示错误或状态信息 THEN EasyProDock系统 SHALL 使用中文提供清晰的用户反馈
4. WHEN 用户访问帮助信息 THEN EasyProDock系统 SHALL 提供中文的操作指导和说明

### 需求 8 - 跨平台分发（最终阶段）

**用户故事:** 作为用户，我希望能够在Windows和Mac系统上直接运行软件，无需安装Python环境或其他依赖，以便快速开始使用。

#### 验收标准

1. WHEN 软件打包完成 THEN EasyProDock系统 SHALL 生成Windows平台的单文件.exe可执行程序
2. WHEN 软件打包完成 THEN EasyProDock系统 SHALL 生成Mac平台的单文件.dmg安装包
3. WHEN 用户在目标系统运行程序 THEN EasyProDock系统 SHALL 无需预装Python环境即可正常启动
4. WHEN 程序运行 THEN EasyProDock系统 SHALL 完全离线工作，不依赖网络连接
5. WHEN 使用PyInstaller打包 THEN EasyProDock系统 SHALL 将所有依赖库打包到单一可执行文件中