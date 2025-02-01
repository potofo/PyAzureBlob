# Azure Blob Storage 操作ツール

## 概要

このプロジェクトは、Azure Blob Storageを操作するためのPythonスクリプト群です。以下の機能を提供します：

- Blobコンテナ内のファイル一覧表示
- Blobからのファイルダウンロード
- Blobへのファイルアップロード

## 前提条件

- Python 3.x
- Azureアカウント
- Azure Storageアカウント
- 必要なPythonパッケージ:
  - azure-identity==1.19.0
  - azure-storage-blob==12.24.1
  - python-dotenv==1.0.1

## セットアップ

1. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

2. 環境変数の設定:
`.env_template` ファイルを `.env` にコピーし、以下の情報を設定します：

```
AZURE_STORAGE_CONNECTION_STRING_TEMPLATE="DefaultEndpointsProtocol=https;AccountName={AZURE_STORAGE_ACCOUNT};AccountKey={AZURE_STORAGE_KEY};EndpointSuffix=core.windows.net"
AZURE_STORAGE_ACCOUNT="<your-storage-account-name>"
AZURE_STORAGE_KEY="<your-storage-account-key>"
AZURE_STORAGE_CONTAINER_NAME="<your-container-name>"
```

必要な情報は以下の場所で確認できます：
- Storage Account Name: Azure Portal -> Storage Account -> 概要
- Storage Account Key: Azure Portal -> Storage Account -> セキュリティ + ネットワーク -> アクセスキー
- Container Name: Azure Portal -> Storage Account -> ストレージ エクスプローラー -> BLOBコンテナー

## 使用方法

### Blobリストの表示

```bash
python ListBlob.py
```

コンテナ内のすべてのBlobのリストが表示されます。

### Blobのダウンロード

```bash
python DownloadBlob.py
```

指定したBlobを `downloads` ディレクトリにダウンロードします。
ディレクトリ構造は自動的に作成されます。

### Blobのアップロード

```bash
python UploadBlob.py
```

ローカルファイルをBlobストレージにアップロードします。
既存のBlobは上書きされます。

## プロジェクト構造

```
PyAzureBlob/
├── .env_template          # 環境変数テンプレート
├── .gitignore            # Gitの除外設定
├── ListBlob.py           # Blob一覧表示スクリプト
├── DownloadBlob.py       # Blobダウンロードスクリプト
├── UploadBlob.py         # Blobアップロードスクリプト
├── requirements.txt      # 依存パッケージリスト
├── downloads/            # ダウンロードしたファイルの保存先
└── uploads/              # アップロードするファイルの配置先
```

## 参考リンク

- [Azure Blob Storage Documentation](https://learn.microsoft.com/ja-jp/azure/storage/common/storage-samples-python)
- [Azure Blob Upload Python](https://learn.microsoft.com/ja-jp/azure/storage/blobs/storage-blob-upload-python)
- [Azure Blob Download Python](https://learn.microsoft.com/ja-jp/azure/storage/blobs/storage-blob-download-python)