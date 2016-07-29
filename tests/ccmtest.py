import os
from unittest import TestCase


class Tester(TestCase):

    def tearDown(self):
        if hasattr(self, 'cluster'):
            try:
                for node in self.cluster.nodelist():
                    self.assertListEqual(node.grep_log_for_errors(), [])
            finally:
                test_path = self.cluster.get_path()
                self.cluster.remove()
                if os.path.exists(test_path):
                    os.remove(test_path)
