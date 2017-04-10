#coding:utf-8
import re
import os.path
import sys
import subprocess
import json
import types
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm

dictr = {}
def mkdir(path):
    path = path.strip()
    print "$$$$$$$$$$$$$$$$$$$$$$$$\n"
    #path = path.rstricp("\\")
    #print "$$$$$$$$$$$$$$$$$$$$$$$$\n"
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print 'create success'
        return True
    else:
        print 'is exists'
        return False


def handle_uploaded_file(filename, destfile):
    # destfile = destfile.strip()
    destination = open(destfile, 'wb+')
    for chunk in filename.chunks():
        destination.write(chunk)
    destination.close()
    print 'saved'

def write_file(request, filename):
    print '22222222\n'
    print 'filename:', filename
    UploadFileForm(request.POST, request.FILES)
    filename2 = request.FILES['file']  # 获取文件名
    # string = '' + filename2

    print 'filename: ', filename2
    if re.findall('mapping', filename):
        print 'fksjkl'
        handle_uploaded_file(filename2, "mapping.txt")
    elif re.findall('stacks', filename):
        handle_uploaded_file(filename2, "stacks.txt")
    else:
        handle_uploaded_file(filename2, "other.txt")


def call_jar():
    cmdargs = sys.argv
    input1 = 'mapping.txt'
    input2 = 'stacks.txt'
    res1 = find_file(input1)
    res2 = find_file(input2)
    if res1 and res2:
        output = 'Retrace.txt'
        with open(output, 'a') as f_output:
            subprocess.Popen(['java', '-jar', './proguard5.3.2./lib/retrace.jar', input1, input2], stdout=f_output)
        return True
    else:
        return False


def find_file(filename):
    filename = filename.strip()
    FileExists = os.path.exists(filename)
    if not FileExists:
        return False
    else:
        return True


def getdata(request):
    try:
        data = request.read()
        return data
    except:
        return None


def split_data(data, key):
    data1 = eval(data)
    value = data1.get(key, None)
    if value == None:#没有key对应的值返回None
        return None
    else:
        return value


def data_process(request):#获取数据段
    dictr={}#每次重新初始化字典
    data = getdata(request)
    if data.strip() == '' or data == None:
        data = None
        dict1 = {'result': 'fail', 'stacks': data, 'reason': 'data is empty'}
        dictr.update(dict1)
        return dictr
    else:
        res = get_proguarded_data(data)
        dictr.update(res)
        return dictr

def get_proguarded_data(data):
    li1 = []
    stack = split_data(data, 'stacks')#获取stacks段
    res = find_file('mapping.txt')
    if res == False:
        dict1 = {'result': 'fail', 'reason': 'no search ./mapping.txt'}
        return dict1
    if stack == None:
        dict1 = {'result': 'fail', 'stacks': None, 'reason': 'stacks is not exists'}
        return dict1
    else:
        if type(stack) is types.StringType:#stacks 是一个字符串
            stack2 = re.findall(r'\w*\.\w*\..*', stack)
            if stack2:#第一次提取匹配字符串
                stack2 = stack2[0]
                stack3 = re.findall(r'^(.+?)\(', stack2)
                if stack3:#第二次提取待字符串匹配成功
                    str1 = stack3[0]
                    res = Search(str1, stack)
                    if res == 'open file fail':
                        dict1 = {'result': 'fail', 'stacks': stack, 'reason': 'open file fail'}
                        return res
                    else:
                        dict1 = {'stacks': res}
                        res.update(dict1)
                        return res
                else:#stacks无效
                    dict1 = {'result': 'successful', 'stacks': stack}
                    return dict1

            else:#stacks无效
                dict1 = {'result': 'successful', 'stacks': stack}
                return dict1
        else:#stacks 是一个列表
            #print '*********************************\n'
            #print 'stacks: ', stack
            #print 'type stack: ', type(stack)
            for v in stack:
                #print 'type v : ', type(v)
                stack2 = re.findall(r'\w*\.\w*\..*', v)

                if stack2:  # 第一次提取匹配字符串
                    stack2 = stack2[0]
                    stack3 = re.findall(r'^(.+?)\(', stack2)
                    if stack3:  # 第二次提取待字符串匹配成功
                        str1 = stack3[0]
                        #print 'str1: ', str1
                        res = Search(str1, v)
                        #print "res: ", res
                        #print '111111111111111111111\n'
                        li1.append(res)
                    else:
                        li1.append(v)
                else:
                    li1.append(v)
            dict1 = {'result': 'successful', 'stacks': li1}
            return dict1


def Search(source, stack):
    #res = find_file('mapping.txt')
    length = len(source)
    index = source.rfind('.')
    str1 = source[0:index]#保存混淆前缀
    str2 = source[index+1:length]#保存混淆内容
    f = open('mapping.txt', 'r')
    res = match_string(f, str1, str2, stack)
    f.close()
    return res


def match_string(file1, str1, str2, stack):
    flag = 0
    string = ''
    lis1 = []
    while 1:
        line = file1.readline()
        if not line:
            if flag == 1:
                break
            else:
                flag = -1
                break
        if flag == 1 or flag == -1:
            break
        str3 = ')' + ' -> ' + str2
        if (str1 in line) and (':' in line) and ('(' not in line) and (')' not in line):  # 定位到查找起始位置
            while 1:
                line2 = file1.readline()
                #print 'line2>>: ', line2
                if not line2:
                    if flag == 1:
                        break
                    else:
                        flag = -1
                        break
                line2 = line2.strip()
                length = len(line2)
                if line2[length - 1] == ':':  # 另一种类型，则结束匹配，说明找不到匹配
                    #print '_____________\n'
                    #print 'line2: ', line2
                    if flag == 1:
                        break
                    else:
                        flag = -1
                        break
                else:
                    line2 = line2.replace('\n', '')
                    line2 = line2.strip()
                    str3 = str3.strip()
                    if line2.endswith(str3):  # # 在此行匹配成功
                        line3 = re.findall(' .*\(', line2)
                        str4 = str(line3[0])
                        str5 = str4.replace('(', '')
                        str5 = str5.strip()
                        str5 = str5.split(' ')
                        leng = len(str5)
                        lis1.append(str(str5[leng - 1]))
                        flag = 1
                    else:
                        continue
        else:
            continue
    if flag == 1:
        length = len(lis1)
        strl = str(lis1[0])
        str3 = '.' + str2 + '('
        if length == 1:
            strl = str(lis1[0])
            strl = strl.strip()
            strl = str(strl)
            strl = '.' + strl + '('
            stack = stack.replace(str3, strl)
            #dict1 = {'result': 'successful', 'stacks': stack}
            #print '22222:', stack
            return stack
        else:
            for i in range(1, length):
                if i == 1:
                    strl = strl + '(' + str(lis1[i])
                else:
                    strl = strl + ' | ' + str(lis1[i])
            strl = strl+')'
            #print 'strl::', strl
            strl = '.' + strl + '('
            stack = stack.replace(str3, strl)
            #dict1 = {'result': 'successful', 'stacks': stack, 'reason': 'but too many function name is %s'%(str2)}

            #return dict1
            #print '22222:', stack
            return stack

    else:
        #print '**************1111111111111111111\n'
        #dict1 = {'result': 'fail', 'reason': 'not find match'}
        #return dict1
        #print '333:', stack
        return stack
