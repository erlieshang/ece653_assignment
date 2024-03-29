import unittest
import wlang.ast as ast
import wlang.stats_visitor as stats_visitor

class TestStatsVisitor (unittest.TestCase):
    def test_one (self):
        prg1 = "x := 10; print_state"
        ast1 = ast.parse_string (prg1)

        sv = stats_visitor.StatsVisitor ()
        sv.visit (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (sv.get_num_stmts (), 2)
        self.assertEquals (sv.get_num_vars (), 1)

    def test_two(self):
        with open('./wlang/stats_test.prg', 'r') as f:
            prg = f.read()
        # test parser
        ast1 = ast.parse_string(prg)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 21)
        self.assertEquals(sv.get_num_vars(), 3)
