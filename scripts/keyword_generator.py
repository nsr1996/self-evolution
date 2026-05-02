#!/usr/bin/env python3
"""
行路 · 随机关键词生成器
从关键词库中随机组合探索主题
"""

import random
import json
import sys

# 核心关键词
CORE_ZH = [
    "AI", "fintech", "人工智能投资", "一人公司", "新范式",
    "AI新概念", "个人创业机会", "个人投资机会", "数字游民"
]

CORE_EN = [
    "AI", "fintech", "AI investment", "solopreneur", "new paradigm",
    "emerging AI concepts", "indie hacking", "personal investment", "digital nomad"
]

# 衍生关键词
DERIVED_ZH = [
    "AI Agent", "大模型应用", "AI编程", "去中心化金融",
    "量化投资", "加密货币", "知识付费", "自动化创业",
    "个人品牌", "小型SaaS", "无代码", "个人出海",
    "内容创业", "社区驱动", "AI概念股"
]

DERIVED_EN = [
    "AI agents", "LLM applications", "vibe coding", "DeFi",
    "quantitative investing", "cryptocurrency", "creator economy",
    "automation entrepreneurship", "personal branding", "micro SaaS",
    "no-code", "global indie", "content entrepreneurship",
    "community-driven", "AI concept stocks"
]

# 组合模板
COMBO_TEMPLATES = [
    ("AI", "一人公司", "AI驱动的个人创业"),
    ("fintech", "AI", "AI金融科技交叉"),
    ("数字游民", "AI编程", "远程工作+产品开发"),
    ("AI新概念", "投资", "AI领域投资机会"),
    ("新范式", "个人创业", "新范式下的创业模式"),
    ("量化投资", "AI", "AI驱动的投资策略"),
    ("知识付费", "AI", "AI时代的知识变现"),
    ("小型SaaS", "AI", "AI增强的微SaaS"),
    ("DeFi", "个人投资", "去中心化金融投资机会"),
    ("个人品牌", "AI", "AI时代的个人IP打造"),
]


def random_walk(n=3):
    """随机漫步：从核心+衍生关键词中随机选n个"""
    all_kw = CORE_ZH + DERIVED_ZH
    selected = random.sample(all_kw, min(n, len(all_kw)))
    return selected


def random_combo():
    """随机组合：返回一个组合模板"""
    return random.choice(COMBO_TEMPLATES)


def generate_search_queries(keywords):
    """根据关键词生成搜索查询"""
    queries = []
    for kw in keywords:
        # 找到对应的英文
        idx_zh = -1
        if kw in CORE_ZH:
            idx_zh = CORE_ZH.index(kw)
            queries.append(f"site:reddit.com {CORE_EN[idx_zh]}")
        elif kw in DERIVED_ZH:
            idx_zh = DERIVED_ZH.index(kw)
            queries.append(f"site:reddit.com {DERIVED_EN[idx_zh]}")
        else:
            queries.append(f"site:reddit.com {kw}")
    return queries


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "walk"
    
    if mode == "walk":
        keywords = random_walk()
        queries = generate_search_queries(keywords)
        result = {
            "mode": "random_walk",
            "keywords": keywords,
            "search_queries": queries
        }
    elif mode == "combo":
        combo = random_combo()
        result = {
            "mode": "random_combo",
            "keywords": [combo[0], combo[1]],
            "theme": combo[2],
            "search_queries": generate_search_queries([combo[0], combo[1]])
        }
    else:
        result = {"error": f"Unknown mode: {mode}. Use 'walk' or 'combo'."}
    
    print(json.dumps(result, ensure_ascii=False, indent=2))
