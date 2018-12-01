import unittest
import subprocess
import os
import sys

class Tests(unittest.TestCase):

    def test_Task1_Build(self):
        saved_path = os.getcwd()
        os.chdir('../task1')
        result = subprocess.run(['run.sh'], stdout=subprocess.PIPE)
        os.chdir(saved_path)
        self.assertTrue(result.returncode == 0)

    def test_Task1_CompareInputAndOutputStrings(self):
        saved_path = os.getcwd()
        os.chdir('../task1')
        input_string = 'test'
        result = subprocess.run(['./out/app', input_string], stdout=subprocess.PIPE)
        os.chdir(saved_path)
        output_string = result.stdout.decode("utf-8").strip()
        self.assertTrue(output_string == input_string)

    ''' Негативный сценарий. Слишком длинная строка будет обрезана '''
    def test_Task1_VeryLongInputString(self):
        saved_path = os.getcwd()
        os.chdir('../task1')
        input_string = 'This is a very very long input string, more than 50 chars'
        result = subprocess.run(['./out/app', input_string], stdout=subprocess.PIPE)
        os.chdir(saved_path)
        output_string = result.stdout.decode("utf-8").strip()
        self.assertFalse(output_string == input_string)

    def test_Task2_Build(self):
        saved_path = os.getcwd()
        os.chdir('../task2')
        sys.stdout = None
        result = subprocess.run(['run.sh'], stdout=subprocess.PIPE)
        os.chdir(saved_path)
        self.assertTrue(result.returncode == 0)

    def test_Task2_CompareInputAndOutputStrings(self):
        saved_path = os.getcwd()
        os.chdir('../task2')
        input_string = 'test'
        result = subprocess.run(['./out/app', input_string], stdout=subprocess.PIPE)
        os.chdir(saved_path)
        output_string = result.stdout.decode("utf-8").strip()
        self.assertTrue(output_string == input_string)

    ''' Негативный сценарий. Слишком длинная строка будет обрезана '''
    def test_Task2_VeryLongInputStringWillCut(self):
        saved_path = os.getcwd()
        os.chdir('../task2')
        input_string = 'This is a very very long input string'
        result = subprocess.run(['./out/app', input_string], stdout=subprocess.PIPE)
        os.chdir(saved_path)
        output_string = result.stdout.decode("utf-8").strip()
        self.assertFalse(output_string == input_string)

if __name__ == '__main__':
    unittest.main(verbosity=2)
