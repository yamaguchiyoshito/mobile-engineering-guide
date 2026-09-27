---
title: "性能・メモリ・起動時間"
description: "性能・メモリ・起動時間の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# 性能・メモリ・起動時間

**スキルID：** `mobile.performance`  
**スキル領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** 並行処理、UI実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## このスキルについて

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

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（Profiling Instruments）／[SwiftUI](https://roadmap.sh/swift-ui)（Logging & Debugging）／[Android](https://roadmap.sh/android)（Leak Canary、Jetpack Benchmark、Chucker）／[React Native](https://roadmap.sh/react-native)（Performance、Profiling、Optimizing FlatList Config、RAM Bundles & Inline Requires、Understand Frame Rates）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
