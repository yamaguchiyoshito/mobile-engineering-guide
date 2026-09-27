---
title: "監視・クラッシュ分析"
description: "監視・クラッシュ分析の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# 監視・クラッシュ分析

**要素技術ID：** `mobile.observability`  
**技術領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** API連携とデータフロー、署名・配布・ストア公開

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

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

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="firebase-crashlytics, crashlytics-ios-symbols, crashlytics-android-mapping, xcode-debug-symbols, xcode-shipping-performance, metrickit, android-vitals, oslog, swift-log, timber, android-logcat, sentry-react-native, sentry-rn-sourcemaps, react-native-logs, firebase-remote-config" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [デバッグ情報を含むビルド（iOS）](https://developer.apple.com/documentation/xcode/building-your-app-to-include-debugging-information) | iOS | デバッグとクラッシュ解析に使うdSYMなどのシンボル情報を生成する設定 |
| 公式リファレンス | [配信中アプリの性能分析（iOS）](https://developer.apple.com/documentation/xcode/analyzing-the-performance-of-your-shipping-app) | iOS | Xcode Organizerで配信中アプリの電力や性能の指標を確認する方法 |
| 公式リファレンス | [MetricKit](https://developer.apple.com/documentation/metrickit) | iOS | 利用者の端末で集めた性能指標や診断情報をアプリで受け取るフレームワーク |
| 公式リファレンス | [OSLog](https://developer.apple.com/documentation/os/logging) | iOS | 統合ログシステムにログを記録し、取得・閲覧するためのAPI |
| 公式リファレンス | [Android vitals](https://developer.android.com/google/play/vitals) | Android | Google Playが集計する起動時間・ANR・クラッシュなどの品質指標 |
| 公式リファレンス | [Logcatでログを表示する（Android）](https://developer.android.com/studio/debug/logcat) | Android | Android Studioでアプリのログを表示し絞り込む方法 |
| ライブラリ | [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics) | iOS・Android・React Native | アプリのクラッシュを収集し、原因ごとにまとめて表示するサービス |
| ライブラリ | [読めるクラッシュレポートの取得（iOS）](https://firebase.google.com/docs/crashlytics/ios/get-deobfuscated-reports) | iOS | dSYMを送りスタックトレースを読める形にする方法 |
| ライブラリ | [swift-log](https://github.com/apple/swift-log) | iOS | 出力先を差し替えられるSwift向けのログ出力API |
| ライブラリ | [Firebase Remote Config](https://firebase.google.com/docs/remote-config) | iOS・Android・React Native | アプリを更新せずに設定値を配信して機能の有効・無効を切り替えるサービス |
| ライブラリ | [読めるクラッシュレポートの取得（Android）](https://firebase.google.com/docs/crashlytics/android/get-deobfuscated-reports) | Android | Crashlyticsにmappingファイルを送り難読化を解除する方法 |
| ライブラリ | [Timber](https://github.com/JakeWharton/timber) | Android | 出力先を差し替えられるAndroid向けのログ出力ライブラリ |
| ライブラリ | [Sentry for React Native](https://docs.sentry.io/platforms/react-native/) | React Native | JavaScriptの例外とネイティブのクラッシュを収集して表示するサービス |
| ライブラリ | [ソースマップ（React Native）](https://docs.sentry.io/platforms/react-native/sourcemaps/) | React Native | ソースマップを送りJSの例外位置を元のコードに対応付ける方法 |
| ライブラリ | [react-native-logs](https://github.com/mowispace/react-native-logs) | React Native | ログの重要度と出力先を設定できるReact Native向けのログライブラリ |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
