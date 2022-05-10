# DropBox Developers 
※ログイン必要
(https://www.dropbox.com/developers/documentation)
### Dropbox Github
(https://github.com/dropbox)

手順
- ログイン、
- Appの作成[create App]
 この時に注意するのは、AppのScoped access設定を[Full Dropbox]にすること
 でないと、共有されたURLからファイルをダウンロードすることができない

- App keyをメモ
 [App key]、[App secret]をメモする

- 必要なライブラリをインストール
■Python
(https://github.com/dropbox/dropbox-sdk-python)
$ pip3 install dropbox

■JavaSDK
(https://github.com/dropbox/dropbox-sdk-java#setup)
(https://github.com/dropbox/dropbox-sdk-java/tree/master/examples/android)

- Access tokenを発行する
共有されたURLからファイルをダウンロードするにはこのトークンが必要となる
揮発性のため常時使用する場合はコードで自動発行が必要のよう※未解決
テストの場合は、Appのダッシュボードから手動で発行ができるのでそれを使用すると簡単