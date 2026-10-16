"""
DeveloperOS Web & Frontend Craft Suite - Interactive Application
"""

import streamlit as st
from core.meta_tags import generate_meta_tags
from ui.components import render_suite_header, render_suite_footer, render_main_promotional_banner

st.set_page_config(
    page_title="DeveloperOS - Web Craft Suite",
    page_icon="🌐",
    layout="wide",
)


def main():
    render_suite_header(
        title="OpenGraph & Meta Tag Generator",
        description="Craft SEO-optimized meta tags, Twitter cards, and OpenGraph social previews with instant live syntax output.",
    )

    col_input, col_preview = st.columns([1, 1], gap="large")

    with col_input:
        st.subheader("Metadata Properties")
        title = st.text_input("Page Title", value="DeveloperOS — Open-Source Developer Tools")
        description = st.text_area(
            "Page Description",
            value="Scalable, zero-tracking developer utilities ecosystem for modern engineering teams.",
            height=100,
        )
        url = st.text_input("Canonical URL", value="https://developeros.in")
        image_url = st.text_input("Social Share Image URL (OG Image)", value="https://developeros.in/assets/og-banner.png")
        twitter_card = st.selectbox("Twitter Card Type", ["summary_large_image", "summary", "app", "player"])

    results = generate_meta_tags(
        title=title,
        description=description,
        url=url,
        image_url=image_url,
        twitter_card=twitter_card,
    )

    with col_preview:
        st.subheader("Generated HTML Tags")
        st.code(results["html"], language="html")
        st.caption(f"Generated {results['tag_count']} standard tags.")

    render_main_promotional_banner()
    render_suite_footer()


if __name__ == "__main__":
    main()
