# Kalman

http://www.mdpi.com/sensors/sensors-12-03049/article_deploy/html/images/sensors-12-03049f5.png



sudo add-apt-repository ppa:jonathonf/gcc-7.1

sudo add-apt-repository ppa:acooks/libwebsockets6

sudo apt-get update

sudo apt-get install git build-essential cmake libuv1-dev libmicrohttpd-dev gcc-7 g++-7


####################http://iot-watch.com/69#################
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
もとの v4.1 はそっとしておいて、Androidを扱う時だけ v3.81 を使うようにすると他に影響がなくてよいかと思います。
単純に .profile あたりに下記のパス設定の記述を追加します。/fooとしたパス部分は環境に合わせて変更してください。


PATH="/foo/make3.8.1:$PATH"

これで source ~/.profile などすれば make3.8.1 を作ったパスが優先されます。

v4.1を使いたくなったときはこのパス記述を削って source ~/.profile すればOKです。


