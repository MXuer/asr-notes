#coding=utf-8
#! python
# 逐行合并两个文件

import sys;
import re;
import os;

punct_str = "«»...ㆍ·！＂％）（，﹐]｝\：’‘；[“”｛？“\"。、﹑!﹗'`%﹪》《().﹒,【】;﹔~:︰﹕}|?﹖{﹛><———………＠@#￥&*-=+−×÷＃＆＋－／．＝～﹢‐―℃』『」「〝㏄≠≦≧$＄﹩/∩_^＾ˇ·⊙–※ˉ┐┌─︶︿﹁﹀﹏﹌﹋﹣＊＜＞＿￣　●↑↓←→◎˙ˋˊ〈〉〔〕﹝﹞﹚﹙〞∕☆★［］′‵○﹍‥╮╭｀√│╰╯︵▽＼﹃╬‰∵∮▌△╳└◇┘∶╥┴Д≡｜┬дΣ□〃°∞∥⊿┻━ᵒ̤∠┸〒ᴗ┑┍".decode('utf-8');


def edit_dist_str(str1, str2):
    if not str1 or not str2:
        print "Error, str1 or str2 is null, please check!";
        return -1;

    n = len(str1);
    m = len(str2);

    if n == 0:
        return m;
    elif m == 0:
        return n;

    if n > m:
        tmp = str1;
        str1 = str2;
        str2 = tmp;
        n = m;
        m = len(str2);

    p = []; ## 'previous' cost array, horizontally
    d = []; ## cost array, horizontally;
    _d = []; ## placeholder to assist in swapping p and d;

    ## indexes into strings str1 and str2;
    for i in range(n+1): ## iterates through str1;
        p.append(i);

    for j in range(m+1): ## iterates through str2;
        d.append(j);

    for j in range(1, m+1):
        t_j = str2[j-1]; ## jth character of str2;
        d[0] = j;

        for i in range(1, n+1):
            if str1[i-1] == t_j:
                cost = 0;
            else:
                cost = 1;
            d[i] = min(min(d[i-1]+1, p[i]+1), p[i-1]+cost);

        _d = p;
        p = d;
        d = _d;

    return p[n];


def edit_dist_list(wd_list_1, wd_list_2):
    if not wd_list_1 or not wd_list_2:
        print "Error, wd_list_1 or wd_list_2 is null, please check!";
        return -1;

    n = len(wd_list_1);
    m = len(wd_list_2);

    if n == 0:
        return m;
    elif m == 0:
        return n;

    if n > m:
        tmp = wd_list_1;
        wd_list_1 = wd_list_2;
        wd_list_2 = tmp;
        n = m;
        m = len(wd_list_2);

    p = [];
    d = [];
    _d = [];

    for i in range(n+1):
        p.append(i);

    for j in range(m+1):
        d.append(j);

    for j in range(1, m+1):
        wd_j = wd_list_2[j-1];
        d[0] = j;

        for i in range(1, n+1):
            cost = 0;
            if wd_list_1[i-1] == wd_j:
                cost = 0;
            else:
                cost = 1;
            d[i] = min(min(d[i-1]+1, p[i]+1), p[i-1]+cost);
        
        _d = p;
        p = d;
        d = _d;

    return p[n];


def handle_file(input_path_1, input_path_2, output_path):
        if not os.path.exists(input_path_1):
                print "Error, file "+input_path_1+" not exists!"
                return
        if not os.path.exists(input_path_2):
                print "Error, file "+input_path_2+" not exists!"
                return
        
        fpw = open(output_path, 'w')

        lineMap = {}
        dmp = diff_match_patch();

        lineNum = 0

        fr1 = open(input_path_1)
        fr2 = open(input_path_2)

        line1 = fr1.readline()
        line2 = fr2.readline()
        while line1 and line2:
                lineNum += 1

                #fpw.write(line1[:-1]+"\t"+line2[:-1]+"\n")
##                fpw.write(line1[:-1]+"\n")
##                fpw.write(line2[:-1]+"\n")
                
                
                line1 = fr1.readline()
                line2 = fr2.readline()


##        new_line,num = re.subn(u"[^\u4e00-\u9fa5]+", "", new_line)
        
def handle_dir(input_path_1, input_path_2, output_path):
        if not os.path.exists(input_path_1):
                print "Error, dir "+input_path_1+" not exists!"
                return
        if not os.path.exists(input_path_2):
                print "Error, dir "+input_path_2+" not exists!"
                return

        if not os.path.isdir(input_path_1):
                print "Error, "+input_path_1+" is not directory!"
                return
        if not os.path.isdir(input_path_2):
                print "Error, "+input_path_2+" is not directory!"
                return

        if not os.path.exists(output_path):
                os.mkdir(output_path)

        file_list = os.listdir(input_path_1)
        for file_name in file_list:
                if os.path.isdir(input_path_1+"/"+file_name):
                        handle_dir(input_path_1+"/"+file_name, input_path_2+"/"+file_name, output_path+"/"+file_name)
                else:
                        handle_file(input_path_1+"/"+file_name, input_path_2+"/"+file_name, output_path+"/"+file_name)


        #print "Complete "+input_path_1+" !"

def handle(input_path_1, input_path_2, output_path):

    if os.path.isdir(input_path_1):
        handle_dir(input_path_1, input_path_2, output_path)
    else:
        handle_file(input_path_1, input_path_2, output_path)


if __name__ == '__main__':
        if len(sys.argv)<4:
                print "Usage: python %s input_path_1, input_path_2, output_path" % sys.argv[0]
                exit(-1);
        else:
                input_path_1 = sys.argv[1]
                input_path_2 = sys.argv[2]
                output_path = sys.argv[3]
                handle(input_path_1, input_path_2, output_path);
##                #wd_list_1 = "g o o d".split(" ");
##                #wd_list_2 = "g e a o d o".split(" ");
##                #edit_difstr_list(wd_list_1, wd_list_2);
##                str1 = "Hello World.";
##                str2 = "Goodbye World.";
##                edit_difstr(str1, str2);
                
                

