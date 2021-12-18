import sys

if len(sys.argv) < 7 :
    print ("Usages: sys_argv.py --flag1 number1 --flag2 number2 --flag3 number3")
    sys.exit()
else:
    print (sys.argv)
    
    if "--flag1" in sys.argv:
        f1loc=sys.argv.index("--flag1")
        val1=sys.argv[f1loc+1]
        
    if "--flag2" in sys.argv:
        f2loc=sys.argv.index("--flag2")
        val2=sys.argv[f2loc+1]
        
    if "--flag3" in sys.argv:
        f3loc=sys.argv.index("--flag3")
        val3=sys.argv[f3loc+1]
        
        
        
    
print ("result:"+ repr(int(val1)+int(val2)+int(val3)))


