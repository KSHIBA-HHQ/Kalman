# Kalman

http://www.mdpi.com/sensors/sensors-12-03049/article_deploy/html/images/sensors-12-03049f5.png


# hint
https://www.youtube.com/watch?v=J7WK9gEUltM&feature=youtu.be

#######################################

sudo add-apt-repository ppa:jonathonf/gcc-7.1

sudo add-apt-repository ppa:acooks/libwebsockets6

sudo apt-get update

sudo apt-get install git build-essential cmake libuv1-dev libmicrohttpd-dev gcc-7 g++-7

#############  Docker   ####################################
https://classroom.udacity.com/nanodegrees/nd013/parts/40f38239-66b6-46ec-ae68-03afd8a601c8/modules/0949fca6-b379-42af-a919-ee50aa304e6a/lessons/f758c44c-5e40-4e01-93b5-1a82aa4e044f/concepts/16cf4a78-4fc7-49e1-8621-3450ca938b77

docker run -it -p 4567:4567 -v 'pwd':/work udacity/controls_kit:latest


############ ubuntu 14  try gcc-upgrade #############
http://iot-watch.com/69

make v3.81 のソースをダウンロード
取得元の公式はこちらです。ここに v3.81 がありますので取得します。
http://ftp.gnu.org/gnu/make/


$ wget "http://ftp.gnu.org/gnu/make/make-3.81.tar.bz2"

$ tar xjf make-3.81.tar.bz2

$ cd make

解凍してビルド
tarを解凍して、configureしてmakeします。

$ ./configure

$ make

パスを通す
単純に .profile あたりに下記のパス設定の記述を追加します。/fooとしたパス部分は環境に合わせて変更してください。


PATH="/foo/make3.8.1:$PATH"

これで source ~/.profile などすれば make3.8.1 を作ったパスが優先されます。

v4.1を使いたくなったときはこのパス記述を削って source ~/.profile すればOKです。


