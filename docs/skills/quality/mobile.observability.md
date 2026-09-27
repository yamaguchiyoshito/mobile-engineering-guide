---
title: "監視・クラッシュ分析"
description: "監視・クラッシュ分析の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# 監視・クラッシュ分析

**スキルID：** `mobile.observability`  
**スキル領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** API連携とデータフロー、署名・配布・ストア公開

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

クラッシュ、応答停止、エラーログ、利用状況の指標の違いを説明できず、報告の確認や再現に手順ごとの指示が必要である。

## Lv1

用意された管理画面でクラッシュ報告とスタックトレースを確認し、発生したバージョンと端末を記録できる。原因箇所の特定と再現には支援が必要である。

## Lv2

クラッシュ報告の送信とシンボル情報のアップロードを設定し、読める形になったスタックトレースから原因を特定して修正できる。ログのレベルと出力内容を決め、個人情報を含めずに調査に必要な情報を記録できる。

## Lv3

クラッシュ率、応答停止、通信エラー、性能指標をバージョン、端末、OSごとに分析し、影響範囲から対応の優先順位を決められる。アプリ内の層ごとの例外とサーバー側の障害を切り分け、機能の段階的な有効化や遠隔設定で影響を抑える方法を設計できる。

## Lv4

監視項目、通知の閾値、ログ規約、シンボル情報の管理、障害時の対応手順を整備し、チームで運用できる。運用実績を基に、クラッシュ率、検知から修正版の公開までの時間、再発件数が改善したことを確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | Crashlytics、Xcode Organizer（クラッシュ・Hang・エネルギー）、MetricKit、OSLog／swift-log、dSYM のシンボル化 |
| Android | Crashlytics、Android vitals、Timber、Logcat、Remote Config、ProGuard mapping のアップロード |
| React Native | Sentry／Crashlytics、ソースマップのアップロード、JS 例外とネイティブクラッシュの区別 |

roadmap.sh の参照トピック：android: crashlytics, timber, remote-config, chucker / swift-ui: logging--debugging, swift-log, cocoalumberjack / react-native: sourcemaps, logbox

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
