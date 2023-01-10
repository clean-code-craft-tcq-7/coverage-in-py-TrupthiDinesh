import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(-1, 0, 45) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(1, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(44, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(46, 0, 45) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(40, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(-1, 0, 40) == 'TOO_LOW')
      self.assertTrue(typewise_alert.infer_breach(0, 0, 40) == 'TOO_HIGH')
 


if __name__ == '__main__':
  unittest.main()
