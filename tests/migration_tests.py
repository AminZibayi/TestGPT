import unittest
import json
from migrate_scripts.migration import extract_forestry_data, insert_tina_data

class TestMigration(unittest.TestCase):

    def setUp(self):
        with open('forestry_data/posts.json', 'r') as f:
            self.forestry_posts = json.load(f)
        with open('forestry_data/pages.json', 'r') as f:
            self.forestry_pages = json.load(f)
        with open('forestry_data/settings.json', 'r') as f:
            self.forestry_settings = json.load(f)

    def test_extract_forestry_data(self):
        posts, pages, settings = extract_forestry_data()
        self.assertEqual(posts, self.forestry_posts)
        self.assertEqual(pages, self.forestry_pages)
        self.assertEqual(settings, self.forestry_settings)

    def test_insert_tina_data(self):
        insert_tina_data(self.forestry_posts, self.forestry_pages, self.forestry_settings)
        with open('tinaCMS_data/posts.json', 'r') as f:
            tina_posts = json.load(f)
        with open('tinaCMS_data/pages.json', 'r') as f:
            tina_pages = json.load(f)
        with open('tinaCMS_data/settings.json', 'r') as f:
            tina_settings = json.load(f)
        self.assertEqual(tina_posts, self.forestry_posts)
        self.assertEqual(tina_pages, self.forestry_pages)
        self.assertEqual(tina_settings, self.forestry_settings)

if __name__ == '__main__':
    unittest.main()