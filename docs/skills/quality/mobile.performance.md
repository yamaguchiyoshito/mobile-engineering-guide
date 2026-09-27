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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | Instruments（Time Profiler、Allocations、Leaks）、MetricKit、起動時間、Hang 検出、メモリリーク（循環参照） |
| Android | Android Profiler、LeakCanary、Jetpack Benchmark／Macrobenchmark、Baseline Profile、Android vitals（起動時間、ANR、ジャンク） |
| React Native | Hermes、FlatList 最適化、RAM Bundle／inline require、Flipper／DevTools のプロファイラ、JS スレッドと UI スレッド |

roadmap.sh の参照トピック：ios: profiling-instruments / android: leak-canary, jetpack-benchmark, chucker / swift-ui: logging--debugging / react-native: performance, profiling, optimizing-flatlist-config, ram-bundles--inline-requires, common-problem-sources, understand-frame-rates

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
