"""
Unit tests for suite-web-craft business logic.
"""

import sys
import unittest
from pathlib import Path

# Ensure suite root is in sys.path
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
        self.assertIn('name="twitter:card"', res["html"])
        self.assertEqual(res["tag_count"], 14)

    def test_escaping_quotes(self):
        res = generate_meta_tags(
            title='Test "Quotes"',
            description='Test "Desc"',
            url="https://developeros.in",
        )
        self.assertIn("Test &quot;Quotes&quot;", res["html"])


if __name__ == "__main__":
    unittest.main()
