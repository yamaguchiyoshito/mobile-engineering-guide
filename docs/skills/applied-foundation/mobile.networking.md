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

## このスキルについて

アプリからインターネット上のサーバーに問い合わせてデータを受け取り、画面に表示したり、入力内容を送信したりする技術です。モバイルアプリは電車の中や地下など通信が途切れやすい環境で使われるため、Webページ以上に、読み込み中の表示、失敗したときの再試行、オフライン時の振る舞いまで考える必要があります。最初に押さえるのは、HTTPのリクエストと応答の基本（メソッド、ステータスコード、JSON）と、通信は時間がかかるので画面を止めずに非同期で行うという原則です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公開されているAPIを1つ呼び出し、応答のJSONをデータ型に変換して一覧画面に表示する。送受信した内容をログやデバッグツールで確認する | [Foundation（URLSession）](https://developer.apple.com/documentation/foundation)・[ネットワーク接続（Android）](https://developer.android.com/training/basics/network-ops)・[ネットワーク（React Native）](https://reactnative.dev/docs/network) |
| Lv2 | 一覧と詳細の2画面を持つニュース閲覧アプリを作り、読み込み中の表示、ステータスコードごとのエラー表示、再読み込みを実装する。機内モードや不正な応答を再現して表示を確認し、通信部分をモックに差し替えたテストを書く | [Foundation（URLSession）](https://developer.apple.com/documentation/foundation)・[Retrofit](https://github.com/square/retrofit)・[ネットワーク（React Native）](https://reactnative.dev/docs/network)・[テスト（Android）](https://developer.android.com/training/testing) |
| Lv3 | タイムアウト、再試行、キャンセル、認証情報の付与をまとめた通信層を設計し、低速回線を再現して挙動を確かめる。既存アプリの通信処理を読み、エラー処理の抜けや安全でない通信設定を洗い出す | [OWASP MAS](https://mas.owasp.org/)・[セキュリティのヒント（Android）](https://developer.android.com/privacy-and-security/security-tips)・[セキュリティ（React Native）](https://reactnative.dev/docs/security) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| HTTP通信 | URLSession、Alamofire、Moya | OkHttp、Retrofit | fetch、axios |
| JSONの変換 | Codable | kotlinx.serialization／Moshi | JSON.parse、zodなどの検証ライブラリ |
| GraphQL・WebSocket | Apollo iOS、URLSessionWebSocketTask | Apollo（GraphQL） | WebSocket |
| 通信の安全性 | HTTPS／ATS | HTTPS／Network Security Config | 各OSの設定に従う（ATS、Network Security Config） |
| 接続状態の確認 | NWPathMonitor | ConnectivityManager | NetInfo |

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（Networking、HTTP/HTTPS、REST、GraphQL、URLSession、Alamofire、JSON/XML）／[SwiftUI](https://roadmap.sh/swift-ui)（Networking Libraries、Alamofire、Moya）／[Android](https://roadmap.sh/android)（Network、OkHttp、Retrofit、Apollo Android）／[React Native](https://roadmap.sh/react-native)（Networking、Fetch、WebSockets、Connectivity Status）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
