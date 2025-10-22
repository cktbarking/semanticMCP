# Semantic Scholar MCP Server

一个基于FastMCP框架的Semantic Scholar学术搜索引擎工具，可以搜索学术论文并下载PDF文件。支持通过MCP协议与各种AI助手集成。

## 功能特性

1. 🔍 **学术论文搜索** - 搜索Semantic Scholar数据库
2. 📄 **PDF下载** - 自动识别出版社并下载论文PDF
3. 🔗 **DOI解析** - 支持通过DOI获取论文信息
4. 🏢 **多出版社支持** - 支持IEEE、ACM、Elsevier、Springer、arXiv等
5. 🛠️ **MCP协议** - 兼容Model Context Protocol

## 快速开始

### 使用uvx运行（推荐）

```bash
# 安装并运行MCP服务器
uvx semantic-scholar-mcp --transport stdio

# 或者指定版本
uvx semantic-scholar-mcp@latest --transport stdio
```

### 本地开发

```bash
# 克隆项目
git clone <repository-url>
cd semantic-scholar-mcp

# 安装依赖
uv sync

# 运行服务器
uv run semantic-scholar-mcp --transport stdio
```

### 传统方式

```bash
# 安装依赖
pip install -r requirements.txt

# 运行服务
python main.py
```

## MCP工具

### 1. search_papers - 搜索论文

搜索Semantic Scholar数据库中的学术论文。

**参数：**
- `query` (str, 必需): 搜索查询字符串
- `limit` (int, 可选): 返回结果数量，默认5，最大100

**返回：**
包含论文标题、作者、摘要、年份、引用次数、DOI、PDF链接等信息的列表。

### 2. download_paper - 下载论文PDF

根据DOI下载论文PDF文件，自动识别出版社。

**参数：**
- `doi` (str, 必需): 论文的DOI标识符
- `output_dir` (str, 可选): PDF输出目录，默认"./pdfs"

**支持的出版社：**
- IEEE (10.1109/*)
- ACM (10.1145/*)
- Elsevier (10.1016/*)
- Springer (10.1007/*)
- arXiv (10.48550/arXiv.*)

**返回：**
下载结果信息，包括成功状态、文件路径、出版社等。

## 响应格式

### 搜索响应示例
```json
{
  "success": true,
  "query": "machine learning",
  "count": 5,
  "results": [
    {
      "title": "Deep Learning for Computer Vision",
      "authors": "John Doe, Jane Smith",
      "abstract": "This paper presents...",
      "year": 2023,
      "citation_count": 150,
      "article_url": "https://...",
      "pdf_url": "https://...",
      "doi": "10.1109/...",
      "doi_link": "https://doi.org/10.1109/..."
    }
  ]
}
```

### 下载响应示例
```json
{
  "success": true,
  "message": "PDF下载成功",
  "file_path": "./pdfs/10.1109_example.pdf",
  "doi": "10.1109/example",
  "publisher": "ieee"
}
```

## 配置MCP客户端

### Claude Desktop配置

在Claude Desktop的配置文件中添加：

```json
{
  "mcpServers": {
    "semantic-scholar": {
      "command": "uvx",
      "args": ["semantic-scholar-mcp", "--transport", "stdio"]
    }
  }
}
```

### 其他MCP客户端

支持任何兼容MCP协议的客户端，只需配置命令为：
```bash
uvx semantic-scholar-mcp --transport stdio
```

## 开发说明

### 项目结构
```
semantic-scholar-mcp/
├── main.py                 # MCP服务器主文件
├── publishers/             # 出版社下载器
│   ├── ieee_downloader.py
│   ├── acm_downloader.py
│   ├── elsevier_downloader.py
│   ├── springer_downloader.py
│   ├── arxiv_downloader.py
│   └── generic_downloader.py
├── pyproject.toml          # 项目配置
├── requirements.txt        # 依赖列表
└── README.md              # 说明文档
```

### 添加新的出版社支持

1. 在`publishers/`目录下创建新的下载器文件
2. 实现下载函数，接受`doi`, `doi_link`, `output_dir`参数
3. 在`publishers_dict.py`的`PUBLISHER_DICT`字典中添加DOI前缀到出版社的映射
4. 在`download_paper_by_doi()`函数中添加对应的处理分支

## 注意事项

1. **API限制** - Semantic Scholar API有调用频率限制，请合理使用
2. **版权合规** - 下载的PDF文件仅供个人学术研究使用
3. **网络要求** - 某些出版社可能需要机构访问权限,请合理使用。
4. **Python版本** - 需要Python 3.10或更高版本

## 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 致谢

- [Semantic Scholar](https://www.semanticscholar.org/) 提供优秀的学术搜索API
- [FastMCP](https://github.com/jlowin/fastmcp) 简化MCP服务器开发
- 各大学术出版社提供的研究资源
