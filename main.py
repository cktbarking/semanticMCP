from fastmcp import FastMCP
from dataclasses import dataclass
import requests
import time
import os
import sys
from typing import Dict, List, Any, Optional
from publishers_dict import detect_publisher_by_dict

# 添加当前目录到Python路径，以便能够导入publishers模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 自定义异常类，包含错误码信息
class APIRequestError(Exception):
    """API请求异常类"""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code
        self.message = message
    
    def __str__(self):
        if self.status_code:
            return f"API请求失败 (状态码: {self.status_code}): {self.message}"
        else:
            return f"API请求失败: {self.message}"

# 初始化FastMCP实例
mcp = FastMCP("Semantic Scholar API")

@mcp.tool()
def search_papers(query: str, limit: int = 5):
    """
    搜索学术论文
    :param query: 搜索查询字符串
    :param limit: 返回结果数量(默认5，最大100)
    """
    
    def search_semantic_scholar(query, limit=5):
        """
        搜索Semantic Scholar数据库
        :param query: 搜索查询字符串
        :param limit: 返回结果数量(默认5)
        :return: 搜索结果
        """
        # Semantic Scholar Search API端点
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        
        # 默认字段 - 添加externalIds以获取DOI信息
        
        fields = ["title", "authors", "abstract", "year", "citationCount", "url", "openAccessPdf", "externalIds"]
        
        # 查询参数
        params = {
            "query": query,
            "limit": limit,
            "fields": ",".join(fields)
        }
        
        try:
            # 发送请求
            response = requests.get(url, params=params)
            
            # 检查响应状态
            if response.status_code == 200:
                return response.json()
            else:
                # 抛出包含错误码的自定义异常
                raise APIRequestError(f"API请求失败: {response.status_code} - {response.text}", response.status_code)
        except requests.exceptions.RequestException as e:
            # 网络连接错误，没有具体的HTTP状态码
            raise APIRequestError(f"网络连接错误: {str(e)}")
    
    def format_search_results(results):
        """
        格式化搜索结果
        :param results: API返回的原始结果
        :return: 格式化的结果列表
        """
        formatted_results = []
        
        # 检查是否有搜索结果
        if "data" in results:
            papers = results["data"]
            
            for paper in papers:
                # 提取基本信息
                title = paper.get("title", "N/A")
                authors = ", ".join([author.get("name", "") for author in paper.get("authors", [])]) if paper.get("authors") else "N/A"
                abstract = paper.get("abstract", "N/A")
                year = paper.get("year", "N/A")
                citation_count = paper.get("citationCount", 0)
                url = paper.get("url", "N/A")
                
                # 提取PDF链接
                pdf_url = "N/A"
                if paper.get("openAccessPdf"):
                    pdf_url = paper["openAccessPdf"].get("url", "N/A")
                
                # 提取DOI信息 - 根据API文档，DOI在externalIds字段中
                doi = "N/A"
                doi_link = "N/A"
                external_ids = paper.get("externalIds", {})
                if external_ids and "DOI" in external_ids:
                    doi = external_ids["DOI"]
                    doi_link = f"https://doi.org/{doi}"
                
                # 构建格式化结果
                formatted_result = {
                    "title": title,
                    "authors": authors,
                    "abstract": abstract,
                    "year": year,
                    "citation_count": citation_count,
                    "article_url": url,
                    "pdf_url": pdf_url,
                    "doi": doi,
                    "doi_link": doi_link
                }
                
                formatted_results.append(formatted_result)
        
        return formatted_results
    
    import time
    
    max_retries = 5
    base_delay = 0.2  # 基础延时1秒
    
    for attempt in range(max_retries):
        try:
            # 调用Semantic Scholar API
            raw_results = search_semantic_scholar(query, limit)
            
            # 格式化结果
            formatted_results = format_search_results(raw_results)
            
            return {
                "success": True,
                "query": query,
                "count": len(formatted_results),
                "results": formatted_results
            }
        except APIRequestError as e:
            # 检查错误码是否为4开头（客户端错误）
            should_retry = False
            if e.status_code is not None and str(e.status_code).startswith('4'):
                should_retry = True
                print(f"检测到4xx错误码 {e.status_code}，将进行重试")
            else:
                print(f"检测到非4xx错误码或网络错误，不进行重试: {str(e)}")
            
            # 如果是最后一次尝试，或者不应该重试，直接返回错误
            if attempt == max_retries - 1 or not should_retry:
                return {
                    "success": False,
                    "error": str(e)
                }
            
            # 计算延时时间（指数退避策略）
            delay = base_delay * (2 ** attempt)
            print(f"第{attempt + 1}次尝试失败，{delay}秒后重试...")
            time.sleep(delay)
        except Exception as e:
            # 处理其他类型的异常（非APIRequestError）
            print(f"发生非API请求异常，不进行重试: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    # 理论上不会执行到这里，但为了完整性
    return {
        "success": False,
        "error": "未知错误"
    }

# 出版社识别和下载功能已集成到download_paper工具函数中
@mcp.tool()
def download_paper(doi: str, output_dir: str = "./pdfs"):
    """
    根据DOI下载论文PDF
    
    :param doi: 论文的DOI标识符
    :param output_dir: PDF输出目录（可选）
    :return: 下载结果信息
    """
    
    def ensure_output_directory(output_dir):
        """
        确保输出目录存在，如果不存在则创建
        
        :param output_dir: 输出目录路径
        :return: 无
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def download_paper_by_doi(doi, output_dir="./pdfs"):
        """
        根据DOI下载论文PDF
        
        :param doi: 论文DOI
        :param output_dir: 输出目录
        :return: 下载结果字典
        """
        if not doi:
            return {
                "success": False,
                "message": "DOI不能为空",
                "file_path": None,
                "doi": doi
            }
        
        # 确保输出目录存在
        ensure_output_directory(output_dir)
        
        # 构建DOI链接
        doi_link = f"https://doi.org/{doi}"
        
        # 识别出版社
        publisher = detect_publisher_by_dict(doi)
        print(f"识别到出版社: {publisher}")
        
        # 动态导入对应的下载器
        try:
            if publisher == "ieee":
                from publishers.ieee_downloader import download_ieee_paper
                result = download_ieee_paper(doi, doi_link, output_dir)
            elif publisher == "acm":
                from publishers.acm_downloader import download_acm_paper
                result = download_acm_paper(doi, doi_link, output_dir)
            elif publisher == "elsevier":
                from publishers.elsevier_downloader import download_elsevier_paper
                result = download_elsevier_paper(doi, doi_link, output_dir)
            elif publisher == "springer":
                from publishers.springer_downloader import download_springer_paper
                result = download_springer_paper(doi, doi_link, output_dir)
            elif publisher == "arxiv":
                # arXiv论文下载处理
                from publishers.arxiv_downloader import download_arxiv_paper
                result = download_arxiv_paper(doi, doi_link, output_dir)
            else:
                raise Exception("暂不支持的出版社")
            
        except ImportError as e:
            print(f"导入下载器时出错: {e}")
            result = {
                "success": False,
                "message": f"下载器导入失败: {str(e)}",
                "file_path": None,
                "doi": doi,
                "publisher": publisher
            }
        
        return result
    
    try:
        # 验证DOI参数
        if not doi or not isinstance(doi, str):
            return {
                "success": False,
                "message": "无效的DOI参数",
                "error": "DOI必须是非空字符串"
            }
        
        # 调用下载管理器下载论文
        result = download_paper_by_doi(doi, output_dir)
        
        # 返回下载结果
        return {
            "success": result["success"],
            "message": result["message"],
            "file_path": result["file_path"],
            "doi": result["doi"],
            "publisher": result.get("publisher", "Unknown")
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "下载过程中发生错误",
            "doi": doi
        }

def main():
    """Main entry point for uvx execution"""
    # 运行FastMCP服务器
    mcp.run()

if __name__ == "__main__":
    # 运行FastMCP服务器
    main()