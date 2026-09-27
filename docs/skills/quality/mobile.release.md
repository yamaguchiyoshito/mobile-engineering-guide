---
title: "署名・配布・ストア公開"
description: "署名・配布・ストア公開の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# 署名・配布・ストア公開

**スキルID：** `mobile.release`  
**スキル領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** ビルドと依存管理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | 証明書・プロビジョニングプロファイル、App Store Connect、TestFlight、App Review Guidelines、段階的リリース、プライバシーマニフェスト、ASO |
| Android | アプリ署名（Play App Signing）、AAB、Play Console（内部テスト・クローズド・オープン・段階的公開）、データセーフティ、Firebase App Distribution |
| React Native | EAS Build／Submit／Update、OTA 更新の制約、ストア公開手順 |

roadmap.sh の参照トピック：ios: app-store-distribution, testflight, app-store-optimization-aso / android: distribution, google-playstore, firebase-distribution, signed-apk / react-native: publishing-apps, apple-app-store, google-play-store

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
