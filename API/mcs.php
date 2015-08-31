<?php

/**
 * Get user token from MCS
 * @return json object responsed from MCS server
 */
function get_user_token($app_key, $app_secret, $email, $password)
{
	$url = 'https://mcs.mediatek.com/oauth/login/thirdpart';
	$data = array('email' => $email, 'password' => $password);

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data)); 
	curl_setopt($ch, CURLOPT_USERPWD, $app_key . ":" . $app_secret);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	$response = curl_exec($ch); 
	curl_close($ch);
	$r = json_decode($response);
	if ( $r->code != 200 )
	{
		echo $r->message;
		return;
	}

	return $r->access_token; 
}


/**
 * Refresh user token from MCS
 * @return json object responsed from MCS server
 */
function refresh_user_token($app_key, $app_secret, $token)
{
	$url = 'https://mcs.mediatek.com/oauth/login/thirdpart/refresh';
	$data = array('token' => $token);

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data)); 
	curl_setopt($ch, CURLOPT_USERPWD, $app_key . ":" . $app_secret);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	$response = curl_exec($ch); 
	curl_close($ch);

	return json_decode($response)->results;
}

function send_data($access_token, $device_id, $chn_id, $value) 
{
	$url = 'https://api.mediatek.com/mcs/v2/devices/' . $device_id . '/datapoints';
	$header = array('Authorization: Bearer ' . $access_token,
					'Content-Type: application/json');
	$data = '{"datapoints": [{"values": {"value": ' . $value . '}, "dataChnId": "' . $chn_id. '"}]}';

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $data); 
	curl_setopt($ch, CURLOPT_HTTPHEADER, $header);	
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	$response = curl_exec($ch); 
	curl_close($ch);

	$r = json_decode($response);
	if ( $r->code != 200 )
	{
		echo $r->message;
		return false;
	}
	return true;
}
