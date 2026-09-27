---
title: "性能・メモリ・起動時間"
description: "性能・メモリ・起動時間の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# 性能・メモリ・起動時間

**要素技術ID：** `mobile.performance`  
**技術領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** 並行処理、UI実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

アプリが速く起動し、操作に遅れなく反応し、画面が滑らかに動き、メモリや電池を使いすぎないようにする技術です。モバイル端末はサーバーやパソコンに比べて処理能力、メモリ、電池が限られ、機種による性能差も大きく、メモリが不足するとOSがアプリを終了させることもあります。最初に押さえるのは、画面の描画と操作の受け付けを担うメインスレッド（UIスレッド）で重い処理をしないことと、改善の前後を同じ端末・同じ条件で計測して比べることです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

起動時間、描画、応答性、メモリ、電池消費の違いや主な低下要因を説明できず、計測と結果の読み取りに支援が必要である。

## Lv1

指定された端末とツールで起動時間、フレーム落ち、メモリ使用量を計測し、結果を記録できる。提示された改善方法を適用して同じ条件で再計測できる。

## Lv2

主要な画面と操作の指標と計測条件を定め、メインスレッドの重い処理、一覧表示、画像の読み込み、メモリリークなど通常のボトルネックを特定できる。リリース相当のビルドで改善前後を比較し、他機能への影響も確認できる。

## Lv3

実利用データと開発環境の計測を区別し、端末性能、OSバージョン、データ量、ネットワーク条件ごとの原因を分析できる。初期化の遅延、事前コンパイル、キャッシュ、描画の分割などの代替案を比較し、メモリや電池消費との兼ね合いを踏まえて改善できる。

## Lv4

性能目標、計測条件、自動ベンチマーク、性能予算、実利用データの監視と悪化時の対応手順を整備できる。開発・リリース工程に組み込み、起動時間や応答停止率で劣化の再発が減ったことを確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントの手順に沿って、自分のアプリの起動時間とメモリ使用量をプロファイラで計測して記録する。画像を縮小して読み込むなどの改善を1つ適用し、同じ端末・同じ条件で再計測する | [アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[パフォーマンス（Android）](https://developer.android.com/topic/performance)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |
| Lv2 | 画像付きの項目を数百件表示する一覧画面を作り、スクロール中のフレーム落ちとメモリ使用量をリリース相当のビルドで計測する。画像の読み込みと表示部品の再利用を改善し、改善前後の数値と他の画面への影響を記録する | [アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[パフォーマンス（Android）](https://developer.android.com/topic/performance)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |
| Lv3 | 既存アプリの起動処理を分析し、初期化の遅延、事前コンパイル、キャッシュなどの改善案をメモリや電池消費への影響と合わせて比較する。性能の異なる端末とデータ量で計測し、実利用データと開発環境での計測結果の違いを説明する | [MetricKit](https://developer.apple.com/documentation/metrickit)・[Android vitals](https://developer.android.com/topic/performance/vitals)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 処理時間の計測 | Instruments（Time Profiler） | Android Profiler | Flipper／DevToolsのプロファイラ |
| メモリとリークの調査 | Instruments（Allocations、Leaks）、メモリリーク（循環参照） | LeakCanary | Hermesのヒープ計測、各OSのプロファイラ |
| 起動時間の短縮 | 起動時間 | Baseline Profile | Hermes、RAM Bundle／inline require |
| 描画と応答性 | Hang検出 | Jetpack Benchmark／Macrobenchmark | FlatList最適化、JSスレッドとUIスレッド |
| 実利用データの監視 | MetricKit | Android vitals（起動時間、ANR、ジャンク） | 各OSの仕組み（MetricKit、Android vitals） |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="xcode-improving-performance, xcode-memory-use, swift-arc, xcode-launch-time, xcode-hangs, metrickit, android-profiler, leakcanary, baseline-profiles, android-benchmarking, android-vitals, rn-hermes, rn-flatlist-optimization, rn-js-loading, rn-devtools" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [自動参照カウント（Swift）](https://docs.swift.org/latest/documentation/the-swift-programming-language/automaticreferencecounting/) | iOS | ARCの仕組みと、強参照の循環を弱参照などで解消する方法の解説 |
| 公式リファレンス | [起動時間の短縮（iOS）](https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time) | iOS | 起動処理にかかる時間を計測して短縮する方法の解説 |
| 公式リファレンス | [Hangの理解（iOS）](https://developer.apple.com/documentation/xcode/understanding-hangs-in-your-app) | iOS | メインスレッドの処理を調べて操作への応答の遅れの原因を特定する方法 |
| 公式リファレンス | [MetricKit](https://developer.apple.com/documentation/metrickit) | iOS | 利用者の端末で集めた性能指標や診断情報をアプリで受け取るフレームワーク |
| 公式リファレンス | [アプリ性能のプロファイリング（Android）](https://developer.android.com/studio/profile) | Android | プロファイラでCPUやメモリの使用状況を調べる方法 |
| 公式リファレンス | [Baseline Profile（Android）](https://developer.android.com/topic/performance/baselineprofiles/overview) | Android | 事前コンパイルするコード経路を指定して起動や描画を速くする仕組み |
| 公式リファレンス | [ベンチマーク（Android）](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview) | Android | Benchmarkライブラリで処理時間や起動時間を計測する方法 |
| 公式リファレンス | [Android vitals](https://developer.android.com/google/play/vitals) | Android | Google Playが集計する起動時間・ANR・クラッシュなどの品質指標 |
| 公式リファレンス | [Hermes](https://reactnative.dev/docs/hermes) | React Native | React Native向けに最適化されたJavaScriptエンジン |
| 公式リファレンス | [FlatListの最適化（React Native）](https://reactnative.dev/docs/optimizing-flatlist-configuration) | React Native | FlatListの設定を調整して長い一覧の描画とメモリ使用を改善する方法 |
| 公式リファレンス | [JavaScript読み込みの最適化（React Native）](https://reactnative.dev/docs/optimizing-javascript-loading) | React Native | inline requireなどでJSの読み込みを速くする方法 |
| 公式リファレンス | [React Native DevTools](https://reactnative.dev/docs/react-native-devtools) | React Native | コンポーネント構造の検査やJSのデバッグを行うツール |
| ライブラリ | [LeakCanary](https://square.github.io/leakcanary/) | Android | Androidアプリのメモリリークを検出して原因の参照経路を示すライブラリ |
| 学習資料 | [アプリ性能の改善（iOS）](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance) | iOS | 性能の計測・分析・改善を繰り返してアプリの性能を上げる進め方 |
| 学習資料 | [Gathering information about memory use](https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use) | iOS | メモリグラフなどでアプリのメモリ使用量とリークを調べる方法 |

<!-- references:end -->

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（Profiling Instruments）／[SwiftUI](https://roadmap.sh/swift-ui)（Logging & Debugging）／[Android](https://roadmap.sh/android)（Leak Canary、Jetpack Benchmark、Chucker）／[React Native](https://roadmap.sh/react-native)（Performance、Profiling、Optimizing FlatList Config、RAM Bundles & Inline Requires、Understand Frame Rates）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
