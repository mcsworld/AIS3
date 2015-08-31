# AIS3 Lab

#### 讓 MT7681 連上 [MediaTek Cloud Sandbox](https://mcs.mediatek.com/oauth/zh-TW/signup) ，並透過網際網路控制晶片
##### 1. 註冊 MCS 帳號
- 前往 [MCS 註冊頁面](https://mcs.mediatek.com/oauth/en/signup) 申請一個帳號並登入，需要進行 e-mail 驗證，請填寫可用的信箱帳號

---

##### 2. 建立產品原型，有了產品原型才能將雲端上的設定與實際晶片連結在一起
- 登入後點擊畫面上方的 `開發`
- 在產品原型清單頁面中，點擊創建按鈕來新增一個新的產品原型

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_01.png)

- 輸入自訂產品原型名稱，版本，並選擇產業別。硬體平台請選擇 `MT7681`，之後點擊儲存按鈕
![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_02.png)

---

##### 3. 為產品原型建立資料通道，資料通道是用來連結控制晶片上的腳位訊號
- 點擊剛新建好的產品原型下方的詳情按鈕
![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_03.png)

- 點擊資料通道分頁，並點擊新增按鈕。
![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_05.png)

- 建立資料通道，資料通道名稱輸入 `GPIO 00`，資料通道 ID 請輸入 `GPIO_00`，並且選擇 GPIO 資料型態並儲存
![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_06.png)

- 接著以同樣步驟新增第二個資料通道，這次資料通道名稱輸入 `GPIO 01` ，資料通道 ID 請輸入 `GPIO_01`，選擇 GPIO 資料型態並儲存

---

##### 4. 更新晶片上的韌體
- 請下載並安裝作業系統對應版本的 [VCP Driver](http://www.ftdichip.com/Drivers/VCP.htm)

- 將晶片以 Micro-USB 傳輸線連接至電腦
 
- Windows 系統使用者: 開啟我的電腦->右鍵內容->裝置管理員，找到 COM 連接埠的編號 (例如下圖為 COM3)
![](http://i.imgur.com/e3gd0kW.png)

- 執行提供的 mt7681_uploader.py 或 mt7681_uploader.exe (位於 Files 資料夾)，依照上個步驟所找到的 COM 編號，輸入對應參數，例如 `mt7681_uploader.exe -c COM3 -f MT7681_sta_header.bin` 來更新韌體

![](http://i.imgur.com/JdAGs4J.png)
![](http://i.imgur.com/hpMdBDo.png)

---

- OSX 系統使用者: 於 Terminal 執行 `ls /dev/tty.usbserial*`，應該可以找到對應的 tty name
- 以 python 執行 `python mt7681_uploader.py -c /dev/tty.usbserial-DB0078CI -f MT7681_sta_header.bin` 來更新韌體

![](http://i.imgur.com/L0d0HFv.png)

- 等待韌體更新完畢，若過程中出現 Enter Recovery Mode Failed 相關訊息，請手動按一下晶片上的重置按鈕，再按下鍵盤上的任意鍵繼續執行

---

#### 5. 進行 Smart Connection
- 此步驟會透過 Android 手機將實體晶片與前面在 MCS 所建立的原型連接在一起，讓我們能夠直接透過網路來控制晶片動作

- 此步驟比較可能會遇到問題，可請助教群協助

- 透過掃描 QRCode 安裝 MCS 手機 APP

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_00.png)

- 或是從 Google Play 搜尋 [MediaTek Cloud Sandbox](https://play.google.com/store/apps/details?id=com.mediatek.iotcloud&hl=zh_TW) 安裝

![](http://i.imgur.com/LT9HwNW.png)

- 開啟 APP 登入後，點選下方的新增按鈕

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_09.png)

- 點擊畫面下方的 Smart Connection 按鈕

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_10.png)

- 輸入無線網路的 SSID 和密碼後點選開始。正常情況下，SSID 會自動帶入手機所連線至的無線網路
- 在 AIS3 教室請輸入 `AIS3` 及 `ais3{2015}`

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_11.png)

- 等待幾秒後，如果 Smart Connection 成功，將會看到晶片出現在列表上，找到 MAC Address 對應的晶片並點選

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_13.png)

- 選取剛剛在網站新增的原型

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_14.png)

- 輸入自訂名稱及描述後儲存

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_15.png)

- 點選進入裝置後即可透過手機或 MCS 網頁以及 API 來控制晶片上的 GPIO 腳位訊號

![](https://img.mediatek.com/1500/mtk.linkit/mcs-resources/zh-TW/2.8.5/LinkIt_Connect/img_linkitconnect7681_22.png)


---


##### 附錄. 透過腳本修改晶片所使用的無線網路訊號

- 由於並非所有學員都有 Android 手機，如果在課程結束後，想要使用自己的無線網路熱點讓晶片連上網路，可以使用提供的 `set_ap.exe` 或 `set_ap.py` 進行晶片上 WiFi 設定的修改
- 將晶片以 Micro-USB 傳輸線連接上電腦後，透過 `set_ap.exe` 來設定目標無線網路的 SSID 以及密碼
- 例如想要讓晶片連接的 WiFi 名稱為 `Free Wifi`，密碼為 `12345678`，則輸入 `set_ap.exe -c COM3 -s "Free WiFi" -p "12345678"` ，執行後將會重新修改晶片設定並嘗試連接至目標無線網路
- 或是使用 python 執行 `python set_ap.py -c COM3 -s "Free WiFi" -p "12345678"`
- 注意: 若無線網路名稱含有中文，可能無法正常連線

##### 附錄2. 透過腳本重置晶片設定

- 若發生問題需要重置晶片上的所有設定，可以透過 mt7681_uploader.exe 重置
- 執行 `mt7681_uploader.exe -c COM3 --default` 即可重置所有設定
- 注意: 重置設定後必須重新使用 Android App 進行 Smart Connection 才能讓晶片重新連上網路
