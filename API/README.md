#Python / PHP API for MCS

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

    # Control GPIO
    send_data(access_token, device_id, "GPIO_00", 1)
    time.sleep(1)
    send_data(access_token, device_id, "GPIO_00", 0)
```

PHP API example

```php
<?php
    require_once('mcs.php');

    // Get access token from MCS
    $app_key = 'YOUR_APP_KEY';
    $app_secret = 'YOUR_APP_SECRET';
    $email = 'YOUR_EMAIL';
    $password = 'PASSWORD';
    $device_id = 'DEVICE_ID';
    
    $access_token = get_user_token($app_key, $app_secret, $email, $password);
    
    // Control GPIO port
    send_data($access_token, $device_id, 'GPIO_00', 1);
    Sleep(1);
    send_data($access_token, $device_id, 'GPIO_00', 0);
```
