from wcferry import Wcf

wcf = Wcf()

# 检查登录
if not wcf.is_login():
    print("请扫码登录微信！")
    wcf.get_qrcode()

# 遍历好友列表
friends = wcf.get_friends()
print(f"好友总数：{len(friends)}")

# 开启消息监听
wcf.enable_receiving_msg()

# 消息循环
while True:
    msg = wcf.get_msg()
    if not msg:
        continue
    # 只处理雪雪消息
    if msg.sender == "wxid_40tgvd7yg95g22":
        print(f"收到雪雪消息：{msg.content}")
        # 自动回复
        wcf.send_text("收到啦", msg.sender)