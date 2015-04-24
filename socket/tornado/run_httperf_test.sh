/usr/bin/httperf –hog –timeout=60 –client=0/1 –server=localhost –port=8080 –uri=/ –rate=400 –send-buffer=4096 –recv-buffer=16384 –num-conns=40000 –num-calls=10
