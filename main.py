from turtle import down
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
import requests

import os
from os.path import join, dirname
from dotenv import load_dotenv
from pprint import pprint
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_TOKEN = os.environ.get("Access_Token")
APP_KEY = os.environ.get("App_Key")
APP_SECRET = os.environ.get("App_Secret")

# auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY,
#                                         consumer_secret=APP_SECRET,
#                                         token_access_type='offline',
#                                         scope=['files.metadata.read'])

# with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
#     dbx.users_get_current_account()
#     print("Successfully set up client!")
    
    
    
dbx = dropbox.Dropbox(oauth2_access_token=ACCESS_TOKEN,
                app_key=APP_KEY, app_secret=APP_SECRET,)

# 共有リンクからメタデータを取得(=ファイルの名前を取得)
shared_link = dropbox.files.SharedLink(url='ここに共有リンクを貼り付ける')
share_dir_metadata = dbx.files_list_folder(path="", shared_link=shared_link)
pprint(share_dir_metadata)

# ファイルのメタデータを取得
# pprint(dbx.sharing_get_shared_link_file(url='ここに共有リンクを貼り付ける', path="/boots.jpg"))

# 共有リンクとファイル名からファイルをダウンロード
dbx.sharing_get_shared_link_file_to_file(download_path='./down.jpg', url='ここに共有リンクを貼り付ける', path='/ファイル名 (← / 大事)')