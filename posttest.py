#coding:utf-8
import httplib 
import urllib
import sys
import requests
import json

def data():
	#conn = httplib.HTTPConnection("127.0.0.1:8000")   #请求http服务器，这里的ip.ip.ip.ip要换成服务器端所在ip  
	#print "requesting..." 
	#params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
	
	#payload = {'key1': 'value1', 'key2': ['value2', 'value3'], 'stacks': "03-30 14:37:24.107  1258  1258 E AndroidRuntime: FATAL EXCEPTION: main"}
	#payload = {'key1': 'value1', 'key2': ['value2', 'value3'], 'stacks': "03-30 14:37:24.107  1258  1258 E AndroidRuntime: java.lang.RuntimeException: he ate a table yesterday."}
	
	
	payload = {'key1': 'value1',
	'key2': ['value2', 'value3'], 
	'stacks': [
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime: FATAL EXCEPTION: main",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime: Process: chencanmao.ndkprofiler1, PID: 1258",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime: java.lang.RuntimeException: he ate a table yesterday.",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at chencanmao.ndkprofiler1.Pong.Action(Unknown Source)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at chencanmao.ndkprofiler1.Pong.d(Unknown Source)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at chencanmao.ndkprofiler1.MainActivity$1.onClick(Unknown Source)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at android.view.View.performClick(View.java:5207)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at android.view.View$PerformClick.run(View.java:21177)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at android.os.Handler.handleCallback(Handler.java:739)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at android.os.Handler.dispatchMessage(Handler.java:95)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at android.os.Looper.loop(Looper.java:148)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at android.app.ActivityThread.main(ActivityThread.java:5458)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at java.lang.reflect.Method.invoke(Native Method)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:738)",
	"03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:628)",
	"03-30 14:37:39.553  3291  3291 E AndroidRuntime:        at com.xsj.crasheye.NetSender.a(Unknown Source)"
	]}
	
	#payload = {'appkey': '123456', 'version': 1, 'stacks': "03-30 14:37:24.107  1258  1258 E AndroidRuntime:        at android.os.Looper.loop(Looper.java:148)"}
	#payload = {'appkey': '123456', 'version': 1, 'stacks': "03-30 14:37:39.553  3291  3291 E AndroidRuntime:        at chencanmao.ndkprofiler1.Pong.c(Unknown Source)"}
	#payload = {'appkey': '123456', 'version': 1, 'stacks': "03-30 14:37:39.553  3291  3291 E AndroidRuntime:        at com.xsj.crasheye.NetSender.a(Unknown Source)"}
	#payload = {'key1': 'value1', 'key2': ['value2', 'value3']}  
	#request = requests.c
	#file1 = {'file': open('stacks.txt','rb')}
	js = json.dumps(payload)
	#r1 = requests.post("http://127.0.0.1:8000",data = {'hash':'jskldfjs'},files = file1)
	#file2 = {'file': open('mapping.txt','rb')}
	#r3 = requests.post("http://127.0.0.1:8000",files = file2)
	r2 =requests.post('http://127.0.0.1:8000/index/',json = payload)
	#r2 =requests.post('http://10.20.126.19:8000',json = payload)
	#sys.stdout.flush()
	#str1 = raw_input("str1 input: ")
	#sys.stdin.flush()
	#str2 = raw_input("str2 input: ")
	#sys.stdin.flush()
	#headers = {"134556":"AAAAAAAAAA"}
	#headers = {str1 : str2}
	#conn.request("GET", "/")   #发出GET请求并制定请求的文件路径 
	#conn.request("GET", "/", params, headers,)
	
	#r1 = conn.getresponse()
	#print 'r1.txt: ', r1.text
	#print 'r1.headers: ', r1.headers
	print 'r2.txt: ', r2.text
	#print 'r2.headers: ', r2.headers
'''	
	print r1.status, r1.reason      #打印响应码和响应状态信息 

	try: 
	  data1 = r1.read()         #读响应内容 
	except: 
	  print "exception!" 
	finally: 
	  print "read response!" 
	print "data1:", data1               #打印响应内容 
	#print 'header: ',r1.getheader
	conn.close() 
'''
def main():
	data()
	
main()