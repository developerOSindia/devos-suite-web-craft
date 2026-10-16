"""
Pure business logic for OpenGraph and Meta Tag generation.
Zero UI or Streamlit dependencies.
"""

import html
from typing import Dict, Any, Optional


def generate_meta_tags(
    title: str,
    description: str,
    url: str,
    image_url: Optional[str] = None,
    site_name: str = "DeveloperOS",
    twitter_card: str = "summary_large_image",
) -> Dict[str, Any]:
    """Generates standard HTML meta, OpenGraph, and Twitter Card tags safely."""
    safe_title = html.escape((title or "").strip(), quote=True)
    safe_desc = html.escape((description or "").strip(), quote=True)
    safe_site = html.escape((site_name or "DeveloperOS").strip(), quote=True)
    safe_url = (url or "").strip()
    safe_image = (image_url or "").strip()

    valid_cards = {"summary", "summary_large_image", "app", "player"}
    card_type = twitter_card if twitter_card in valid_cards else "summary_large_image"

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
    tags.append(f'<meta property="og:site_name" content="{safe_site}">')
    if safe_image:
        tags.append(f'<meta property="og:image" content="{safe_image}">')

    # Twitter
    tags.append(f'<meta name="twitter:card" content="{card_type}">')
    tags.append(f'<meta name="twitter:url" content="{safe_url}">')
    tags.append(f'<meta name="twitter:title" content="{safe_title}">')
    tags.append(f'<meta name="twitter:description" content="{safe_desc}">')
    if safe_image:
        tags.append(f'<meta name="twitter:image" content="{safe_image}">')

    return {
        "html": "\n".join(tags),
        "title": safe_title,
        "description": safe_desc,
        "site_name": safe_site,
        "tag_count": len(tags),
        "has_image": bool(safe_image),
        "card_type": card_type,
    }
