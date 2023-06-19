import sys
import unittest
from ga import get_args_of, parse, get_assoc

# test_ga_parse - required convention
# But TestGaParseFunc - discretionary - favor descriptiveness
# But test* method name is - required convention

class TestGaParse(unittest.TestCase):
  def test_parse_no_args(self):
    # Test the ga function
    result = parse()
    r = {'err_m': '', 'err_code': 'Ok', 'err_id': 100, 'options': [], 'flags': [], '_poss': {}}
    msg = 'Testing for '
    self.assertEqual(result, r)
    self.assertTrue(sys.argv[1:] == [])
    pass

if __name__ == '__main__':
  unittest.main()
  # 33500+24,500 = 58,000