import requests
url = "http://192.168.0.1" #python自学的写的比较乱

head0 = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"
  }

date0 = "{'method':'do','login':{'password':'WacVBgNWBywL88Mc'}}" #password需要自己抓包查看
#stok相当于cookie
res1 = requests.post(url,headers=head0,data=date0)

eko = res1.text
eko1 = eko.replace('{"error_code":0, "stok":"', '')#把返回结果只留下stok
stok = eko1.replace('"}', '')
print(stok)

url1 = 'http://192.168.0.1/stok={}/ds'.format(stok)
head1 = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49",

  }

date1 = '{"hosts_info":{"set_block_flag":{"mac":"f0-6d-78-a0-94-91","is_blocked":"0","name":"AdminisiiPhone3","down_limit":"0","up_limit":"0","forbid_domain":"","limit_time":""}},"method":"do"}'
         #mac为mac地址 is_blocked(是否禁用该设备):0为否 1为禁用 name为该设备名称 down_limit为下载速度 up_limit为上传速度 单位为KB(值为0不限速)
res = requests.post(url=url1,headers=head1,data=date1)
print (res.text)#返回{"error_code":0}表示成功
     
    
    
    

    
    
    

   

    
