import unittest
import os
import shutil
from pipeline import create_directory_structure, parse_summary_from_text

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_date_dir"

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_create_directory_structure(self):
        title = "A Simple Test Title: With Some !@# Special Chars"
        expected_dir = os.path.join(self.test_dir, "a-simple-test-title-with-some-special-chars")

        created_dir = create_directory_structure(self.test_dir, title)

        self.assertEqual(created_dir, expected_dir)
        self.assertTrue(os.path.exists(created_dir))
        self.assertTrue(os.path.isdir(created_dir))

    def test_parse_summary_from_text(self):
        text = "This is a full text. The system consists of three modules. We evaluate using metric X."
        abstract = "This paper addresses a problem. We propose a framework. Results show an impact on society."

        summary = parse_summary_from_text(text, abstract)

        self.assertIn("## 🎯 Problem Statement", summary)
        self.assertIn("## 🏗️ Architectural Overview & Technical Design", summary)
        self.assertIn("## 🛠️ Solution Approaches & Methodology", summary)
        self.assertIn("## 🌍 Societal Impact & Sector Benefits", summary)
        self.assertIn("This paper addresses a problem.", summary)

if __name__ == '__main__':
    unittest.main()
