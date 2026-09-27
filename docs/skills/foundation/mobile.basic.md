---
title: "モバイルプラットフォーム基礎"
description: "モバイルプラットフォーム基礎の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# モバイルプラットフォーム基礎

**要素技術ID：** `mobile.basic`  
**技術領域：** [基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**評価対象：** OS構成、アプリライフサイクル、サンドボックス、権限、配布形態

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

スマートフォンのOSの上でアプリがどのように動き、どのような制約を受けるかを理解するための基礎知識です。Webアプリはブラウザがサーバーから読み込んで表示しますが、モバイルアプリは端末にインストールされて動き、起動・前面・背面・終了といった状態の移り変わり（ライフサイクル）をOSが管理し、メモリが足りなくなれば背面のアプリを予告なく終了させます。さらに、カメラや位置情報などを使うには、利用者の許可（権限）をOS経由で得る必要があります。アプリはApp StoreやGoogle Playなどのストアの審査を経て配布されるため修正版もすぐには利用者に届かず、通信が常につながっている前提も置けません。最初に押さえるのは、アプリがいつ止められても状態を失わないようにするライフサイクルの考え方と、アプリは自分専用の保存領域（サンドボックス）の外にOSの許可なくアクセスできないという原則です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式チュートリアルに沿って新規アプリを作り、起動、背面への移行、前面への復帰のたびにログを出力して、ライフサイクルの各状態で処理が呼ばれる順序を確認する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Activity入門](https://developer.android.com/guide/components/activities/intro-activities)・[はじめに（React Native）](https://reactnative.dev/docs/getting-started) |
| Lv2 | カメラまたは位置情報を使う1画面のアプリを作り、権限を許可した場合と拒否した場合のそれぞれの表示を実装する。入力途中でアプリを背面に移してから戻しても、入力内容が残っていることを端末上で確認する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Activity入門](https://developer.android.com/guide/components/activities/intro-activities)・[Expoドキュメント](https://docs.expo.dev/) |
| Lv3 | 既存のアプリで、背面にある間にプロセスが終了された後の復帰、画面回転などの構成変更、設定画面から権限を取り消した後の起動を再現し、状態が失われる箇所を一覧にして改善案を比べる。ストアの審査基準のうち権限とバックグラウンド実行に関わる項目を読み、設計への影響を整理する | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)・[Background Tasks](https://developer.apple.com/documentation/backgroundtasks)・[バックグラウンド処理](https://developer.android.com/develop/background-work)・[アプリの公開](https://developer.android.com/studio/publish) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| OSとアプリの構成 | Cocoa Touch層構成 | Activity・Service・BroadcastReceiver・ContentProvider | JSランタイムとネイティブ層の関係 |
| 状態の移り変わり（ライフサイクル） | アプリライフサイクル（UIApplication／SceneDelegate、SwiftUI App） | Activityライフサイクル | AppState |
| 構成と権限の宣言 | Info.plist | AndroidManifest | app.json（Expo）、各OSの設定ファイル |
| 権限の要求 | 権限ダイアログ | 実行時権限 | 各OSの権限ダイアログ（Expoの各SDK経由） |
| 保存領域の分離 | サンドボックス | アプリ専用ストレージ | 各OSのサンドボックス |
| 開発・配布の形態 | App Store、TestFlight、Ad Hoc | Google Play、APKの直接配布 | Expo Managed／Bare |

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（iOS Architecture、Core OS、Core Services、Cocoa Touch、File System）／[SwiftUI](https://roadmap.sh/swift-ui)（App Lifecycle）／[Android](https://roadmap.sh/android)（App Components、Activity Lifecycle、The Fundamentals、File System）／[React Native](https://roadmap.sh/react-native)（What Is React Native、Why Use React Native、Expo Tradeoffs、React Native Alternatives）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
