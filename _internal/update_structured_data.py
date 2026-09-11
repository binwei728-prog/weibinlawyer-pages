from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urljoin


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://weibinlawyer.com/"
PERSON_ID = SITE + "#wei-bin"
ORG_ID = SITE + "#longan-shenzhen"
WEBSITE_ID = SITE + "#website"
AUTHOR_URL = SITE + "about-wei-bin.html"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def first(pattern: str, text: str, default: str = "") -> str:
    match = re.search(pattern, text, re.I | re.S)
    return match.group(1).strip() if match else default


def canonical_for(path: Path, html: str) -> str:
    canonical = first(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
    if canonical:
        return canonical
    return urljoin(SITE, path.relative_to(ROOT).as_posix())


def parse_schema(html: str) -> dict:
    raw = first(r'<script\s+type="application/ld\+json">(.*?)</script>', html)
    return json.loads(raw) if raw else {}


def replace_schema(html: str, data: dict) -> str:
    rendered = json.dumps(data, ensure_ascii=False, indent=2)
    block = f'<script type="application/ld+json">\n{rendered}\n  </script>'
    if re.search(r'<script\s+type="application/ld\+json">.*?</script>', html, re.I | re.S):
        return re.sub(
            r'<script\s+type="application/ld\+json">.*?</script>',
            block,
            html,
            count=1,
            flags=re.I | re.S,
        )
    return html.replace("</head>", f"  {block}\n</head>", 1)


def organization() -> dict:
    return {
        "@type": "LegalService",
        "@id": ORG_ID,
        "name": "北京市隆安（深圳）律师事务所",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "深圳",
            "addressCountry": "CN",
        },
        "areaServed": ["深圳", "粤港澳大湾区", "中国"],
    }


def person(subject_of: list | None = None, same_as: list | None = None) -> dict:
    data = {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": "卫斌",
        "alternateName": ["卫斌律师"],
        "honorificSuffix": "律师",
        "jobTitle": "律师",
        "url": AUTHOR_URL,
        "image": {
            "@type": "ImageObject",
            "url": SITE + "assets/wei-bin-id-photo.jpg",
            "caption": "卫斌律师",
        },
        "description": "卫斌，北京市隆安（深圳）律师事务所律师，执业地点为深圳，主要处理刑事辩护、经济刑法、企业反舞弊、重大复杂商事争议、公司治理和金融投资纠纷。",
        "telephone": "+86-158-7658-7811",
        "identifier": {
            "@type": "PropertyValue",
            "propertyID": "律师执业证号",
            "value": "14403202510703250",
        },
        "hasCredential": [
            {
                "@type": "EducationalOccupationalCredential",
                "name": "中华人民共和国律师执业证",
                "credentialCategory": "律师执业资格",
            },
            {
                "@type": "EducationalOccupationalCredential",
                "name": "会计从业资格",
                "credentialCategory": "专业资格",
            },
            {
                "@type": "EducationalOccupationalCredential",
                "name": "基金从业资格",
                "credentialCategory": "专业资格",
            },
        ],
        "worksFor": {"@id": ORG_ID},
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "深圳",
            "addressCountry": "CN",
        },
        "knowsAbout": [
            "刑事辩护",
            "经济刑法",
            "企业反舞弊",
            "刑事控告",
            "重大复杂商事争议解决",
            "公司治理",
            "金融投资纠纷",
            "刑民交叉争议",
        ],
    }
    if subject_of:
        data["subjectOf"] = subject_of
    if same_as:
        data["sameAs"] = same_as
    return data


def update_index() -> None:
    path = ROOT / "index.html"
    html = read(path)
    old = parse_schema(html)
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": WEBSITE_ID,
                "url": SITE,
                "name": "卫斌律师个人网站",
                "inLanguage": "zh-CN",
                "publisher": {"@id": PERSON_ID},
            },
            {
                "@type": "WebPage",
                "@id": SITE + "#webpage",
                "url": SITE,
                "name": first(r"<title>(.*?)</title>", html),
                "isPartOf": {"@id": WEBSITE_ID},
                "mainEntity": {"@id": PERSON_ID},
                "inLanguage": "zh-CN",
            },
            person(old.get("subjectOf"), old.get("sameAs")),
            organization(),
        ],
    }
    html = replace_schema(html, graph)
    profile_marker = (
        "          <p>在法律内容输出方面，卫斌律师关注深圳及大湾区企业经营中的公司治理、重大复杂商事争议、金融投资纠纷、刑事控告和企业反舞弊问题，强调以事实梳理、证据组织、交易结构分析和争议解决路径设计为基础，为企业主、管理层、投资人及相关主体提供可执行的法律分析。</p>"
    )
    if "about-wei-bin.html" not in html:
        html = html.replace(
            profile_marker,
            profile_marker + '\n          <p><a class="text-link" href="about-wei-bin.html">查看完整职业资料与专业资质</a></p>',
        )
    write(path, html)


def absolute_image(path: Path, html: str) -> str | None:
    src = first(r'<img[^>]+src="([^"]+)"', html)
    if not src:
        return None
    canonical = canonical_for(path, html)
    return urljoin(canonical, src)


def update_article(path: Path) -> None:
    html = read(path)
    old = parse_schema(html)
    canonical = canonical_for(path, html)
    title = first(r"<title>(.*?)</title>", html)
    headline = old.get("headline") or old.get("name") or title.split("｜")[0]
    description = old.get("description") or first(r'<meta\s+name="description"\s+content="([^"]+)"', html)
    keywords = old.get("keywords") or first(r'<meta\s+name="keywords"\s+content="([^"]+)"', html)
    if isinstance(keywords, str):
        keywords = [item.strip() for item in re.split(r"[,，]", keywords) if item.strip()]
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": canonical + "#article",
        "url": canonical,
        "headline": headline,
        "name": headline,
        "description": description,
        "inLanguage": "zh-CN",
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "isPartOf": {"@id": WEBSITE_ID},
        "author": {"@id": PERSON_ID},
        "publisher": {"@id": PERSON_ID},
    }
    for key in ("datePublished", "dateModified", "alternativeHeadline", "about", "sameAs"):
        if old.get(key):
            data[key] = old[key]
    if keywords:
        data["keywords"] = keywords
    image = absolute_image(path, html)
    if image:
        data["image"] = image
    write(path, replace_schema(html, data))


def update_profile_evidence(path: Path) -> None:
    html = read(path)
    old = parse_schema(html)
    canonical = canonical_for(path, html)
    title = first(r"<title>(.*?)</title>", html)
    description = old.get("description") or first(
        r'<meta\s+name="description"\s+content="([^"]+)"', html
    )
    data = {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "@id": canonical + "#profile-page",
        "url": canonical,
        "name": old.get("name") or title,
        "description": description,
        "inLanguage": "zh-CN",
        "isPartOf": {"@id": WEBSITE_ID},
        "mainEntity": {"@id": PERSON_ID},
        "about": {"@id": PERSON_ID},
    }
    for key in ("datePublished", "dateModified"):
        if old.get(key):
            data[key] = old[key]
    image = absolute_image(path, html)
    if image:
        data["primaryImageOfPage"] = {
            "@type": "ImageObject",
            "url": image,
        }
    write(path, replace_schema(html, data))


def update_service(path: Path) -> None:
    html = read(path)
    old = parse_schema(html)
    canonical = canonical_for(path, html)
    title = first(r"<title>(.*?)</title>", html)
    name = old.get("name") or title.split("｜")[0]
    description = old.get("description") or first(r'<meta\s+name="description"\s+content="([^"]+)"', html)
    data = {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "@id": canonical + "#service",
        "url": canonical,
        "name": name,
        "serviceType": name,
        "description": description,
        "provider": {"@id": PERSON_ID},
        "areaServed": old.get("areaServed") or "深圳",
        "isPartOf": {"@id": WEBSITE_ID},
        "inLanguage": "zh-CN",
    }
    if old.get("keywords"):
        data["keywords"] = old["keywords"]
    write(path, replace_schema(html, data))


def update_tool() -> None:
    path = ROOT / "tools" / "enterprise-risk-intake.html"
    html = read(path)
    canonical = canonical_for(path, html)
    data = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "@id": canonical + "#application",
        "url": canonical,
        "name": "企业风险事项初步梳理器",
        "description": first(r'<meta\s+name="description"\s+content="([^"]+)"', html),
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web browser",
        "isAccessibleForFree": True,
        "inLanguage": "zh-CN",
        "creator": {"@id": PERSON_ID},
        "isPartOf": {"@id": WEBSITE_ID},
    }
    write(path, replace_schema(html, data))


def main() -> None:
    update_index()
    for path in sorted((ROOT / "articles").glob("*.html")):
        if path.name == "prosecutor-appointment-professional-background.html":
            update_profile_evidence(path)
        else:
            update_article(path)
    for path in sorted((ROOT / "services").glob("*.html")):
        update_service(path)
    update_tool()
    print("Structured data updated.")


if __name__ == "__main__":
    main()
