"""
Pure business logic for OpenGraph and Meta Tag generation.
Zero UI or Streamlit dependencies.
"""

from typing import Dict, Optional


def generate_meta_tags(
    title: str,
    description: str,
    url: str,
    image_url: Optional[str] = None,
    site_name: str = "DeveloperOS",
    twitter_card: str = "summary_large_image",
) -> Dict[str, str]:
    """Generates standard HTML meta, OpenGraph, and Twitter Card tags."""
    safe_title = title.strip().replace('"', '&quot;')
    safe_desc = description.strip().replace('"', '&quot;')
    safe_url = url.strip()
    safe_image = (image_url or "").strip()

    tags = []
    # Primary Meta
    tags.append(f'<title>{safe_title}</title>')
    tags.append(f'<meta name="title" content="{safe_title}">')
    tags.append(f'<meta name="description" content="{safe_desc}">')

    # OpenGraph / Facebook
    tags.append('<meta property="og:type" content="website">')
    tags.append(f'<meta property="og:url" content="{safe_url}">')
    tags.append(f'<meta property="og:title" content="{safe_title}">')
    tags.append(f'<meta property="og:description" content="{safe_desc}">')
    tags.append(f'<meta property="og:site_name" content="{site_name}">')
    if safe_image:
        tags.append(f'<meta property="og:image" content="{safe_image}">')

    # Twitter
    tags.append(f'<meta name="twitter:card" content="{twitter_card}">')
    tags.append(f'<meta name="twitter:url" content="{safe_url}">')
    tags.append(f'<meta name="twitter:title" content="{safe_title}">')
    tags.append(f'<meta name="twitter:description" content="{safe_desc}">')
    if safe_image:
        tags.append(f'<meta name="twitter:image" content="{safe_image}">')

    return {
        "html": "\n".join(tags),
        "title": safe_title,
        "description": safe_desc,
        "tag_count": len(tags),
    }
