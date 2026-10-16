"""
Unit tests for suite-web-craft business logic.
"""

import sys
import unittest
from pathlib import Path

SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.meta_tags import generate_meta_tags


class TestMetaTags(unittest.TestCase):
    def test_generate_standard_tags(self):
        res = generate_meta_tags(
            title="DeveloperOS Tools",
            description="Open-source ecosystem",
            url="https://developeros.in",
            image_url="https://developeros.in/img.png",
        )
        self.assertIn("<title>DeveloperOS Tools</title>", res["html"])
        self.assertIn('property="og:url" content="https://developeros.in"', res["html"])
        self.assertIn('name="twitter:card" content="summary_large_image"', res["html"])
        self.assertTrue(res["has_image"])
        self.assertEqual(res["tag_count"], 14)

    def test_escaping_quotes_and_html(self):
        res = generate_meta_tags(
            title='Test <script>alert("xss")</script> & "Quotes"',
            description='Test "Desc" & <b>Bold</b>',
            url="https://developeros.in",
        )
        self.assertNotIn("<script>", res["html"])
        self.assertNotIn("<b>", res["html"])
        self.assertIn("&lt;script&gt;", res["html"])
        self.assertIn("&quot;Quotes&quot;", res["html"])
        self.assertIn("&amp;", res["html"])

    def test_empty_inputs(self):
        res = generate_meta_tags(title="", description="", url="")
        self.assertEqual(res["title"], "")
        self.assertEqual(res["description"], "")
        self.assertEqual(res["has_image"], False)
        self.assertNotIn("og:image", res["html"])

    def test_none_inputs(self):
        res = generate_meta_tags(title=None, description=None, url=None, image_url=None)
        self.assertEqual(res["title"], "")
        self.assertEqual(res["description"], "")
        self.assertEqual(res["has_image"], False)

    def test_twitter_card_fallback(self):
        res = generate_meta_tags(
            title="Card Test",
            description="Testing unknown card",
            url="https://developeros.in",
            twitter_card="invalid_card_type",
        )
        self.assertEqual(res["card_type"], "summary_large_image")
        self.assertIn('content="summary_large_image"', res["html"])

    def test_custom_site_name(self):
        res = generate_meta_tags(
            title="Custom Site",
            description="Custom site test",
            url="https://custom.dev",
            site_name="CustomPlatform",
        )
        self.assertEqual(res["site_name"], "CustomPlatform")
        self.assertIn('property="og:site_name" content="CustomPlatform"', res["html"])

    def test_whitespace_trimming(self):
        res = generate_meta_tags(
            title="   Padded Title   ",
            description="   Padded Desc   ",
            url="   https://developeros.in   ",
        )
        self.assertEqual(res["title"], "Padded Title")
        self.assertEqual(res["description"], "Padded Desc")
        self.assertIn('content="https://developeros.in"', res["html"])


if __name__ == "__main__":
    unittest.main()
