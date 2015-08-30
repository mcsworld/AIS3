#Python / PHP API for MCS

Python API example

```python
from pymcs import *

app_key = "YOUR_APP_KEY"
app_secret = "YOUR_APP_SECRET"
email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"

deviceId = "DEVICE_ID"
deviceKey = "DEVICE_KEY"

# Get user token from MCS
r = get_user_token(app_key, app_secret, email, password)
if r:
    access_token = r['access_token']

    # Control GPIO
    send_data(access_token, deviceId, "GPIO_00", 1)
    time.sleep(1)
    send_data(access_token, deviceId, "GPIO_01", 0)
```
