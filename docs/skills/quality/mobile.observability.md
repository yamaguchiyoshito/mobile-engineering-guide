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

## このスキルについて

公開したアプリで起きたクラッシュ（異常終了）、応答停止、エラーを利用者の端末から集めて分析し、原因の特定と修正につなげる技術です。モバイルアプリは利用者それぞれの端末の上で動くため、クラッシュもその端末の中で起こり、サーバーのログだけでは何が起きたかは分かりません。そこで、端末から報告を送る収集サービス（CrashlyticsやSentryなど）を組み込みます。配布用ビルドではクラッシュ位置が読めない形になっているため、ソースコードの関数名や行番号に対応付ける処理（シンボル化）に必要な情報もアップロードしておきます。最初に押さえるのは、スタックトレース（クラッシュ時に実行中だった処理の履歴）の読み方と、発生したアプリのバージョン・端末・OSを合わせて確認する習慣です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿ってサンプルアプリにクラッシュ報告の収集を組み込み、テスト用のクラッシュを発生させて、管理画面でスタックトレース、アプリのバージョン、端末を確認して記録する | [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics) |
| Lv2 | 自分のアプリの配布用ビルドでdSYM、ProGuard mapping、ソースマップなどのシンボル情報のアップロードを設定し、読める形になったスタックトレースから原因を特定して修正する。あわせて、個人情報を含めないログの出力規則を決めてアプリに適用する | [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics)・[OSLog](https://developer.apple.com/documentation/os/logging) |
| Lv3 | 既存アプリのクラッシュ率と応答停止をバージョン、端末、OSごとに集計し、影響の大きい順に対応の優先順位を決める。アプリ側の例外とサーバー側の障害を切り分ける手順と、遠隔設定で問題のある機能を止める方法を設計する | [MetricKit](https://developer.apple.com/documentation/metrickit)・[Android vitals](https://developer.android.com/topic/performance/vitals)・[Firebase Crashlytics](https://firebase.google.com/docs/crashlytics) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| クラッシュ報告の収集 | Crashlytics | Crashlytics | Sentry／Crashlytics、JS例外とネイティブクラッシュの区別 |
| シンボル化（クラッシュ位置をソースに対応付ける） | dSYMのシンボル化 | ProGuard mappingのアップロード | ソースマップのアップロード |
| 応答停止・性能などの指標 | Xcode Organizer（クラッシュ・Hang・エネルギー）、MetricKit | Android vitals | 各OSの仕組み（MetricKit、Android vitals） |
| ログの出力 | OSLog／swift-log | Timber、Logcat | console、react-native-logs |
| 機能の遠隔制御 | Remote Config（Firebase） | Remote Config | Remote Config（Firebase） |

roadmap.shで学ぶ：[SwiftUI](https://roadmap.sh/swift-ui)（Logging & Debugging、Swift Log、CocoaLumberjack）／[Android](https://roadmap.sh/android)（Crashlytics、Timber、Remote Config、Chucker）／[React Native](https://roadmap.sh/react-native)（Sourcemaps、LogBox）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
