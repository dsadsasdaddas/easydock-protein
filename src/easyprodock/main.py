"""
EasyProDock主程序入口

提供命令行和GUI启动功能。
"""

import sys
import argparse
from typing import Optional


def main(args: Optional[list] = None) -> int:
    """主程序入口函数
    
    Args:
        args: 命令行参数列表，如果为None则使用sys.argv
        
    Returns:
        int: 程序退出码
    """
    if args is None:
        args = sys.argv[1:]
    
    parser = argparse.ArgumentParser(
        description="EasyProDock - 蛋白质结构预测与分子对接一体化桌面软件",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="EasyProDock 0.1.0"
    )
    
    parser.add_argument(
        "--gui",
        action="store_true",
        default=True,
        help="启动图形用户界面（默认）"
    )
    
    parser.add_argument(
        "--cli",
        action="store_true",
        help="启动命令行界面"
    )
    
    parsed_args = parser.parse_args(args)
    
    try:
        if parsed_args.cli:
            print("命令行界面将在后续版本中实现")
            return 0
        else:
            print("图形用户界面将在后续版本中实现")
            print("EasyProDock v0.1.0 - 项目结构已初始化")
            return 0
            
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        return 1
    except Exception as e:
        print(f"程序运行出错: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())