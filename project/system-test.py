import os
import unittest
import pandas as pd
import sqlite3

def verify_files(directory, filenames):
    
    verification_results = {}
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        verification_results[filename] = os.path.isfile(file_path)
    
    return verification_results


def verify_table(db_name):
    cnx = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", cnx)
    return list(df['name'])
    

class SystemTest(unittest.TestCase):
    def setUp(self):
        self.test_directory = "../data/"
        self.db_name = 'climate_change.sqlite'

    def test_files_exist(self):
        filenames = ["climate_change.sqlite"]
        expected_results = {
            "climate_change.sqlite": True
        }
        results = verify_files(self.test_directory, filenames)
        self.assertEqual(results, expected_results)

    def test_table_names(self):
        expected_results = ['ocean_surface_acidity', 'carbon_emission_europe']
        results = verify_table(self.test_directory+self.db_name)
        self.assertEqual(results,expected_results,"Table Names are not Correct")


if __name__ == "__main__":
    unittest.main()
