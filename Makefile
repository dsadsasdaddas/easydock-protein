# EasyProDock Makefile

.PHONY: help install test clean lint format run

help:
	@echo "EasyProDock 开发工具"
	@echo ""
	@echo "可用命令:"
	@echo "  install    安装依赖包"
	@echo "  test       运行测试"
	@echo "  clean      清理临时文件"
	@echo "  lint       代码检查"
	@echo "  format     代码格式化"
	@echo "  run        运行程序"

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest

test-verbose:
	pytest -v

test-coverage:
	pytest --cov=src/easyprodock --cov-report=html

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/

run:
	python -m easyprodock.main

run-gui:
	python -m easyprodock.main --gui

run-cli:
	python -m easyprodock.main --cli