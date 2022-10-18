#!/usr/bin/env python

from distutils.core import setup


long_description = '''

机器学习

作者：蔡猛

模块说明

    learning
       |
       |---- apriori
                |
                |---- def freq_one(data) 生成频繁1项集
                |
                |---- def get_subset(item, k) 得到所有k项子集
                |
                |---- def get_all_subsets_not_self(item) 得到所有非空子集并剔除自身
                |
                |---- def freq_k(data, frequent_k_minus_one, k, min_support=2) 生成频繁k项集 k>=2
                |
                |---- def frequent_final(data, freq_one, min_support=2) 生成最终频繁项集
                |
                |---- def frequent_all(data, freq_one, min_support=2) 生成所有频繁项集
                |
                |---- def rule(data, freq_one, min_support=2, min_confidence=0.6) 生成关联规则
                |
                |---- def load_example() 示例数据
                |
                |---- def load_movie() 电影高评数据

模块安装

    Windows系统：请在当前目录下运行 python setup.py install
    
    Linux系统：请在当前目录下运行 python3 setup.py install

'''

setup(
    name='machine-learning',
    version='2.1.3',
    author='蔡猛',
    author_email='13683277331@163.com',
    keywords=['Apriori'],
    long_description=long_description,
    packages=['learning']
)


