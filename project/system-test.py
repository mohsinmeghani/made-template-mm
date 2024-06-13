import os
import unittest


def verify_files(directory, filenames):
    
    verification_results = {}
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        verification_results[filename] = os.path.isfile(file_path)
    
    return verification_results


class SystemTest(unittest.TestCase):
    def setUp(self):
        self.test_directory = "../data/"

    def test_files_exist(self):
        filenames = ["climate_change.sqlite"]
        expected_results = {
            "climate_change.sqlite": True
        }
        results = verify_files(self.test_directory, filenames)
        self.assertEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
