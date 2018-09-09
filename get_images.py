import itchat
itchat.auto_login(hotReload=True)
for friend in itchat.get_friends(update=True)[0:]:
    print(friend['NickName'],friend['RemarkName'],friend['Sex'],friend['Province'],friend['Signature'])
    img=itchat.get_head_img(userName=friend['UserName'])
    path="/home/lsgo30/下载/Wechat_images/images/"+friend['NickName']+'('+friend['RemarkName']+').jpg'
    with open(path,'wb') as f:
        f.write(img)
itchat.run()