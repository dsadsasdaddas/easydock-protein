"""
核心接口定义模块

定义了EasyProDock系统的核心接口，包括序列验证、结构预测和可视化功能。
"""

from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Any
from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class ChainType(Enum):
    """蛋白质链类型枚举"""
    SINGLE_CHAIN = "single_chain"
    DOUBLE_CHAIN = "double_chain"


class ValidationStatus(Enum):
    """验证状态枚举"""
    VALID = "valid"
    INVALID_FORMAT = "invalid_format"
    INVALID_LENGTH = "invalid_length"
    INVALID_CHARACTERS = "invalid_characters"


class TaskStatus(Enum):
    """任务状态枚举"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class DisplayStyle(Enum):
    """显示样式枚举"""
    WIREFRAME = "wireframe"
    BALL_STICK = "ball_stick"
    SURFACE = "surface"
    CARTOON = "cartoon"
    RIBBON = "ribbon"


@dataclass
class ValidationResult:
    """序列验证结果"""
    is_valid: bool
    status: ValidationStatus
    error_message: Optional[str] = None
    chain_type: Optional[ChainType] = None
    sequence_length: Optional[int] = None


@dataclass
class PredictionResult:
    """结构预测结果"""
    sequence_id: str
    pdb_structure: str
    confidence_scores: List[float]  # pLDDT scores
    prediction_time: float
    algorithm_used: str
    created_at: datetime
    task_status: TaskStatus


class ISequenceValidator(ABC):
    """序列验证接口
    
    负责验证蛋白质氨基酸序列的格式、长度和类型。
    """
    
    @abstractmethod
    def validate_sequence(self, sequence: str) -> ValidationResult:
        """验证氨基酸序列
        
        Args:
            sequence: 待验证的氨基酸序列字符串
            
        Returns:
            ValidationResult: 包含验证结果的对象
        """
        pass
    
    @abstractmethod
    def check_length_limit(self, sequence: str, max_length: int = 800) -> bool:
        """检查序列长度限制
        
        Args:
            sequence: 氨基酸序列
            max_length: 最大允许长度，默认800残基
            
        Returns:
            bool: 是否在长度限制内
        """
        pass
    
    @abstractmethod
    def detect_chain_type(self, sequence: str) -> ChainType:
        """检测蛋白质链类型
        
        Args:
            sequence: 氨基酸序列
            
        Returns:
            ChainType: 检测到的链类型
        """
        pass


class IStructurePredictor(ABC):
    """结构预测接口
    
    负责调用结构预测算法并管理预测任务。
    """
    
    @abstractmethod
    def predict_structure(self, sequence: str) -> str:
        """预测蛋白质结构
        
        Args:
            sequence: 氨基酸序列
            
        Returns:
            str: 预测任务ID
        """
        pass
    
    @abstractmethod
    def get_prediction_status(self, task_id: str) -> TaskStatus:
        """获取预测任务状态
        
        Args:
            task_id: 任务ID
            
        Returns:
            TaskStatus: 任务当前状态
        """
        pass
    
    @abstractmethod
    def get_prediction_result(self, task_id: str) -> Optional[PredictionResult]:
        """获取预测结果
        
        Args:
            task_id: 任务ID
            
        Returns:
            Optional[PredictionResult]: 预测结果，如果任务未完成则返回None
        """
        pass
    
    @abstractmethod
    def cancel_prediction(self, task_id: str) -> bool:
        """取消预测任务
        
        Args:
            task_id: 任务ID
            
        Returns:
            bool: 是否成功取消
        """
        pass


class IVisualization(ABC):
    """可视化接口
    
    负责3D分子结构的显示和交互。
    """
    
    @abstractmethod
    def display_structure(self, pdb_data: str) -> None:
        """显示分子结构
        
        Args:
            pdb_data: PDB格式的结构数据
        """
        pass
    
    @abstractmethod
    def set_display_style(self, style: DisplayStyle) -> None:
        """设置显示样式
        
        Args:
            style: 显示样式
        """
        pass
    
    @abstractmethod
    def export_image(self, filename: str, resolution: int = 1024) -> bool:
        """导出结构图像
        
        Args:
            filename: 输出文件名
            resolution: 图像分辨率
            
        Returns:
            bool: 是否成功导出
        """
        pass
    
    @abstractmethod
    def enable_interaction(self, enabled: bool) -> None:
        """启用/禁用交互功能
        
        Args:
            enabled: 是否启用交互
        """
        pass
    
    @abstractmethod
    def get_view_state(self) -> dict:
        """获取当前视图状态
        
        Returns:
            dict: 包含视图参数的字典
        """
        pass
    
    @abstractmethod
    def set_view_state(self, state: dict) -> None:
        """设置视图状态
        
        Args:
            state: 视图状态参数
        """
        pass