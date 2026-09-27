---
title: "React Nativeのネイティブ連携"
description: "React Nativeのネイティブ連携の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# React Nativeのネイティブ連携

**要素技術ID：** `react-native.native-integration`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** React Native  
**主な前提：** React Native実装、SwiftまたはKotlinの基礎

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

React Nativeのアプリは、画面や処理を書くJavaScriptの層と、端末の機能を実際に動かすiOS／Androidのネイティブの層に分かれています。通知、位置情報、ディープリンクのようなOSの機能はネイティブの層を経由しないと使えず、権限の要求や設定ファイルの書き方もOSごとに異なります。この要素技術は、既存のライブラリで両者をつなぐことから、足りない機能を自分でネイティブモジュールとして作ることまでを扱います。最初に押さえるのは、JavaScriptからネイティブの機能を呼び出す仕組みと、Platformモジュールや`.ios.js`／`.android.js`のファイル名でOSごとにコードを分ける方法です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

JavaScript層とネイティブ層の役割分担、プラットフォーム別コードの仕組みを説明できず、ネイティブ機能の利用に手順ごとの指示が必要である。

## Lv1

手順書に沿って既存のネイティブ機能ライブラリを導入し、権限の要求、通知、ディープリンクを限定された範囲で動かせる。指定された端末で動作を確認できる。

## Lv2

プラットフォーム別の分岐やファイルを使い分け、権限、プッシュ通知、ディープリンクを要件どおりに実装できる。ネイティブ側の設定を変更し、iOSとAndroidの双方で動作を検証・修正できる。

## Lv3

既存ライブラリで不足する機能をネイティブモジュールとして設計し、型、スレッド、エラーの受け渡しを定義できる。ビルド方式や依存ライブラリの制約を比較して導入方針を判断し、他者の実装をレビューできる。

## Lv4

ネイティブモジュールの作成手順、ライブラリの採用基準、両プラットフォームでの自動ビルドと検証を整備できる。他者の利用を支援し、ネイティブ連携に起因する不具合や更新時の手戻りの減少を確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Expoの手順に沿ってexpo-notificationsを導入し、通知の権限を要求してローカル通知を表示する。実機で権限を許可した場合と拒否した場合の動作を確認する | [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/)・[プラットフォーム固有コード](https://reactnative.dev/docs/platform-specific-code) |
| Lv2 | 通知をタップすると特定の詳細画面が開くアプリを作り、プッシュ通知の受信とディープリンク（Linking）をiOSとAndroidの両方で動かす。OSごとに変更した設定ファイルと理由を記録する | [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/)・[Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)・[React Navigation](https://reactnavigation.org/docs/getting-started) |
| Lv3 | 既存ライブラリにない端末機能を1つ選んでTurbo Native Moduleとして作り、引数と戻り値の型、エラー時の扱い、呼び出されるスレッドを定義する。Expoの管理下で続ける場合とBareに移る場合を比較し、判断の根拠をまとめる | [Turbo Native Modules](https://reactnative.dev/docs/turbo-native-modules-introduction)・[Expo EAS](https://docs.expo.dev/eas/) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| ネイティブ機能の呼び出し | Native Modules（Turbo Modules） |
| OSごとのコードの分岐 | Platformモジュール、`.ios.js`／`.android.js` |
| 権限と通知 | 権限（expo-permissions相当）、Push通知（expo-notifications、FCM／APNs） |
| ディープリンク | Linking |
| ビルド方式と対象の拡張 | Bareワークフローでのネイティブ設定、react-native-web |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="rn-turbo-native-modules, rn-platform-specific-code, rn-platform, rn-permissionsandroid, expo-permissions, expo-notifications, firebase-cloud-messaging, apns-registering, rn-linking, expo-cng, expo-bare-overview, react-native-web" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) | 共通 | サーバーから端末へプッシュ通知やメッセージを送る仕組み |
| 公式リファレンス | [Registering your app with APNs](https://developer.apple.com/documentation/usernotifications/registering-your-app-with-apns) | iOS | APNsに端末を登録してプッシュ通知を受け取るための手順 |
| 公式リファレンス | [Turbo Native Modules](https://reactnative.dev/docs/turbo-native-modules-introduction) | React Native | 型定義に基づいてネイティブコードを呼び出すモジュールの作り方 |
| 公式リファレンス | [Platform-Specific Code（React Native）](https://reactnative.dev/docs/platform-specific-code) | React Native | OSごとに処理やスタイル、ファイルを切り替える方法 |
| 公式リファレンス | [Platform](https://reactnative.dev/docs/platform) | React Native | 実行中のOSの種類やバージョンを判定するためのモジュール |
| 公式リファレンス | [PermissionsAndroid](https://reactnative.dev/docs/permissionsandroid) | React Native | Androidの実行時権限を確認・要求するためのAPI |
| 公式リファレンス | [権限の扱い（React Native）](https://docs.expo.dev/guides/permissions/) | React Native | Expoアプリで各OSの権限を設定し要求する方法を説明 |
| 公式リファレンス | [Linking](https://reactnative.dev/docs/linking) | React Native | URLで他アプリやアプリ内の画面を開くためのAPI |
| 公式リファレンス | [Continuous Native Generation（React Native）](https://docs.expo.dev/workflow/continuous-native-generation/) | React Native | prebuildで設定からネイティブプロジェクトを生成する仕組み |
| ライブラリ | [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) | React Native | 通知の権限要求・受信・ローカル通知の表示を扱うライブラリ |
| ライブラリ | [Overview of using Expo with existing React Native apps](https://docs.expo.dev/bare/overview/) | React Native | ネイティブプロジェクトを直接管理するアプリでExpoを使う方法 |
| ライブラリ | [React Native for Web](https://github.com/necolas/react-native-web) | React Native | React Nativeの部品をWebブラウザで動かすライブラリ |

<!-- references:end -->

roadmap.shで学ぶ：[React Native](https://roadmap.sh/react-native)（Using native modules、Platform module、File extensions、Permissions、Push notifications、Deep linking、Expo tradeoffs）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
