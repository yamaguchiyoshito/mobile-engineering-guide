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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | UserDefaults／@AppStorage、Keychain、FileManager、Core Data、SwiftData、SQLite（GRDB）、Realm、CloudKit |
| Android | SharedPreferences、DataStore、Room、SQLite、内部・外部ストレージ |
| React Native | AsyncStorage、expo-secure-store、expo-sqlite、expo-file-system、MMKV |

roadmap.sh の参照トピック：ios: data-persistence, user-defaults, keychain, core-data, sqlite, file-system, preferences / swift-ui: data-persistence, userdefaults-appstorage, filemanager, core-data, swiftdata, databases, realm, grdb, cloudkit / android: storage, shared-preferences, datastore, room-database, file-system / react-native: storage, react-native-async-storage, expo-secure-store, expo-sqlite, expo-file-system, other-storage-options

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
