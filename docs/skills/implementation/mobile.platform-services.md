---
title: "プラットフォーム機能連携"
description: "プラットフォーム機能連携の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# プラットフォーム機能連携

**スキルID：** `mobile.platform-services`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** モバイル基礎、並行処理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

通知、位置情報、カメラ、バックグラウンド処理などのOS機能と権限の関係を説明できず、利用に手順ごとの指示が必要である。

## Lv1

手順書と例に沿って権限を要求し、通知の受信や位置情報・カメラの利用を限定された範囲で実装できる。指定された端末で動作を確認できる。

## Lv2

要件が明確な機能について、権限の拒否や取り消し、前面と背面での実行の違いを考慮してOS機能を実装できる。実機で通知、バックグラウンド処理、アプリ内課金などの動作を検証し、通常の不具合を修正できる。

## Lv3

OSごとのバックグラウンド実行の制限、電池消費、プライバシー要件、ストア審査の規定を踏まえて機能を設計できる。端末やOS版による挙動の差を分析し、代替手段を比較して他者の実装をレビューできる。

## Lv4

OS機能の利用方針、権限要求の共通処理、実機・OS版ごとの検証手順を整備できる。他者の利用を支援し、権限や通知に関する不具合、審査での指摘の減少を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | プッシュ通知（APNs、UserNotifications）、Background Tasks、MapKit、AVFoundation、HealthKit、ARKit、Core ML、In-App Purchase（StoreKit） |
| Android | Firebase Cloud Messaging、WorkManager、Service／BroadcastReceiver、ContentProvider、Google Maps、Play Services、Play Billing |
| React Native | expo-notifications、expo-location、expo-camera、react-native-maps、バックグラウンド処理の制約 |

roadmap.sh の参照トピック：ios: media, mapkit, avfoundation, core-audio, core-image, core-graphics, core-ml, metal, healthkit, arkit, gamekit, lottie / android: cloud-messaging, workmanager, services, broadcast-receiver, content-provider, common-services, google-maps, google-play-services, google-admob, firestore, firebase / react-native: push-notifications, permissions / swift-ui: background

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
