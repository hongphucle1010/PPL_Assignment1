import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # ! ------------------- Sample test ------------------- !
    def test_simple_program(self):
        """Simple program: void main() {}"""
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    # ! ------------------- Program structure 2 ------------------- !
    def test_program_structure(self):
        """Program with many declaration"""
        input = """var a int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_program_structure_2(self):
        """Invalid program with statement"""
        input = """a := 1;"""
        expect = "Error on line 1 col 1: a"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_program_structure_3(self):
        """Invalid program with for statement"""
        input = """for a := 1 to 10 do {}"""
        expect = "Error on line 1 col 1: for"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_program_structure_4(self):
        """Invalid program with if statement"""
        input = """if a == 1 then {}"""
        expect = "Error on line 1 col 1: if"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_program_structure_5(self):
        """Valid program with struct declaration"""
        input = """type a struct {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    #! ------------------- Declaration ------------------- !
    def test_variable_declaration(self):
        """Variable declaration"""
        input = """var a int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_variable_declaration_2(self):
        """Multiple variable declaration"""
        input = """var a,b,c int;"""
        expect = "Error on line 1 col 6: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_variable_declaration_3(self):
        """Variable declaration with assignment"""
        input = """var a int = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_variable_declaration_4(self):
        """Variable declaration with inferred type"""
        input = """var a = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_variable_declaration_5(self):
        """Variable declaration with not specify type and initial value"""
        input = """var a;"""
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_variable_declaration_6(self):
        """Variable declaration with composite type"""
        input = """var a = Person{name:"name", age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_invalid_variable_declaration(self):
        """Invalid variable declaration"""
        input = """var a;"""
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_constant_declaration(self):
        """Constant declaration"""
        input = """const a = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_constant_declaration_2(self):
        """Constant struct declaration"""
        input = """const a = Person{name:"name", age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_invalid_constant_declaration(self):
        """Invalid constant declaration"""
        input = """const a = 1"""
        expect = "Error on line 1 col 12: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_invalid_constant_declaration_2(self):
        """Missing right hand side"""
        input = """const a;"""
        expect = "Error on line 1 col 8: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_function_declaration(self):
        """Function declaration"""
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_function_declaration_2(self):
        """Function declaration with parameter"""
        input = """func main(a int) {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_function_declaration_3(self):
        """Function declaration with return type"""
        input = """func main() int {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_function_declaration_4(self):
        """Function declaration with body statement"""
        input = """func main() {a := 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_function_declaration_5(self):
        """Function declaration with return type, parameters and body statement"""
        input = """func main(a int) int {return 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_method_declaration(self):
        """Method declaration"""
        input = """func (a Person) main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_method_declaration_2(self):
        """Method declaration with parameter"""
        input = """func (a Person) main(b int) {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_method_declaration_3(self):
        """Method declaration with return type"""
        input = """func (a Person) main() int {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_method_declaration_4(self):
        """Method declaration with body statement"""
        input = """func (a Person) main() {a := 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_method_declaration_5(self):
        """Method declaration with return type, parameters and body statement"""
        input = """func (a Person) main(b int) int {return 1;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_invalid_function_declaration(self):
        """Missing function identifier"""
        input = """func () {};"""
        expect = "Error on line 1 col 7: )"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_invalid_function_declaration_2(self):
        """Nested function declaration"""
        input = """func main() {func foo() {};};"""
        expect = "Error on line 1 col 14: func"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_invalid_function_declaration_3(self):
        """Missing function body"""
        input = """func main();"""
        expect = "Error on line 1 col 12: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_invalid_method_declaration(self):
        """Missing method identifier"""
        input = """func (a Person) () {};"""
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_invalid_method_declaration_2(self):
        """Nested method declaration"""
        input = """func (a Person) main() {func foo() {};};"""
        expect = "Error on line 1 col 25: func"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_invalid_method_declaration_3(self):
        """Missing method body"""
        input = """func (a Person) main();"""
        expect = "Error on line 1 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_invalid_method_declaration_4(self):
        """Missing struct type"""
        input = """func (a) main() {};"""
        expect = "Error on line 1 col 8: )"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_struct_declaration(self):
        """Struct declaration"""
        input = """type Person struct {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_struct_declaration_2(self):
        """Struct declaration with field"""
        input = """type Person struct {name string; age int;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_invalid_struct_declaration(self):
        """Missing struct identifier"""
        input = """type struct {};"""
        expect = "Error on line 1 col 6: struct"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_invalid_struct_declaration_2(self):
        """Missing struct body"""
        input = """type Person struct;"""
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_invalid_struct_declaration_3(self):
        """Missing struct keyword"""
        input = """Person struct {};"""
        expect = "Error on line 1 col 1: Person"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_interface_declaration(self):
        """Interface declaration"""
        input = """type Person interface {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_interface_declaration_2(self):
        """Interface declaration with method"""
        input = """type Person interface {Hello();};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_interface_declaration_3(self):
        """Interface declaration with method and return type"""
        input = """type Person interface {Hello() int;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_invalid_interface_declaration(self):
        """Missing interface identifier"""
        input = """type interface {};"""
        expect = "Error on line 1 col 6: interface"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_invalid_interface_declaration_2(self):
        """Missing interface body"""
        input = """type Person interface;"""
        expect = "Error on line 1 col 22: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_invalid_interface_declaration_3(self):
        """Missing interface keyword"""
        input = """Person interface {};"""
        expect = "Error on line 1 col 1: Person"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    #! ------------------- Literal ------------------- !
    def test_integer_literal(self):
        """Integer literal"""
        input = """const a = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_integer_literal_2(self):
        """Negative integer literal"""
        input = """const a = -1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_boolean_literal(self):
        """Boolean literal"""
        input = """const a = true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_float_literal(self):
        """Float literal"""
        input = """const a = 1.0;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_string_literal(self):
        """String literal"""
        input = """const a = "Hello";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_array_literal(self):
        """Array literal"""
        input = """const a = [3]int{10, 20, 30};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_struct_literal(self):
        """Struct literal"""
        input = """const a = Person{name:"name", age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_nil_literal(self):
        """Nil literal"""
        input = """const a = nil;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))