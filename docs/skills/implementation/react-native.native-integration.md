---
title: "React Nativeのネイティブ連携"
description: "React Nativeのネイティブ連携の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# React Nativeのネイティブ連携

**スキルID：** `react-native.native-integration`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** React Native  
**主な前提：** React Native実装、SwiftまたはKotlinの基礎

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## このスキルについて

React Native のアプリは、画面や処理を書く JavaScript の層と、端末の機能を実際に動かす iOS／Android のネイティブの層に分かれています。通知、位置情報、ディープリンクのような OS の機能はネイティブの層を経由しないと使えず、権限の要求や設定ファイルの書き方も OS ごとに異なります。このスキルは、既存のライブラリで両者をつなぐことから、足りない機能を自分でネイティブモジュールとして作ることまでを扱います。最初に押さえるのは、JavaScript からネイティブの機能を呼び出す仕組みと、Platform モジュールや `.ios.js`／`.android.js` のファイル名で OS ごとにコードを分ける方法です。

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
| Lv1 | Expo の手順に沿って expo-notifications を導入し、通知の権限を要求してローカル通知を表示する。実機で権限を許可した場合と拒否した場合の動作を確認する | [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/)・[プラットフォーム固有コード](https://reactnative.dev/docs/platform-specific-code) |
| Lv2 | 通知をタップすると特定の詳細画面が開くアプリを作り、プッシュ通知の受信とディープリンク（Linking）を iOS と Android の両方で動かす。OS ごとに変更した設定ファイルと理由を記録する | [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/)・[Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)・[React Navigation](https://reactnavigation.org/docs/getting-started) |
| Lv3 | 既存ライブラリにない端末機能を1つ選んで Turbo Native Module として作り、引数と戻り値の型、エラー時の扱い、呼び出されるスレッドを定義する。Expo の管理下で続ける場合と Bare に移る場合を比較し、判断の根拠をまとめる | [Turbo Native Modules](https://reactnative.dev/docs/turbo-native-modules-introduction)・[Expo EAS](https://docs.expo.dev/eas/) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| ネイティブ機能の呼び出し | Native Modules（Turbo Modules） |
| OSごとのコードの分岐 | Platform モジュール、`.ios.js`／`.android.js` |
| 権限と通知 | 権限（expo-permissions 相当）、Push 通知（expo-notifications、FCM／APNs） |
| ディープリンク | Linking |
| ビルド方式と対象の拡張 | Bare ワークフローでのネイティブ設定、react-native-web |

roadmap.sh で学ぶ：[React Native](https://roadmap.sh/react-native)（Using native modules、Platform module、File extensions、Permissions、Push notifications、Deep linking、Expo tradeoffs）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
