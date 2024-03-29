import unittest
import wlang.ast as ast
import wlang.undef_visitor as undef_visitor

class TestStatsVisitor (unittest.TestCase):
    def test_one (self):
        prg1 = "x := 10; y := x + z"
        ast1 = ast.parse_string (prg1)

        uv = undef_visitor.UndefVisitor ()
        uv.check (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (set ([ast.IntVar('z')]), uv.get_undefs ())

    def test_two (self):
        with open('./wlang/undef_test.prg', 'r') as f:
            prg = f.read()

        ast1 = ast.parse_string (prg)
        uv = undef_visitor.UndefVisitor ()
        print(uv.get_undefs())
        uv.check(ast1)
        print(uv.get_undefs())
        # UNCOMMENT to run the test
        self.assertEquals(set([ast.IntVar('z'), ast.IntVar('q'), ast.IntVar('r'), ast.IntVar('w')]), uv.get_undefs())
