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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| React Native | Native Modules（Turbo Modules）、Platform モジュール、`.ios.js`／`.android.js`、権限（expo-permissions 相当）、Push 通知（expo-notifications、FCM／APNs）、ディープリンク（Linking）、react-native-web、Bare ワークフローでのネイティブ設定 |

roadmap.sh の参照トピック：react-native: using-native-modules, writing-platform-specific-code, platform-module, file-extensions, for-ios, for-android, permissions, push-notifications, deeplinking, react-native-web, expo-tradeoffs

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
