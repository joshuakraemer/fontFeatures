from fontFeatures.feeLib import FeeParser
from fontTools.ttLib import TTFont

import unittest

class TestFeeAnchors(unittest.TestCase):

  def test_parse_to_ff(self):
    p = FeeParser(TTFont("fonts/Roboto-Regular.ttf"))
    p.parseString("""
      Anchors A {
        top <679 1600>
        bottom <691 0>
      };

      Anchors B {
        top <611 1612>
      };

      Anchors acutecomb { _top <-570 1290> };
      Anchors tildecomb { _top <-542 1256> };

      Feature mark { Attach &top &_top; };
""")

    self.assertEqual(p.fea.anchors["A"]["top"], (679,1600))
    self.assertEqual(p.fea.asFea(),"""
    markClass acutecomb <anchor -570 1290> @top;
    markClass tildecomb <anchor -542 1256> @top;

feature mark {
                        pos base A <anchor 679 1600> mark @top;
            pos base B <anchor 611 1612> mark @top;


} mark;
""")