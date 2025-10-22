"""
出版社识别字典

该文件包含DOI前缀到出版社的映射字典，用于快速识别论文所属出版社
"""

# 出版社识别字典
PUBLISHER_DICT = {
    # IEEE相关
    "10.1109": "ieee",
    "ieee": "ieee",
    
    # ACM相关
    "10.1145": "acm", 
    "acm": "acm",
    
    # Elsevier相关
    "10.1016": "elsevier",
    "elsevier": "elsevier",
    "sciencedirect": "elsevier",
    
    # Springer相关
    "10.1007": "springer",
    "springer": "springer",
    
    # Nature相关
    "10.1038": "nature",
    "nature": "nature",
    
    # Science相关
    "10.1126": "science",
    "science": "science",
    
    # PLOS相关
    "10.1371": "plos",
    "plos": "plos",
    
    # Oxford University Press
    "10.1093": "oup",
    "oup": "oup",
    
    # SAGE相关
    "10.1177": "sage",
    "sage": "sage",
    
    # Wiley相关
    "10.1002": "wiley",
    "wiley": "wiley",
    
    # Taylor & Francis相关
    "10.1080": "taylor_francis",
    "taylor": "taylor_francis",
    "francis": "taylor_francis",
    
    # Society for Neuroscience
    "10.1523": "sfn",
    "jneurosci": "sfn",
    
    # PNAS相关
    "10.1073": "pnas",
    "pnas": "pnas",
    
    # Royal Society of Chemistry
    "10.1039": "rsc",
    "rsc": "rsc",
    
    # American Chemical Society
    "10.1021": "acs",
    "acs": "acs",
    
    # BMJ相关
    "10.1136": "bmj",
    "bmj": "bmj",
    
    # Thieme相关
    "10.1055": "thieme",
    "thieme": "thieme",
    
    # W.B. Saunders
    "10.1053": "surgical",
    "surgical": "surgical",
    
    # Wiley-Blackwell
    "10.1111": "wiley_blackwell",
    "blackwell": "wiley_blackwell",
    "wiley-blackwell": "wiley_blackwell",
    
    # American Society of Clinical Oncology
    "10.1200": "asco",
    "asco": "asco",
    
    # Europhysics Letters
    "10.1209": "epl",
    "epl": "epl",
    
    # Company of Biologists
    "10.1242": "company_of_biologists",
    "jeb": "company_of_biologists",
    
    # Genetics Society of America
    "10.1534": "genetics",
    "genetics": "genetics",
    
    # Ecological Society of America
    "10.1890": "esa",
    "esa": "esa",
    
    # JSTOR相关
    "10.2307": "jstor",
    "jstor": "jstor",
    
    # De Gruyter相关
    "10.1515": "degruyter",
    "degruyter": "degruyter",
    
    # MIT Press相关
    "10.1162": "mit_press",
    "mit": "mit_press",
    
    # American Institute of Physics
    "10.1063": "aip",
    "aip": "aip",
    
    # bioRxiv相关
    "10.1101": "biorxiv",
    "biorxiv": "biorxiv",
    
    # American Society for Microbiology
    "10.1128": "asm",
    "asm": "asm",
    
    # American Physiological Society
    "10.1152": "physiology",
    "physiology": "physiology",
    
    # BioMed Central相关
    "10.1186": "biomedcentral",
    "biomedcentral": "biomedcentral",
    "bmc": "biomedcentral",
    
    # American Society of Hematology
    "10.1182": "blood",
    "blood": "blood",
    
    # American Association of Pharmaceutical Scientists
    "10.1208": "aaps",
    "aaps": "aaps",
    
    # Endocrine Society
    "10.1210": "endocrine",
    "endocrine": "endocrine",
    
    # American Academy of Neurology
    "10.1212": "neurology",
    "neurology": "neurology",
    
    # Institute for Operations Research and the Management Sciences
    "10.1287": "informs",
    "informs": "informs",
    
    # Optical Society of America
    "10.1364": "osa",
    "osa": "osa",
    
    # American Public Health Association
    "10.1370": "ajph",
    "ajph": "ajph",
    
    # American College of Chest Physicians
    "10.1378": "chest",
    "chest": "chest",
    
    # Humana相关
    "10.1385": "humana",
    "humana": "humana",
    
    # Silva Fennica
    "10.14214": "silva",
    "silva": "silva",
    
    # International Union of Crystallography
    "10.14469": "iucr",
    "crystallography": "iucr",
    
    # University of California Press
    "10.1525": "uc_press",
    "ucpress": "uc_press",
    
    # Bioscientifica相关
    "10.1530": "bioscientifica",
    "bioscientifica": "bioscientifica",
    
    # American Fisheries Society
    "10.1577": "afs",
    "afs": "afs",
    
    # Botanical Society of America
    "10.1600": "botany",
    "botany": "botany",
    
    # American Institute of Biological Sciences
    "10.1641": "bioscience",
    "bioscience": "bioscience",
    
    # Paleontological Society
    "10.1671": "jpaleontology",
    "jpaleontology": "jpaleontology",
    
    # Slack Inc.
    "10.1891": "rehab",
    "rehab": "rehab",
    
    # Society for the Experimental Analysis of Behavior
    "10.1901": "jaba",
    "jaba": "jaba",
    
    # International Association for Dental Research
    "10.1922": "jdr",
    "jdr": "jdr",
    
    # Society of Petroleum Engineers
    "10.2118": "spe",
    "spe": "spe",
    
    # Journal of Orthodontics
    "10.2144": "joponline",
    "joponline": "joponline",
    
    # Baywood Publishing
    "10.2190": "jap",
    "jap": "jap",
    
    # American Roentgen Ray Society
    "10.2214": "ajr",
    "ajr": "ajr",
    
    # American Society of Nephrology
    "10.2215": "cjn",
    "cjn": "cjn",
    
    # Future Medicine
    "10.2217": "fmc",
    "fmc": "fmc",
    
    # Journal of Prosthodontics
    "10.2223": "jop",
    "jop": "jop",
    
    # Authorea Preprints
    "10.22541": "preprints",
    "preprints": "preprints",
    
    # Science China
    "10.2306": "scichina",
    "scichina": "scichina",
    
    # American Diabetes Association
    "10.2337": "diabetes",
    "diabetes": "diabetes",
    
    # American Society for Clinical Pathology
    "10.2353": "ajcp",
    "ajcp": "ajcp",
    
    # Journal of Preventive Medicine and Hygiene
    "10.23750": "jpm",
    "jpm": "jpm",
    
    # Peer Community In
    "10.24072": "pci",
    "pci": "pci",
    
    # International Journal of Language Studies
    "10.24218": "ijls",
    "ijls": "ijls",
    
    # De Gruyter Open
    "10.2478": "versita",
    "versita": "versita",
    
    # American Institute of Aeronautics and Astronautics
    "10.2514": "aiaa",
    "aiaa": "aiaa",
    
    # American Society of Animal Science
    "10.2527": "jas",
    "jas": "jas",
    
    # EarthArXiv
    "10.25573": "eartharxiv",
    "eartharxiv": "eartharxiv",
    
    # European Food Safety Authority
    "10.25646": "efsa",
    "efsa": "efsa",
    
    # Remote Sensing
    "10.26207": "jrs",
    "jrs": "jrs",
    
    # Scientia Pharmaceutica
    "10.26320": "scientia",
    "scientia": "scientia",
    
    # Journal of Communications and Networks
    "10.26866": "jcn",
    "jcn": "jcn",
    
    # Frontiers相关
    "10.2741": "frontiers",
    "frontiers": "frontiers",
    
    # Atlantis Press
    "10.2991": "atlantis",
    "atlantis": "atlantis",
    
    # Botanica Lithuanica
    "10.3140": "bc",
    "bc": "bc",
    
    # Centers for Disease Control and Prevention
    "10.3201": "cdc",
    "cdc": "cdc",
    
    # IOS Press
    "10.3233": "ios",
    "ios": "ios",
    
    # MDPI相关
    "10.3390": "mdpi",
    "mdpi": "mdpi",
    
    # F1000 Research
    "10.3410": "f1000",
    "f1000": "f1000",
    
    # Institute of Physics
    "10.3847": "iop",
    "iop": "iop",
    
    # Pensoft相关
    "10.3897": "pensoft",
    "pensoft": "pensoft",
    
    # IGI Global
    "10.4018": "igi",
    "igi": "igi",
    
    # arXiv预印本
    "10.48550": "arxiv",
    "arxiv": "arxiv",
    
    # Medknow相关
    "10.4103": "medknow",
    "medknow": "medknow",
    
    # OMICS Publishing Group
    "10.4172": "omics",
    "omics": "omics",
    
    # Scientific Research Publishing
    "10.4236": "scirp",
    "scirp": "scirp",
    
    # World Journal of Gastroenterology
    "10.4239": "wjg",
    "wjg": "wjg",
    
    # Figshare相关
    "10.4251": "figshare",
    "figshare": "figshare",
    
    # PeerJ相关
    "10.4252": "peerj",
    "peerj": "peerj",
    
    # Pensoft Publishers
    "10.4253": "zookeys",
    "zookeys": "zookeys",
    
    # Molecular Biology and Evolution
    "10.4256": "mbe",
    "mbe": "mbe",
    
    # American Journal of Tropical Medicine and Hygiene
    "10.4269": "ajtmh",
    "ajtmh": "ajtmh",
    
    # Copernicus相关
    "10.5194": "copernicus",
    "copernicus": "copernicus",
    
    # Ubiquity Press
    "10.5334": "ubiquity",
    "ubiquity": "ubiquity",
    
    # American Association of Physics Teachers
    "10.5408": "aapt",
    "aapt": "aapt",
    
    # Journal of Applied Poultry Research
    "10.5411": "japr",
    "japr": "japr",
    
    # Applied Clinical Informatics
    "10.5414": "apcc",
    "apcc": "apcc",
    
    # International Journal of Medical Students
    "10.5455": "ijms",
    "ijms": "ijms",
    
    # Pharmacognosy
    "10.5530": "phcog",
    "phcog": "phcog",
    
    # Natural Resources Canada
    "10.5558": "nrc",
    "nrc": "nrc",
    
    # Journal of Learning Analytics
    "10.5617": "jla",
    "jla": "jla",
    
    # Acta Biochimica et Biophysica Sinica
    "10.5713": "abbs",
    "abbs": "abbs",
    
    # Iranian Red Crescent Medical Journal
    "10.5812": "ircmj",
    "ircmj": "ircmj",
    
    # African Journal of Business Management
    "10.5897": "ajb",
    "ajb": "ajb",
    
    # NIST相关
    "10.6028": "nist",
    "nist": "nist",
    
    # Clinics相关
    "10.6061": "clinics",
    "clinics": "clinics",
    
    # International Journal of Biological Sciences
    "10.7150": "ijbs",
    "ijbs": "ijbs",
    
    # Asian Pacific Journal of Cancer Prevention
    "10.7314": "apocp",
    "apocp": "apocp",
    
    # Annals of Internal Medicine
    "10.7326": "annals",
    "annals": "annals",
    
    # Journal of Clinical and Diagnostic Research
    "10.7860": "jcdr",
    "jcdr": "jcdr",
    
    # Clinical Medicine
    "10.7861": "clinmed",
    "clinmed": "clinmed",
}

def detect_publisher_by_dict(doi):
    """
    使用字典查询方式识别出版社
    
    :param doi: 论文DOI
    :return: 出版社标识符，如果未识别则返回"generic"
    """
    doi_lower = doi.lower()
    
    # 首先检查DOI前缀
    for prefix, publisher in PUBLISHER_DICT.items():
        if prefix in doi_lower:
            return publisher
    
    # 如果前缀未匹配，检查关键词
    for keyword, publisher in PUBLISHER_DICT.items():
        if len(keyword) > 5 and keyword in doi_lower:  # 只检查长度大于5的关键词
            return publisher
    
    # 默认返回通用出版社
    return "generic"