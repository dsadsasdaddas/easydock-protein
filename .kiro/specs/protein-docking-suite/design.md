# 设计文档

## 概述

EasyProDock是一个分阶段开发的蛋白质结构预测与分子对接一体化桌面软件。本设计文档描述了系统的整体架构和各个功能模块的详细设计，重点关注第一阶段的蛋白质结构预测功能。

系统采用模块化设计，使用Python作为主要开发语言，PySide6构建图形用户界面，集成多种生物信息学工具和算法来实现蛋白质结构预测、分子对接和结果可视化功能。

## 架构

### 整体架构

系统采用分层架构设计，包含以下主要层次：

1. **表示层（Presentation Layer）**
   - PySide6 GUI界面
   - 用户交互处理
   - 结果可视化显示

2. **业务逻辑层（Business Logic Layer）**
   - 序列验证和处理
   - 结构预测算法调用
   - 分子对接计算管理
   - 结果分析和排序

3. **数据访问层（Data Access Layer）**
   - 文件I/O操作
   - 配体库管理
   - 结果数据存储

4. **外部工具集成层（External Tools Layer）**
   - ColabFold/ChimeraX结构预测
   - P2Rank口袋识别
   - AutoDock Vina分子对接
   - smina重打分

### 技术栈

- **GUI框架**: PySide6 (Qt6 Python绑定)
- **3D可视化**: py3Dmol
- **结构预测**: ColabFold (本地部署) 或 ChimeraX AlphaFold
- **口袋识别**: P2Rank
- **分子对接**: AutoDock Vina + smina
- **分子格式处理**: RDKit, Biopython
- **报告生成**: ReportLab (PDF)
- **打包工具**: PyInstaller

## 组件和接口

### 核心组件

#### 1. 主应用程序 (MainApplication)
- 负责应用程序的启动和生命周期管理
- 协调各个功能模块
- 管理用户界面状态

#### 2. 序列处理器 (SequenceProcessor)
- 验证氨基酸序列格式
- 处理单链和双链序列
- 序列长度限制检查

#### 3. 结构预测引擎 (StructurePredictionEngine)
- 调用ColabFold或其他预测工具
- 管理预测任务队列
- 处理预测结果和置信度评分

#### 4. 可视化管理器 (VisualizationManager)
- 集成py3Dmol进行3D显示
- 处理用户交互（旋转、缩放）
- 管理显示样式和颜色方案

#### 5. 文件管理器 (FileManager)
- PDB文件读写
- SDF/MOL2配体文件处理
- 结果数据导出

### 接口设计

#### ISequenceValidator
```python
class ISequenceValidator:
    def validate_sequence(self, sequence: str) -> ValidationResult
    def check_length_limit(self, sequence: str, max_length: int) -> bool
    def detect_chain_type(self, sequence: str) -> ChainType
```

#### IStructurePredictor
```python
class IStructurePredictor:
    def predict_structure(self, sequence: str) -> PredictionResult
    def get_prediction_status(self, task_id: str) -> TaskStatus
    def cancel_prediction(self, task_id: str) -> bool
```

#### IVisualization
```python
class IVisualization:
    def display_structure(self, pdb_data: str) -> None
    def set_display_style(self, style: DisplayStyle) -> None
    def export_image(self, filename: str, resolution: int) -> bool
```

## 数据模型

### 核心数据结构

#### ProteinSequence
```python
@dataclass
class ProteinSequence:
    sequence: str
    chain_type: ChainType  # SINGLE_CHAIN, DOUBLE_CHAIN
    length: int
    validation_status: ValidationStatus
    created_at: datetime
```

#### PredictionResult
```python
@dataclass
class PredictionResult:
    sequence_id: str
    pdb_structure: str
    confidence_scores: List[float]  # pLDDT scores
    prediction_time: float
    algorithm_used: str
    created_at: datetime
```

#### BindingPocket
```python
@dataclass
class BindingPocket:
    pocket_id: str
    center_coordinates: Tuple[float, float, float]
    volume: float
    druggability_score: float
    residues: List[str]
    rank: int
```

#### LigandMolecule
```python
@dataclass
class LigandMolecule:
    molecule_id: str
    name: str
    smiles: str
    mol_data: str  # SDF or MOL2 format
    molecular_weight: float
    source: LigandSource  # BUILT_IN, USER_UPLOADED
```

#### DockingResult
```python
@dataclass
class DockingResult:
    ligand_id: str
    pocket_id: str
    binding_affinity: float
    vina_score: float
    smina_score: float
    pose_coordinates: str
    rank: int
```

## 错误处理

### 错误分类

1. **输入验证错误**
   - 无效氨基酸序列
   - 序列长度超限
   - 文件格式错误

2. **计算错误**
   - 结构预测失败
   - 对接计算异常
   - 内存不足

3. **系统错误**
   - 文件I/O错误
   - 外部工具调用失败
   - 网络连接问题（如需要）

### 错误处理策略

- 使用自定义异常类型进行错误分类
- 提供用户友好的中文错误消息
- 实现错误日志记录
- 支持错误恢复和重试机制

## 测试策略

### 双重测试方法

本项目将采用单元测试和基于属性的测试（Property-Based Testing）相结合的方法：

**单元测试**：
- 验证具体的功能实现
- 测试边界条件和错误处理
- 确保组件间接口正确

**基于属性的测试**：
- 使用Hypothesis库进行属性测试
- 每个属性测试运行最少100次迭代
- 验证系统的通用正确性属性

**测试框架**：
- 单元测试：pytest
- 属性测试：Hypothesis
- 测试覆盖率：pytest-cov

### 测试环境配置

- 模拟外部工具调用以提高测试速度
- 使用测试数据集进行功能验证
- 自动化测试流水线集成
## 正确性属性

*属性是一个特征或行为，应该在系统的所有有效执行中保持为真——本质上，是关于系统应该做什么的正式陈述。属性作为人类可读规范和机器可验证正确性保证之间的桥梁。*

基于需求分析和预工作评估，以下是系统必须满足的核心正确性属性：

### 属性 1：序列验证和预测完整性
*对于任何*有效的蛋白质氨基酸序列（≤800残基），系统应该在合理时间内（5-12分钟）完成结构预测并生成包含pLDDT置信度评分的有效PDB结构文件
**验证需求：需求 1.1, 1.2, 1.4**

### 属性 2：输入边界验证
*对于任何*超过800残基的序列或包含无效字符的序列，系统应该拒绝处理并返回明确的中文错误信息
**验证需求：需求 1.3, 1.5**

### 属性 3：口袋识别完整性
*对于任何*成功预测的蛋白质结构，系统应该使用P2Rank识别所有结合口袋，并为每个口袋提供完整的参数信息和可视化标记
**验证需求：需求 2.1, 2.2, 2.3**

### 属性 4：配体文件解析通用性
*对于任何*有效的SDF或MOL2格式配体文件，系统应该正确解析并加载分子结构数据；对于无效格式文件，应该返回格式错误提示
**验证需求：需求 3.3, 3.4, 3.5**

### 属性 5：分子对接流程完整性
*对于任何*有效的蛋白质-配体组合，系统应该依次执行AutoDock Vina对接、smina重打分、结果排序，并输出包含完整能量数据的Top10构象
**验证需求：需求 4.1, 4.2, 4.3, 4.4, 4.5**

### 属性 6：3D可视化功能性
*对于任何*分子结构数据，系统应该使用py3Dmol正确显示3D结构，支持旋转、缩放、平移交互，并提供多种显示样式选项
**验证需求：需求 5.1, 5.2, 5.3, 5.4**

### 属性 7：PDF报告完整性
*对于任何*完整的分析结果，系统应该生成包含序列信息、pLDDT曲线、口袋参数、对接结果、结构截图和指定水印的完整PDF报告
**验证需求：需求 6.1, 6.2, 6.3, 6.4, 6.5, 6.6**

### 属性 8：中文界面一致性
*对于任何*用户界面元素、错误信息和帮助文档，系统应该使用PySide6框架提供完全中文化的显示
**验证需求：需求 7.1, 7.2, 7.3, 7.4**

### 属性 9：离线独立运行
*对于任何*目标运行环境，系统应该在无网络连接和无Python环境的情况下正常启动和运行所有功能
**验证需求：需求 8.4**

### 属性 10：配体库完整性
*当*用户访问配体选择界面时，系统应该显示包含50种内置药物分子的完整库，并支持加载任何选定分子的结构数据
**验证需求：需求 3.1, 3.2**

## 第一阶段实现重点

### 核心功能优先级

第一阶段将专注于以下核心功能的实现：

1. **序列输入和验证**
   - 氨基酸序列格式验证
   - 长度限制检查
   - 单链/双链序列识别

2. **结构预测引擎**
   - ColabFold本地部署集成
   - 预测任务管理
   - pLDDT置信度评分处理

3. **基础可视化**
   - py3Dmol 3D结构显示
   - 基本交互功能（旋转、缩放）
   - PDB文件导出

4. **中文GUI界面**
   - PySide6主界面设计
   - 序列输入区域
   - 结果显示区域
   - 进度指示和错误提示

### 技术实现细节

#### 结构预测集成

**ColabFold本地部署方案**：
- 使用conda环境管理ColabFold依赖
- 集成MMseqs2进行序列搜索
- 配置本地模型文件缓存
- 实现预测任务队列管理

**替代方案**：
- ChimeraX AlphaFold插件集成
- ESMFold轻量级预测
- 在线API调用（需网络连接）

#### 可视化实现

**py3Dmol集成**：
- 在PySide6中嵌入Web视图
- JavaScript与Python交互
- 自定义分子显示样式
- 交互事件处理

#### 数据流设计

```
用户输入序列 → 序列验证 → 结构预测 → 结果解析 → 3D可视化 → 文件导出
     ↓              ↓           ↓          ↓          ↓
   错误提示    格式检查    进度显示   置信度评分   交互控制
```

## 性能考虑

### 计算性能

- **内存管理**：大分子结构的内存优化
- **并发处理**：多序列预测的任务队列
- **缓存策略**：预测结果和模型文件缓存
- **进度反馈**：实时预测进度显示

### 用户体验

- **响应性**：GUI操作的即时反馈
- **错误恢复**：预测失败的重试机制
- **资源监控**：CPU和内存使用情况显示
- **中断支持**：长时间计算的取消功能

## 安全考虑

### 输入安全

- 序列长度限制防止内存溢出
- 文件格式验证防止恶意文件
- 路径遍历攻击防护
- 输入字符过滤和转义

### 数据安全

- 临时文件安全清理
- 用户数据本地存储
- 敏感信息加密存储
- 日志信息脱敏处理

## 可扩展性设计

### 模块化架构

系统采用插件化设计，便于后续功能扩展：

- **预测引擎插件**：支持多种结构预测算法
- **对接引擎插件**：支持不同分子对接工具
- **可视化插件**：支持多种3D渲染引擎
- **导出插件**：支持多种文件格式输出

### 配置管理

- 算法参数配置文件
- 用户偏好设置
- 系统性能调优参数
- 插件启用/禁用配置

### 国际化支持

虽然当前版本专注于中文界面，但架构支持未来的多语言扩展：

- 字符串资源外部化
- 动态语言切换支持
- 文化相关格式处理
- 右到左语言支持预留