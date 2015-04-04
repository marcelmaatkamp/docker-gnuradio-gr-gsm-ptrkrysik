# docker-gnuradio-gr-gsm-ptrkrysik

Start the image with extra privileges to access the rtlsdr dongle and expose a ssh-port: 
```
 $ docker run -ti --privileged -p 2224:22 marcelmaatkamp/gnuradio-gr-gsm-ptrkrys:latest
 
 root@gnuradio-gr-gsm-ptrkrys# /usr/sbin/sshd
```
Then add your ssh pubkey into /root/.ssh/authorized_keys2

In another terminal ssh into the box with X-forwarding enabled:
```
  $ ssh -X -p 2224 root@dockerhost
  
  root@gnuradio-gr-gsm-ptrkrys# locale-gen en_US en_US.UTF-8
  root@gnuradio-gr-gsm-ptrkrys# export LC_ALL="en_US.UTF-8"
  root@gnuradio-gr-gsm-ptrkrys# airprobe_rtlsdr.py
```

If you tune it right the terminal will display a flood of GSM messages:

![GSM Decoder](https://04a27ff1-a-62cb3a1a-s-sites.googlegroups.com/site/marcelmaatkamp/home/gsm-decoding-with-a-rtlsdr-dongle-and-ptrkrysik-s-gr-gsm/Schermafbeelding%202015-04-03%20om%2015.40.04.png)

I made a nogui version which will output the gsm stream:
```
 root@gnuradio-gr-gsm-ptrkrys# airprobe_rtlsdr_nogui.py -p 50 -g 50 -f 9.462e+08
```
