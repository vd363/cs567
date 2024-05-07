import unittest
import subprocess
from test_contacts import TestContactManagement

class TestMutationTesting(unittest.TestCase):
    def test_mutations(self):
        original_file = 'contact_management.py'

        command = f'universalmutator mutate --language python --directory . --files {original_file}'
        subprocess.run(command, shell=True, check=True)

        suite = unittest.TestLoader().loadTestsFromTestCase(TestContactManagement)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    unittest.main()
