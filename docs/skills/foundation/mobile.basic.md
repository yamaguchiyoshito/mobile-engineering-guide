---
title: "モバイルプラットフォーム基礎"
description: "モバイルプラットフォーム基礎の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# モバイルプラットフォーム基礎

**スキルID：** `mobile.basic`  
**スキル領域：** [基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**評価対象：** OS構成、アプリライフサイクル、サンドボックス、権限、配布形態

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

アプリのライフサイクル、サンドボックス、権限、配布形態の違いを説明できず、状態遷移や権限の扱いに手順ごとの指示が必要である。

## Lv1

手順書に沿ってアプリの設定ファイルに権限や構成を追加し、ライフサイクルの各状態で処理が呼ばれることをログで確認できる。バックグラウンド移行や権限拒否への対応には支援を求められる。

## Lv2

起動、前面、背面、終了の状態遷移に合わせて、リソースの取得と解放、画面状態の保存と復元を実装できる。権限の要求と拒否時の振る舞いを実装し、端末上で各状態を再現して確認できる。

## Lv3

プロセスの強制終了、構成変更、OSのバージョン差による権限やバックグラウンド実行の制約を含む不具合を分析し、原因を特定できる。サンドボックスや配布形態の制約を踏まえて設計案を比較し、他者の実装をレビューできる。

## Lv4

ライフサイクルと権限の扱いに関する実装方針、共通部品、確認手順、演習を整備できる。他者が利用した結果から、状態喪失や権限起因の不具合、審査での指摘の減少を確認し、仕組みを更新できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | アプリライフサイクル（UIApplication／SceneDelegate、SwiftUI App）、サンドボックス、Info.plist、権限ダイアログ、Cocoa Touch層構成 |
| Android | Activity・Service・BroadcastReceiver・ContentProvider、AndroidManifest、Activityライフサイクル、実行時権限 |
| React Native | JSランタイムとネイティブ層の関係、Expo Managed／Bare、AppState |

roadmap.sh の参照トピック：ios: ios-architecture, core-os, core-services, cocoa-touch, file-system / android: app-components, activity-lifecycle, the-fundamentals, file-system / react-native: what-is-react-native, why-use-react-native, expo-tradeoffs, react-native-alternatives / swift-ui: app-lifecycle

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
