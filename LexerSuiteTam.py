import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    
    def test_keyword_stmt(self):
        """test keyword break"""
        self.assertTrue(TestLexer.checkLexeme("""break; continue; return;""", """break,;,continue,;,return,;,<EOF>""", 105))

    def test_keyword_const(self):
        """test keyword const"""
        self.assertTrue(TestLexer.checkLexeme("""const a boolean x = true;""", """const,a,boolean,x,=,true,;,<EOF>""", 106))

    def test_keyword_else(self):
        """test keyword if/else"""
        self.assertTrue(TestLexer.checkLexeme("""if else If Else""", """if,else,If,Else,<EOF>""", 107))

    def test_keyword_for(self):
        """test keyword for"""
        self.assertTrue(TestLexer.checkLexeme("""for a,b := range arr[]""", """for,a,,,b,:=,range,arr,[,],<EOF>""", 108))

    def test_keyword_interface(self):
        """test keyword interface"""
        self.assertTrue(TestLexer.checkLexeme("""type inter interface {}""", """type,inter,interface,{,},<EOF>""", 109))

    def test_keyword_return(self):
        """test keyword return"""
        self.assertTrue(TestLexer.checkLexeme("""return a*b;;""", """return,a,*,b,;,;,<EOF>""", 110))

    def test_keyword_struct(self):
        self.assertTrue(TestLexer.checkLexeme("""struct type int Person, {}""", """struct,type,int,Person,,,{,},<EOF>""", 111))

    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""/* Nested comment bla bla bla skipped */ test // Line comment""", """test,<EOF>""", 112))

    def test_bin_lit(self):
        self.assertTrue(TestLexer.checkLexeme("""0b0101-011.234e-21""","""0b0101,-,011.234e-21,<EOF>""",113))

    def test_float_lit(self):
        self.assertTrue(TestLexer.checkLexeme("""-011.234e-21""","""-,011.234e-21,<EOF>""",114))

    def test_oct_lit(self):
        self.assertTrue(TestLexer.checkLexeme("""0o1237654 + 0O76534121 + 0O123478""","""0o1237654,+,0O76534121,+,0O12347,8,<EOF>""",115))

    def test_hex_lit(self):
        self.assertTrue(TestLexer.checkLexeme("""0xbef-5=0Xace""","""0xbef,-,5,=,0Xace,<EOF>""",116))

    def test117(self):    
        self.assertTrue(TestLexer.checkLexeme("35ab_tAM","35,ab_tAM,<EOF>",117))    

    def test118(self):    
        self.assertTrue(TestLexer.checkLexeme("/*/*sdsfsdfsdf*/*/","<EOF>",118)) 

    def test119(self):    
        self.assertTrue(TestLexer.checkLexeme("000000","0,0,0,0,0,0,<EOF>",119)) 

    def test120(self):    
        self.assertTrue(TestLexer.checkLexeme("00b000","0,0b000,<EOF>",120)) 

    def test121(self):    
        self.assertTrue(TestLexer.checkLexeme("0b2.0e10","0,b2,.,0,e10,<EOF>",121)) 

    def test122(self):    
        self.assertTrue(TestLexer.checkLexeme(".0e10",".,0,e10,<EOF>",122)) 

    def test123(self):    
        self.assertTrue(TestLexer.checkLexeme("\"tam\\n\\t\"","\"tam\\n\\t\",<EOF>",123)) 

    def test124(self):    
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>",124)) 

    def test125(self):    
        self.assertTrue(TestLexer.checkLexeme("a:=b=+=c-=d--*=","a,:=,b,=,+=,c,-=,d,-,-,*=,<EOF>",125)) 

    def test126(self):    
        self.assertTrue(TestLexer.checkLexeme("===/=!==\"==\"%=*=+=","==,=,/=,!=,=,\"==\",%=,*=,+=,<EOF>",126))

    def test127(self):    
        self.assertTrue(TestLexer.checkLexeme("597E+71","597,E,+,71,<EOF>",127))

    def test128(self):    
        self.assertTrue(TestLexer.checkLexeme("6.E-33","6.E-33,<EOF>",128))

    def test129(self):    
        self.assertTrue(TestLexer.checkLexeme("Tam$^HdR","Tam,ErrorToken $",129))

    def test130(self):    
        self.assertTrue(TestLexer.checkLexeme("## F]R","ErrorToken #",130))

    def test131(self):    
        self.assertTrue(TestLexer.checkLexeme("\"\\i'\"_)1'\"\"","Illegal escape in string: \"\\i",131))

    def test132(self):    
        self.assertTrue(TestLexer.checkLexeme("+-=[]{}|","+,-=,[,],{,},ErrorToken |",132))

    def test133(self):
        self.assertTrue(TestLexer.checkLexeme("interface ITest { Method() int; }", "interface,ITest,{,Method,(,),int,;,},<EOF>", 133))

    def test134(self):    
        self.assertTrue(TestLexer.checkLexeme("for;;i+=-1{break}","for,;,;,i,+=,-,1,{,break,},<EOF>",134))

    def test135(self):
        self.assertTrue(TestLexer.checkLexeme("range(1,10)", "range,(,1,,,10,),<EOF>", 135))

    def test136(self):    
        self.assertTrue(TestLexer.checkLexeme("nil??","nil,ErrorToken ?",136))

    def test137(self):
        self.assertTrue(TestLexer.checkLexeme("struct Point { x int; y int; }", "struct,Point,{,x,int,;,y,int,;,},<EOF>", 137))

    def test138(self):    
        self.assertTrue(TestLexer.checkLexeme("map[int]string{1:\"One\", \"Two\":2}","map,[,int,],string,{,1,:,\"One\",,,\"Two\",:,2,},<EOF>",138))

    def test139(self):    
        self.assertTrue(TestLexer.checkLexeme(":= *&^%$#@!()",":=,*,ErrorToken &",139))

    def test140(self):    
        self.assertTrue(TestLexer.checkLexeme("\"\\\"Escape\\\\Sequence\\\\Test\\\"\"","\"\\\"Escape\\\\Sequence\\\\Test\\\"\",<EOF>",140))

    def test141(self):    
        self.assertTrue(TestLexer.checkLexeme("1_234 987_","1,_234,987,_,<EOF>",141))

    def test142(self):    
        self.assertTrue(TestLexer.checkLexeme("package main\nimport \"os\" os.Open(\"file.txt\")","package,main,;,import,\"os\",os,.,Open,(,\"file.txt\",),<EOF>",142))

    def test143(self):    
        self.assertTrue(TestLexer.checkLexeme("x >> y || z**2","x,>,>,y,||,z,*,*,2,<EOF>",143))

    def test144(self):    
        self.assertTrue(TestLexer.checkLexeme("// Single-line comment","<EOF>",144))

    def test145(self):    
        self.assertTrue(TestLexer.checkLexeme("+=-*/%%==!=&&||","+=,-,*,/,%,%=,=,!=,&&,||,<EOF>",145))

    def test146(self):    
        self.assertTrue(TestLexer.checkLexeme("0x1A2B3C DEF123","0x1A2B3C,DEF123,<EOF>",146))

    def test147(self):    
        self.assertTrue(TestLexer.checkLexeme("var pi = 3.1415.926","var,pi,=,3.1415,.,926,<EOF>",147))

    def test148(self):    
        self.assertTrue(TestLexer.checkLexeme("5_6_7_8_","5,_6_7_8_,<EOF>",148))

    def test149(self):    
        self.assertTrue(TestLexer.checkLexeme("456xyz abc?","456,xyz,abc,ErrorToken ?",149))

    def test150(self):    
        self.assertTrue(TestLexer.checkLexeme("y := 4+++5","y,:=,4,+,+,+,5,<EOF>",150))

    def test151(self):    
        self.assertTrue(TestLexer.checkLexeme("while (j>=0) { j-- }","while,(,j,>=,0,),{,j,-,-,},<EOF>",151))
    
    def test152(self):    
        self.assertTrue(TestLexer.checkLexeme("arr := map[string]int{\"a\": 100, \"b\": 200,,}","arr,:=,map,[,string,],int,{,\"a\",:,100,,,\"b\",:,200,,,,,},<EOF>",152))

    def test153(self):    
        self.assertTrue(TestLexer.checkLexeme("range 5..15 {}","range,5.,.,15,{,},<EOF>",153))

    def test154(self):    
        self.assertTrue(TestLexer.checkLexeme("2.3.4e-5.6","2.3,.,4,e,-,5.6,<EOF>",154))

    def test155(self):    
        self.assertTrue(TestLexer.checkLexeme("log.Printf(\"Value: %f\", 3.14)","log,.,Printf,(,\"Value: %f\",,,3.14,),<EOF>",155))
    
    def test156(self):    
        self.assertTrue(TestLexer.checkLexeme("987.E--5","987.,E,-,-,5,<EOF>",156))

    def test157(self):    
        self.assertTrue(TestLexer.checkLexeme("ch := make(chan<-string, 2)","ch,:=,make,(,chan,<,-,string,,,2,),<EOF>",157))

    def test158(self):    
        self.assertTrue(TestLexer.checkLexeme("y = **8","y,=,*,*,8,<EOF>",158))

    def test159(self):    
        self.assertTrue(TestLexer.checkLexeme("returnbreakcontinue","returnbreakcontinue,<EOF>",159))

    def test160(self):    
        self.assertTrue(TestLexer.checkLexeme("val = x || y && !z","val,=,x,||,y,&&,!,z,<EOF>",160))

    def test_newline_1(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""type Animal struct {
    species string
    weight float
}

var y float = 20;""",
"""type,Animal,struct,{,species,string,;,weight,float,;,},;,var,y,float,=,20,;,<EOF>""",
        161)) 

    def test_newline_2(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
const y = 24
var z int
""",
"""const,y,=,24,;,var,z,int,;,<EOF>""",
        162)) 

    def test_newline_3(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
func start() bool {
    var z float = 5.5
}
""",
"""func,start,(,),bool,{,var,z,float,=,5.5,;,},;,<EOF>""",
        163)) 

    def test_newline_4(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""func compute() {}
""",
"""func,compute,(,),{,},;,<EOF>""",
        164)) 

    def test_newline_5(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""var 34float=inty = "abc"
""",
"""var,34,float,=,inty,=,"abc",;,<EOF>""",
        165)) 

    def test_newline_6(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""type Machine interface {
    Multiply(x, y int, z float) int
    Greet(title string)
}""",
"""type,Machine,interface,{,Multiply,(,x,,,y,int,,,z,float,),int,;,Greet,(,title,string,),;,},<EOF>""",
        166)) 

    def test_newline_7(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""if (a != 5) {fmt.Output(a)
    
} else if (y != 3) {
    fmt.Output(y)
}""",
"""if,(,a,!=,5,),{,fmt,.,Output,(,a,),;,},else,if,(,y,!=,3,),{,fmt,.,Output,(,y,),;,},<EOF>""",
        167)) 

    def test_newline_8(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
nums := [4]float{1.1, 2.2, 3.3, 4.4}
for key, item := range nums {
 // item: 1.1, 2.2, 3.3, 4.4
}
""",
"""nums,:=,[,4,],float,{,1.1,,,2.2,,,3.3,,,4.4,},;,for,key,,,item,:=,range,nums,{,},;,<EOF>""",
        168)) 

    def test_newline_9(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
for pos, num := range list 
{}
""",
"""for,pos,,,num,:=,range,list,;,{,},;,<EOF>""",
        169)) 
        
    def test_newline_10(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
vehicle.model := "Tesla"
vehicle.year := 2022
""",
"""vehicle,.,model,:=,"Tesla",;,vehicle,.,year,:=,2022,;,<EOF>""",
        170))


    def test_error_token_1(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("hello@world","hello,ErrorToken @",171))

    def test_error_token_2(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("mail.me@domain","mail,.,me,ErrorToken @",172)) 

    def test_error_token_3(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("x = \" & \" ## ","x,=,\" & \",ErrorToken #",173)) 

    def test_error_token_4(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("$var","ErrorToken $",174)) 

    def test_error_token_5(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("`some string`", "ErrorToken `", 175))

    def test_error_token_6(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("+=&|&&xyz","+=,ErrorToken &",176)) 

    def test_error_token_7(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("!!|\\","!,!,ErrorToken |",177)) 

    def test_error_token_8(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("'a'","ErrorToken '",178)) 

    def test_error_token_9(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("\\abc","ErrorToken \\",179)) 

    def test_error_token_10(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("condition ? val1 : val2","condition,ErrorToken ?",180))


    def test_illegal_escape_1(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""\"\\t\\b\"""","""Illegal escape in string: \"\\t\\b""",181))

    def test_illegal_escape_2(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("\"escape \\q\"", "Illegal escape in string: \"escape \\q", 182))

    def test_illegal_escape_3(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""\"$\\f\"""","""Illegal escape in string: \"$\\f""",183)) 

    def test_illegal_escape_4(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""\"\\n\\t\" * \"$\\f\"""","""\"\\n\\t\",*,Illegal escape in string: \"$\\f""",184)) 

    def test_illegal_escape_5(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""\"\\x\\n\\n\"""","""Illegal escape in string: \"\\x""",185)) 

    def test_illegal_escape_6(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""\"\\nn\\t\\"n\\u\\u\"""","""Illegal escape in string: \"\\nn\\t\\"n\\u""",186)) 

    def test_illegal_escape_7(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""\"\\abcdef\"""","""Illegal escape in string: \"\\a""",187)) 

    def test_illegal_escape_8(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""\"\\",\\t\\.\"""","""Illegal escape in string: \"\\",\\t\\.""",188)) 

    def test_illegal_escape_9(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""\"\\a\\a\"""","""Illegal escape in string: \"\\a""",
        189)) 

    def test_illegal_escape_10(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("""hi\"\\455453abc\"""","""hi,Illegal escape in string: \"\\4""",190)) 

    def test_unclosed_string_1(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(
"""var a = "string test\\nabc
func abc ()""","""var,a,=,Unclosed string: "string test\\nabc""",191)) 

    def test_unclosed_string_2(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""""A""","""Unclosed string: "A""",192)) 

    def test_unclosed_string_3(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(
"""var fun() {
int a = "" "no close
}""","""var,fun,(,),{,int,a,=,"",Unclosed string: "no close""",193))

    def test_unclosed_string_4(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(
""" ""\" "" """,
"""""," ",Unclosed string: " """,
        194))

    def test_unclosed_string_5(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme("""abc"A string""","""abc,Unclosed string: "A string""",195))

    def test_unclosed_string_6(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme("""b"\\"" TAM""","""b,"\\"",TAM,<EOF>""",196))

    def test_unclosed_string_7(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(
"""int VTT = "array
ing\"""",
"""int,VTT,=,Unclosed string: "array""",
        197))

    def test_unclosed_string_8(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(
"""string m = "voila\\n
int name = "futte";""",
            """string,m,=,Unclosed string: "voila\\n""",
        198))

    def test_unclosed_string_9(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(
""""
c'"AB";""",
            """Unclosed string: \"""",
        199))

    def test_unclosed_string_10(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(
""""working on \\t\\"\\n\\\\""",
"""Unclosed string: "working on \\t\\\"\\n\\\\""",
        200))
