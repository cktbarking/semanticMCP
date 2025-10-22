#!/usr/bin/env python3
"""
arXiv论文下载脚本
用于从arXiv预印本服务器下载论文PDF
"""

import os
import requests
import re
from urllib.parse import urlparse

def download_arxiv_paper(doi, doi_link, output_dir="./pdfs"):
    """
    下载arXiv预印本论文
    
    :param doi: 论文DOI
    :param doi_link: 完整的DOI链接
    :param output_dir: 输出目录
    :return: 下载结果字典，包含success、file_path、error等字段
    """
    print(f"[arXiv] 尝试下载论文: {doi}")
    print(f"[arXiv] DOI链接: {doi_link}")
    
    try:
        # 从DOI中提取arXiv ID
        # arXiv DOI格式: 10.48550/arXiv.2307.07697
        arxiv_id = extract_arxiv_id_from_doi(doi)
        if not arxiv_id:
            return {
                "success": False,
                "message": "无法从DOI中提取arXiv ID",
                "file_path": None,
                "doi": doi,
                "publisher": "arXiv"
            }
        
        # 构建arXiv PDF下载链接
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        print(f"[arXiv] PDF下载链接: {pdf_url}")
        
        # 发送请求下载PDF
        response = requests.get(pdf_url, stream=True, timeout=30)
        
        if response.status_code == 200:
            # 确保输出目录存在
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # 构建保存路径
            filename = f"{arxiv_id}.pdf"
            file_path = os.path.join(output_dir, filename)
            
            # 保存PDF文件
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"[arXiv] 论文下载成功: {file_path}")
            
            return {
                "success": True,
                "message": "arXiv论文下载成功",
                "file_path": file_path,
                "doi": doi,
                "publisher": "arXiv",
                "arxiv_id": arxiv_id
            }
        else:
            error_msg = f"下载失败，HTTP状态码: {response.status_code}"
            print(f"[arXiv] {error_msg}")
            return {
                "success": False,
                "message": error_msg,
                "file_path": None,
                "doi": doi,
                "publisher": "arXiv"
            }
            
    except requests.exceptions.RequestException as e:
        error_msg = f"网络请求错误: {str(e)}"
        print(f"[arXiv] {error_msg}")
        return {
            "success": False,
            "message": error_msg,
            "file_path": None,
            "doi": doi,
            "publisher": "arXiv"
        }
    except Exception as e:
        error_msg = f"下载过程中发生错误: {str(e)}"
        print(f"[arXiv] {error_msg}")
        return {
            "success": False,
            "message": error_msg,
            "file_path": None,
            "doi": doi,
            "publisher": "arXiv"
        }

def extract_arxiv_id_from_doi(doi):
    """
    从DOI中提取arXiv ID
    
    :param doi: 论文DOI
    :return: arXiv ID，如果无法提取则返回None
    """
    # arXiv DOI格式: 10.48550/arXiv.2307.07697
    # 或者: 10.48550/arXiv.2307.07697v6
    
    # 匹配arXiv DOI模式
    pattern = r'10\.48550/arXiv\.([A-Za-z0-9\.\-]+)'
    match = re.search(pattern, doi)
    
    if match:
        arxiv_id = match.group(1)
        # 移除版本后缀（如果有）
        if 'v' in arxiv_id:
            arxiv_id = arxiv_id.split('v')[0]
        return arxiv_id
    
    # 如果DOI不匹配标准格式，尝试直接提取arXiv ID
    if 'arxiv' in doi.lower():
        # 尝试从DOI中提取数字部分
        numbers = re.findall(r'\d+\.\d+', doi)
        if numbers:
            return numbers[0]
    
    return None

def download_arxiv_paper_by_id(arxiv_id, output_dir="./pdfs"):
    """
    直接通过arXiv ID下载论文
    
    :param arxiv_id: arXiv ID（如2307.07697）
    :param output_dir: 输出目录
    :return: 下载结果字典
    """
    # 构建DOI
    doi = f"10.48550/arXiv.{arxiv_id}"
    return download_arxiv_paper(doi, f"https://doi.org/{doi}", output_dir)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        doi_or_id = sys.argv[1]
        
        # 判断是DOI还是arXiv ID
        if doi_or_id.startswith('10.'):
            # 是DOI
            doi_link = f"https://doi.org/{doi_or_id}"
            result = download_arxiv_paper(doi_or_id, doi_link)
        else:
            # 是arXiv ID
            result = download_arxiv_paper_by_id(doi_or_id)
        
        print(result)
    else:
        print("请提供DOI或arXiv ID作为参数")
        print("示例DOI: 10.48550/arXiv.2307.07697")
        print("示例arXiv ID: 2307.07697")