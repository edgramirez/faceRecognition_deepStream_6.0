{
        "98:18:88:ba:bf:14": {
            "source": "file:///home/aaeon/amlo.mp4",
            "services": [
		                {
		                    "whiteList": {
		                        "enabled": true,
		                        "endpoint": "http://3.219.81.19:8888/posts/whiteList"
		                    }
		                },
		                {
		                    "blackList": {
		                        "enabled": "True",
		                        "endpoint": "http://3.219.81.19:8888/posts/blackList"
		                    }
		                },
		                {
		                    "ageAndGender": {
		                        "enabled": true,
		                        "endpoint": "http://3.219.81.19:8888/posts/ageAndGender"
		                    }
		                }
                        ]
                },
        "00:04:4b:eb:f6:14": {
            "source": "rtsp://192.168.129.14:9000/live",
            "services": [
		                {
		                    "whiteList": {
		                        "enabled":"False",
		                        "endpoint": "http://3.219.81.19:8888/posts/blackAndWhite"
		                    }
		                },
		                {
		                    "blackList": {
		                        "enabled":"False",
		                        "endpoint": "http://3.219.81.19:8888/posts/blackAndWhite"
		                    }
		                },
		                {
		                    "ageAndGender": {
		                        "enabled":"False",
		                        "endpoint": "http://3.219.81.19:8888/posts/ageAndGender"
		                    }
		                }
                        ]
                },
        "00:04:4b:eb:f6:pp": {
            "source":"rtsp://192.168.129.15:9000/live"
            }
}
