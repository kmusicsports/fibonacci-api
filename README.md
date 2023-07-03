# fibonacci-api

フィボナッチ数を返すAPI

URL: [https://czvuvbmb1h.execute-api.ap-northeast-1.amazonaws.com/fib](https://czvuvbmb1h.execute-api.ap-northeast-1.amazonaws.com/fib)

## 概要

- Python + AWS Lambda + Amazon API Gateway で開発したREST API
- Docker + Docker Compose でコンテナ化
- SymPYモジュールの[fibonacci()](https://docs.sympy.org/latest/modules/functions/combinatorial.html#sympy.functions.combinatorial.numbers.fibonacci)によってフィボナッチ数を計算

## ソースコード構成

```sh
fibonacci-api
 ├ .gitignore
 ├ docker-compose.yml
 ├ Dockerfile
 ├ README.md
 ├ requirements.txt
 └ src
     ├ app.py  # Lambda 関数ハンドラー, フィボナッチ数計算
     └ app_test.py # ユニットテスト
```

## 主なリソース(AWS)

- AWS Lambda
- Amazon Elastic Container Registry(ECR)
- Amazon API Gateway

## APIの仕様

### クエリ文字列パラメータ

```sh
n  # 1以上の整数値, フィボナッチ数列の順番を指定する値。1で先頭のフィボナッチ数を指定する
```

### リクエスト例

```sh
https://czvuvbmb1h.execute-api.ap-northeast-1.amazonaws.com/fib?n=99
```

### レスポンス例

#### 正常系

```json
{
    "result": 218922995834555169026
}
```

#### 異常系

```json
{
    "message": "Error: There is no 'n' that must be an integer larger than 0"
}
```

## コンテナのライフサイクル管理

必要条件: [Docker Desktop](https://www.docker.com/products/docker-desktop)

### ビルド&起動

```sh
docker compose up
```

### 停止&破棄

```sh
docker compose down
```

## ユニットテスト

必要条件: [pytest](https://pypi.org/project/pytest/)

```sh
pytest src/test_app.py
```
