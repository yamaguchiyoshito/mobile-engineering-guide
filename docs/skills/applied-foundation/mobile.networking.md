---
title: "ネットワーク通信"
description: "ネットワーク通信の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# ネットワーク通信

**スキルID：** `mobile.networking`  
**スキル領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** 並行処理、JSON

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

HTTPのメソッド、ステータスコード、ヘッダー、JSONの変換、通信を非同期で行う理由を説明できず、APIを呼び出すには手順ごとの指示が必要である。

## Lv1

例に沿ってHTTPリクエストを送り、応答のJSONをデータ型へ変換して画面に表示できる。支援を受けて通信内容をログやデバッグツールで確認できる。

## Lv2

要件が明確なAPIについて、リクエストの生成、応答の変換、ステータスごとのエラー処理、読み込み中の表示を実装できる。通信失敗、オフライン、不正な応答を再現し、モックやテストで検証・修正できる。

## Lv3

タイムアウト、再試行、キャンセル、認証情報の付与、通信の安全性設定を含む通信層を設計できる。低速回線や応答形式の変更による不具合を分析し、通信方式（REST、GraphQL、WebSocket）や通信ライブラリを比較してレビューできる。

## Lv4

共通の通信クライアント、エラーの分類、モックサーバーや契約検証を含む自動テストを整備できる。他者の利用結果を基に、通信に起因する不具合と実装・調査工数の改善を確認し、共通部品を更新できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | URLSession、Codable、Alamofire、Moya、HTTPS／ATS |
| Android | OkHttp、Retrofit、kotlinx.serialization／Moshi、Apollo（GraphQL） |
| React Native | fetch、axios、WebSocket、NetInfo |

roadmap.sh の参照トピック：ios: networking, http--https, rest, graphql, urlsession, alamofire, json--xml, parsing, serializing / android: network, okhttp, retro, apollo-android / swift-ui: networking-libraries, alamofire, moya / react-native: networking, fetch, websockets, connectivity-status

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
