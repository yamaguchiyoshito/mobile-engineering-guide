---
title: "データ永続化"
description: "データ永続化の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# データ永続化

**スキルID：** `mobile.persistence`  
**スキル領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** 並行処理、モバイル基礎

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## このスキルについて

アプリが扱うデータを端末の中に保存し、次回起動時や通信できないときにも使えるようにする技術です。Webアプリと違い、モバイルアプリは端末に閉じた保存領域（サンドボックス）を持ち、設定値、構造化データ、ファイル、パスワードなどの秘密情報で保存先を使い分けます。最初に押さえるのは、保存先ごとの用途の違いと、秘密情報を通常のデータと同じ場所に置かないという原則です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

設定値、ファイル、データベース、秘密情報の保存先の違いや、アプリ専用の保存領域の仕組みを説明できず、データを保存するには手順ごとの指示が必要である。

## Lv1

例に沿って設定値やデータを保存・読み込みし、アプリの再起動後も値が残ることを確認できる。支援を受けて保存先を選び、保存内容をデバッグツールで確認できる。

## Lv2

データの性質に応じて保存先を選び、データベースのスキーマ定義、読み書き、UIを妨げないスレッドでの処理を実装できる。秘密情報を安全な保存領域に分け、アプリの更新やデータ削除時の動作をテストで検証できる。

## Lv3

スキーマの移行、大量データや同時書き込み、キャッシュとサーバーデータの整合、バックアップ対象の選別を設計できる。データ破損、移行の失敗、性能低下を再現・分析し、永続化の方式を比較してレビューできる。

## Lv4

保存先の選択基準、永続化層の共通部品、スキーマ移行の自動テストを整備できる。他者の利用結果を基に、データ消失や移行不具合の減少を確認し、基準と部品を更新できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 例に沿って、表示テーマの切り替えなど1つの設定値を保存するアプリを作り、アプリを終了して再起動しても値が残ることを確認する | [Foundation（UserDefaults）](https://developer.apple.com/documentation/foundation)・[データストレージ（Android）](https://developer.android.com/training/data-storage)・[Expo ドキュメント](https://docs.expo.dev/) |
| Lv2 | 一覧と詳細の2画面を持つメモアプリを作り、メモをデータベースに保存して、アプリを終了しても内容が残ることを確認する。ログイン用のトークンは通常のデータと分けて安全な保存領域に保存する | [SwiftData](https://developer.apple.com/documentation/swiftdata)・[Room](https://developer.android.com/training/data-storage/room)・[Keychain Services](https://developer.apple.com/documentation/security/keychain-services)・[Keystore](https://developer.android.com/privacy-and-security/keystore)・[Expo ドキュメント](https://docs.expo.dev/) |
| Lv3 | メモアプリに項目を追加するスキーマ変更を行い、旧バージョンで保存したデータが新バージョンで読めることをテストで確認する。数千件のデータで一覧表示と書き込みの速度を測り、サーバーから取得したデータのキャッシュを更新する方針を決める | [Core Data](https://developer.apple.com/documentation/coredata)・[Room](https://developer.android.com/training/data-storage/room)・[データストレージ（Android）](https://developer.android.com/training/data-storage) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 設定値の保存 | UserDefaults／@AppStorage | SharedPreferences、DataStore | AsyncStorage、MMKV |
| 構造化データの保存 | Core Data、SwiftData、SQLite（GRDB）、Realm | Room、SQLite | expo-sqlite |
| ファイルの保存 | FileManager | 内部・外部ストレージ | expo-file-system |
| 秘密情報の保存 | Keychain | Keystore、EncryptedSharedPreferences | expo-secure-store |
| クラウドとの同期 | CloudKit | Firebase（Firestore）など | Firebase（Firestore）など |

roadmap.sh で学ぶ：[iOS](https://roadmap.sh/ios)（Data Persistence、User Defaults、Keychain、Core Data、SQLite、File System）／[SwiftUI](https://roadmap.sh/swift-ui)（Data Persistence、SwiftData、Databases、Realm、GRDB、CloudKit）／[Android](https://roadmap.sh/android)（Storage、Shared Preferences、DataStore、Room Database、File System）／[React Native](https://roadmap.sh/react-native)（Storage、Async Storage、Expo Secure Store、Expo SQLite、Expo File System）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
