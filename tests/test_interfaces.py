"""
接口定义测试模块

测试核心接口的定义和基本功能。
"""

import pytest
from src.easyprodock.interfaces import (
    ISequenceValidator,
    IStructurePredictor,
    IVisualization,
    ValidationResult,
    PredictionResult,
    ChainType,
    ValidationStatus,
    TaskStatus,
    DisplayStyle
)


class TestEnums:
    """测试枚举类型"""
    
    def test_chain_type_enum(self):
        """测试链类型枚举"""
        assert ChainType.SINGLE_CHAIN.value == "single_chain"
        assert ChainType.DOUBLE_CHAIN.value == "double_chain"
    
    def test_validation_status_enum(self):
        """测试验证状态枚举"""
        assert ValidationStatus.VALID.value == "valid"
        assert ValidationStatus.INVALID_FORMAT.value == "invalid_format"
        assert ValidationStatus.INVALID_LENGTH.value == "invalid_length"
        assert ValidationStatus.INVALID_CHARACTERS.value == "invalid_characters"
    
    def test_task_status_enum(self):
        """测试任务状态枚举"""
        assert TaskStatus.PENDING.value == "pending"
        assert TaskStatus.RUNNING.value == "running"
        assert TaskStatus.COMPLETED.value == "completed"
        assert TaskStatus.FAILED.value == "failed"
        assert TaskStatus.CANCELLED.value == "cancelled"
    
    def test_display_style_enum(self):
        """测试显示样式枚举"""
        assert DisplayStyle.WIREFRAME.value == "wireframe"
        assert DisplayStyle.BALL_STICK.value == "ball_stick"
        assert DisplayStyle.SURFACE.value == "surface"
        assert DisplayStyle.CARTOON.value == "cartoon"
        assert DisplayStyle.RIBBON.value == "ribbon"


class TestDataClasses:
    """测试数据类"""
    
    def test_validation_result_creation(self):
        """测试ValidationResult创建"""
        result = ValidationResult(
            is_valid=True,
            status=ValidationStatus.VALID,
            chain_type=ChainType.SINGLE_CHAIN,
            sequence_length=100
        )
        assert result.is_valid is True
        assert result.status == ValidationStatus.VALID
        assert result.chain_type == ChainType.SINGLE_CHAIN
        assert result.sequence_length == 100
        assert result.error_message is None
    
    def test_validation_result_with_error(self):
        """测试带错误信息的ValidationResult"""
        result = ValidationResult(
            is_valid=False,
            status=ValidationStatus.INVALID_FORMAT,
            error_message="序列包含无效字符"
        )
        assert result.is_valid is False
        assert result.status == ValidationStatus.INVALID_FORMAT
        assert result.error_message == "序列包含无效字符"


class TestInterfaces:
    """测试接口定义"""
    
    def test_sequence_validator_interface(self):
        """测试序列验证接口定义"""
        # 验证接口是抽象基类
        assert hasattr(ISequenceValidator, '__abstractmethods__')
        expected_methods = {
            'validate_sequence',
            'check_length_limit', 
            'detect_chain_type'
        }
        assert ISequenceValidator.__abstractmethods__ == expected_methods
    
    def test_structure_predictor_interface(self):
        """测试结构预测接口定义"""
        assert hasattr(IStructurePredictor, '__abstractmethods__')
        expected_methods = {
            'predict_structure',
            'get_prediction_status',
            'get_prediction_result',
            'cancel_prediction'
        }
        assert IStructurePredictor.__abstractmethods__ == expected_methods
    
    def test_visualization_interface(self):
        """测试可视化接口定义"""
        assert hasattr(IVisualization, '__abstractmethods__')
        expected_methods = {
            'display_structure',
            'set_display_style',
            'export_image',
            'enable_interaction',
            'get_view_state',
            'set_view_state'
        }
        assert IVisualization.__abstractmethods__ == expected_methods
    
    def test_cannot_instantiate_interfaces(self):
        """测试不能直接实例化接口"""
        with pytest.raises(TypeError):
            ISequenceValidator()
        
        with pytest.raises(TypeError):
            IStructurePredictor()
        
        with pytest.raises(TypeError):
            IVisualization()