"""
简历ATS关键词匹配率计算脚本
用于扣子工作流Code节点

输入：resume_text（简历文本）, jd_analysis_json（JD解析结果JSON）
输出：match_report（匹配报告字典）
"""

import json
import re


def main(resume_text: str, jd_analysis_json: str) -> dict:
    """
    计算简历与JD的关键词匹配率，并检查简历结构完整性。

    Args:
        resume_text: 用户原始简历文本
        jd_analysis_json: 上一节点JD解析输出的JSON字符串
            格式: {
                "hard_skills": ["skill1", ...],
                "soft_skills": ["skill1", ...],
                "industry_keywords": ["kw1", ...]
            }

    Returns:
        匹配报告字典
    """
    resume_lower = resume_text.lower() if resume_text else ""

    # 解析JD
    try:
        jd_data = json.loads(jd_analysis_json) if isinstance(jd_analysis_json, str) else jd_analysis_json
    except (json.JSONDecodeError, TypeError):
        jd_data = {}

    # 聚合所有关键词
    hard_skills = jd_data.get("hard_skills", [])
    soft_skills = jd_data.get("soft_skills", [])
    industry_kw = jd_data.get("industry_keywords", [])

    all_keywords = hard_skills + soft_skills + industry_kw

    # 匹配检测
    matched = []
    missing = []

    for kw in all_keywords:
        if kw.lower() in resume_lower:
            matched.append(kw)
        else:
            missing.append(kw)

    total_kw = len(all_keywords)
    match_rate = round(len(matched) / max(total_kw, 1) * 100)

    # 结构完整性检查
    structure = {
        "联系方式": bool(re.search(r'(电话|手机|邮箱|[\d]{3}[-]?\d{4}[-]?\d{4}|@)', resume_text or "")),
        "求职意向": bool(re.search(r'(求职意向|期望职位|目标岗位|应聘|意向)', resume_text or "")),
        "教育经历": bool(re.search(r'(学历|学校|大学|本科|硕士|博士|GPA|毕业)', resume_text or "")),
        "工作经历": bool(re.search(r'(工作经历|工作经验|实习经历|任职)', resume_text or "")),
        "项目经历": bool(re.search(r'(项目经历|项目经验|Project)', resume_text or "")),
        "专业技能": bool(re.search(r'(技能|技术栈|专业技能|证书|语言能力)', resume_text or "")),
        "自我评价": bool(re.search(r'(自我评价|个人简介|自我介绍|关于我)', resume_text or "")),
    }

    structure_complete = sum(1 for v in structure.values() if v)
    structure_score = round(structure_complete / 7 * 20)

    # 综合评分
    health_score = round(match_rate * 0.4 + 30 * (1 if structure_complete >= 6 else 0.5) + structure_score)

    return {
        "matched_keywords": matched,
        "missing_keywords": missing,
        "match_rate": match_rate,
        "structure_report": {k: "✅" if v else "❌" for k, v in structure.items()},
        "structure_complete": structure_complete,
        "total_modules": 7,
        "structure_score": structure_score,
        "health_score": min(health_score, 100),
        "total_keywords_scanned": total_kw,
    }
