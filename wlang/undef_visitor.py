# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from __future__ import print_function

import wlang.ast
            
class UndefVisitor (wlang.ast.AstVisitor):
    """Computes all variables that are used before being defined"""
    def __init__ (self):
        super (UndefVisitor, self).__init__ ()
        # the set of undefined variables
        self._undefs = set()
        self._defs = set()
        self._checked = False
        #using this variable or defining
        self._using = False
        #special variable for if statement
        self._ifst = 0
        self._tmpdefs = set()

    def check (self, node):
        """Check for undefined variables starting from a given AST node"""
        # do the necessary setup/arguments and call self.visit (node, args)
        self._undefs.clear()
        self.visit(node)
        self._checked = True


    def get_undefs (self):
        """Return the set of all variables that are used before being defined
           in the program.  Available only after a call to check()
        """
        if self._checked:
            return self._undefs
        else:
            print("This function can only be used after a call to check()!")
        
    def visit_StmtList (self, node, *args, **kwargs):
        if node.stmts is None:
            return
        for s in node.stmts:
            self.visit(s)
    
    def visit_IntVar (self, node, *args, **kwargs):
        if self._ifst == 0:
            if self._using and node not in self._defs:
                self._undefs.add(node)
            elif not self._using and node not in self._undefs:
                self._defs.add(node)
        elif self._ifst == 1:
            if self._using and node not in self._defs:
                self._undefs.add(node)
            elif not self._using and node not in self._undefs:
                self._tmpdefs.add(node)
        elif self._ifst == 2:
            if self._using and node not in self._defs:
                self._undefs.add(node)
            elif not self._using and node not in self._undefs and node in self._tmpdefs:
                self._defs.add(node)
            
    def visit_Const (self, node, *args, **kwargs):
        pass
    
    def visit_Stmt (self, node, *args, **kwargs):
        pass
    
    def visit_AsgnStmt (self, node, *args, **kwargs):
        self._using = True
        self.visit(node.rhs)
        self._using = False
        self.visit(node.lhs)


    def visit_Exp (self, node, *args, **kwargs):
        self._using = True
        for v in node.args:
            self.visit(v)
    
    def visit_HavocStmt (self, node, *args, **kwargs):
        self._using = False
        for v in node.vars:
            self.visit(v)
    
    def visit_AssertStmt (self, node, *args, **kwargs):
        self._using = True
        self.visit(node.cond)
    
    def visit_AssumeStmt (self, node, *args, **kwargs):
        self._using = True
        self.visit(node.cond)

    def visit_IfStmt (self, node, *args, **kwargs):
        self.visit(node.cond)
        self._ifst = 1
        self.visit(node.then_stmt)
        if node.has_else():
            self._ifst = 2
            self.visit(node.else_stmt)
        self._ifst = 0
        self._tmpdefs.clear()

    def visit_WhileStmt (self, node, *args, **kwargs):
        self.visit(node.cond)
        self.visit(node.body)
        
