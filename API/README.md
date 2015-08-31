#Python / PHP API for MCS

##### 使用 API 前必須先到 [MCS 網站個人檔案](https://mcs.mediatek.com/v2console/zh-TW/console/profile) 取得 app key 及 app secret 來進行登入，並取得要控制的裝置 id 

- 到 MCS 的個人檔案 -> 服務提供者 -> 申請 appId 和 appSecret 

![](http://i.imgur.com/gWShls8.png)

- 填寫資料並儲存

![](http://i.imgur.com/TUtqk0f.png)

- 記下 app key 及 app secret，會在之後的程式碼中用到

![](http://i.imgur.com/G41TU0K.png)

- 前往我的裝置 -> 選取裝置後記下 DeviceId

![](http://i.imgur.com/uqG4MSR.png)

---

Python API example

Python API 需要安裝 requests module
```bash
OSX / Linux: pip install requests
Windows: python -m pip install requests 
```

```python
from pymcs import *
import time

app_key = "YOUR_APP_KEY"
app_secret = "YOUR_APP_SECRET"
email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"

device_id = "DEVICE_ID"

# Get user token from MCS
r = get_user_token(app_key, app_secret, email, password)
if r:
    access_token = r['access_token']

    # Control GPIO_00
    send_data(access_token, device_id, "GPIO_00", 1)
    time.sleep(1)
    send_data(access_token, device_id, "GPIO_00", 0)
```

--- 

PHP API example

```php
<?php
    require_once('mcs.php');

    // Get access token from MCS
    $app_key = 'YOUR_APP_KEY';
    $app_secret = 'YOUR_APP_SECRET';
    $email = 'YOUR_EMAIL';
    $password = 'YOUR_PASSWORD';
    $device_id = 'DEVICE_ID';
    
    $access_token = get_user_token($app_key, $app_secret, $email, $password);
    
    // Control GPIO_00
    send_data($access_token, $device_id, 'GPIO_00', 1);
    Sleep(1);
    send_data($access_token, $device_id, 'GPIO_00', 0);
```
