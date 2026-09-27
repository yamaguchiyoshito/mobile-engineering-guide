---
title: "署名・配布・ストア公開"
description: "署名・配布・ストア公開の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# 署名・配布・ストア公開

**要素技術ID：** `mobile.release`  
**技術領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** ビルドと依存管理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

作ったアプリを利用者の端末に届けるために、署名、テスト配信、ストアへの提出と審査、公開までを行う技術です。サーバーにデプロイすれば全員に反映されるWebと違い、モバイルアプリは開発者の署名を付けた配布用ビルドをApp StoreやGoogle Playの審査に通し、段階的に公開した後、利用者が端末上でアップデートして初めて新しい版が動きます。そのため公開後すぐに全員へ届くわけではなく、しばらくは旧版を使い続ける利用者が残り、不具合が見つかっても配布済みの版を即座に取り消すことはできません。最初に押さえるのは、署名が「誰が作ったアプリか」を証明する仕組みであることと、公開する利用者の割合を少しずつ広げる段階的公開の考え方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

署名、配布用ビルド、テスト配信、ストア審査、公開の違いを説明できず、配布作業の各段階に手順ごとの指示が必要である。

## Lv1

手順書と用意された署名情報を使って配布用ビルドを作成し、テスト配信へアップロードできる。署名エラーや審査の指摘への対応には支援が必要である。

## Lv2

バージョン番号とビルド番号、署名設定、ストア掲載情報、プライバシーに関する申告を準備し、テスト配信から公開まで完了できる。審査基準との適合を事前に確認し、指摘を受けた場合は原因を特定して再提出できる。

## Lv3

段階的公開、テスト対象者の区分、強制更新、配布済みバージョンとの互換性を含むリリース計画を設計できる。審査の遅延、公開後の不具合による配信停止、ストアを経由しない更新の制約などのリスクを比較し、判断の根拠を関係者に説明できる。

## Lv4

署名情報の管理、リリース手順の自動化、公開判定の確認項目、ロールバック方針を整備し、特定の担当者に依存しない体制にできる。他者によるリリース実績を基に、所要時間、審査での差し戻し、公開後の障害対応が改善したことを確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿って自分のアプリの配布用ビルドを作成し、TestFlightまたはGoogle Playの内部テストにアップロードして、自分の端末にインストールできることを確認する | [TestFlight](https://developer.apple.com/testflight/)・[アプリの公開](https://developer.android.com/studio/publish)・[Expo EAS](https://docs.expo.dev/eas/) |
| Lv2 | 小さなアプリについて、バージョン番号とビルド番号の更新、署名設定、スクリーンショットと説明文、プライバシーに関する申告を準備し、審査ガイドラインとの適合を確認したうえでストアへの提出から公開まで完了する | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)・[App Store Connectヘルプ](https://developer.apple.com/help/app-store-connect/)・[アプリの公開](https://developer.android.com/studio/publish)・[アプリ署名](https://developer.android.com/studio/publish/app-signing)・[App Storeへの公開](https://reactnative.dev/docs/publishing-to-app-store)・[署名付きAPK](https://reactnative.dev/docs/signed-apk-android) |
| Lv3 | 既存アプリの次回リリースについて、段階的公開の割合と期間、テスト対象者の区分、旧版とAPIの互換性、強制更新の条件、公開後に不具合が見つかった場合の配信停止の手順を含むリリース計画を作り、関係者に説明する | [App Store Connectヘルプ](https://developer.apple.com/help/app-store-connect/)・[アプリの公開](https://developer.android.com/studio/publish)・[Expo EAS](https://docs.expo.dev/eas/) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 署名と配布用ビルド | 証明書・プロビジョニングプロファイル | アプリ署名（Play App Signing）、AAB | EAS Build |
| テスト配信 | TestFlight | Play Console（内部テスト・クローズド・オープン）、Firebase App Distribution | EAS Buildの内部配布、各ストアのテスト配信 |
| ストア掲載と審査 | App Store Connect、App Review Guidelines、プライバシーマニフェスト、ASO | Play Console、データセーフティ | EAS Submit、ストア公開手順 |
| 段階的な公開と更新 | 段階的リリース | Play Consoleの段階的公開 | EAS Update、OTA更新の制約 |

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（App Store Distribution、TestFlight、App Store Optimization (ASO)）／[Android](https://roadmap.sh/android)（Distribution、Google Play Store、Firebase Distribution、Signed APK）／[React Native](https://roadmap.sh/react-native)（Publishing Apps、Apple App Store、Google Play Store）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
