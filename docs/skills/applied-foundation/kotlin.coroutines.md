---
title: "Kotlinコルーチン・Flow"
description: "Kotlinコルーチン・Flowの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# Kotlinコルーチン・Flow

**スキルID：** `kotlin.coroutines`  
**スキル領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** Android  
**主な前提：** Kotlin

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

スレッドとコルーチンの違い、サスペンド関数やFlowの役割を説明できず、メインスレッドを妨げない非同期処理を書くには手順ごとの指示が必要である。

## Lv1

例に沿ってスコープからコルーチンを起動し、サスペンド関数の結果を画面に反映できる。支援を受けてディスパッチャを指定し、ログで実行スレッドと完了順序を確認できる。

## Lv2

画面や状態保持クラスのライフサイクルに合ったスコープを選び、構造化された並行性に沿って逐次処理と並列処理を実装できる。Flowで状態を公開・収集し、キャンセルと例外を扱ったうえで、テストで結果を検証できる。

## Lv3

複数のFlowの結合、ホットとコールドの使い分け、再試行やタイムアウト、ライフサイクルに合わせた収集の停止を設計できる。コルーチンのリーク、キャンセル漏れ、例外の伝播による不具合を再現・分析し、他者の実装をレビューできる。

## Lv4

スコープとディスパッチャの注入方針、Flowの公開規約、テスト用ディスパッチャを使った検証手順を整備できる。他者の利用結果を基に、非同期処理に起因する不具合や応答停止と調査工数の改善を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| Android | Thread／Handler、コルーチン（suspend、CoroutineScope、Dispatchers、structured concurrency）、Flow／StateFlow／SharedFlow、lifecycleScope／viewModelScope、キャンセルと例外 |

roadmap.sh の参照トピック：android: threads, coroutines, flow, asynchronism, tasks--backstack

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
