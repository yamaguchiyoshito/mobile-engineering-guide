---
title: "プラットフォーム機能連携"
description: "プラットフォーム機能連携の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# プラットフォーム機能連携

**要素技術ID：** `mobile.platform-services`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** モバイル基礎、並行処理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

通知、位置情報、カメラ、地図、バックグラウンドでの処理、アプリ内課金など、OSや端末が提供する機能をアプリから使う技術です。これらの機能は利用者のプライバシーや電池に関わるためOSが権限を管理しており、利用者はいつでも許可を拒否したり取り消したりできます。また、アプリが画面に表示されていない間（背面）に動ける処理はOSごとに厳しく制限され、ストアの審査でも使い方が確認されます。最初に押さえるのは、権限を要求して結果に応じて処理を分ける流れと、アプリが前面にあるときと背面にあるときで使える機能が違うことです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 手順書に沿って通知の権限を要求し、ボタンを押すと数秒後にローカル通知が届くアプリを作る。実機で権限を許可した場合と拒否した場合の両方を確認する | [User Notifications](https://developer.apple.com/documentation/usernotifications)・[Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) |
| Lv2 | プッシュ通知を受け取り、通知をタップすると関連する画面を開くアプリを作る。定期的なデータ更新をバックグラウンド処理として登録し、権限を拒否・取り消したときの表示も実装して実機で確認する | [User Notifications](https://developer.apple.com/documentation/usernotifications)・[Background Tasks](https://developer.apple.com/documentation/backgroundtasks)・[Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)・[バックグラウンド処理](https://developer.android.com/develop/background-work)・[Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) |
| Lv3 | 既存アプリのバックグラウンド処理と位置情報の利用を洗い出し、OSごとの実行制限と電池消費を踏まえて代替手段を比較する。ストアの審査ガイドラインの該当項目を確認し、権限を求める理由の説明文を見直す | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)・[Background Tasks](https://developer.apple.com/documentation/backgroundtasks)・[バックグラウンド処理](https://developer.android.com/develop/background-work)・[Android vitals](https://developer.android.com/topic/performance/vitals) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 通知 | プッシュ通知（APNs、UserNotifications） | Firebase Cloud Messaging | expo-notifications |
| バックグラウンド処理 | Background Tasks | WorkManager、Service／BroadcastReceiver | バックグラウンド処理の制約 |
| 位置情報と地図 | MapKit | Google Maps | expo-location、react-native-maps |
| カメラなどの端末機能と他アプリとの連携 | AVFoundation、HealthKit、ARKit、Core ML | ContentProvider、Play Services | expo-camera |
| アプリ内課金 | In-App Purchase（StoreKit） | Play Billing | expo-in-app-purchases、react-native-iap |

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（MapKit、AVFoundation、Core ML、HealthKit、ARKit）／[SwiftUI](https://roadmap.sh/swift-ui)（Background）／[Android](https://roadmap.sh/android)（Cloud messaging、WorkManager、Services、Broadcast receiver、Content provider、Google Maps、Google Play services）／[React Native](https://roadmap.sh/react-native)（Push notifications、Permissions）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
