---
title: "Swift並行処理とメモリ管理"
description: "Swift並行処理とメモリ管理の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# Swift並行処理とメモリ管理

**スキルID：** `swift.concurrency`  
**スキル領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** iOS  
**主な前提：** Swift

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

メインスレッドとバックグラウンド処理の違い、async/awaitの役割、参照カウントによるメモリ解放の仕組みを説明できず、非同期処理やクロージャのキャプチャを書くには手順ごとの指示が必要である。

## Lv1

例に沿ってasync関数を呼び出し、結果をメインスレッドで画面に反映できる。支援を受けてクロージャに弱参照のキャプチャを記述し、デバッガで実行スレッドやインスタンスの解放を確認できる。

## Lv2

逐次処理と並列処理をタスクで書き分け、キャンセルとエラーを扱ったうえでUI更新をメインアクターに限定できる。循環参照を避けるキャプチャを選び、データ競合の警告やメモリリークを検出して修正できる。

## Lv3

共有状態をactorで隔離し、構造化・非構造化タスクの寿命、キャンセルの伝播、コールバック型APIとの橋渡しを設計できる。データ競合や循環参照による不具合を再現・分析し、厳格な並行性検査への段階的な移行を他者とレビューできる。

## Lv4

並行処理とメモリ管理の共通方針、再利用できる非同期部品、厳格な検査設定やリーク検出を含む自動検証を整備できる。他者の利用結果を基に、並行処理に起因するクラッシュやリークと調査工数の改善を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | GCD（DispatchQueue）、OperationQueue、async／await、Task・TaskGroup、actor、MainActor、AsyncSequence、Strict Concurrency Checking、ARC、weak／unowned、循環参照 |

roadmap.sh の参照トピック：ios: concurrency, gcd, operation-queues, async--await, concurrency-and-multithreading, concurrency-gcd-asyncawait, memory-management, capturing-values--memory-mgmt, callbacks, callback-hell / swift-ui: actors, asynchronous-functions, asynchronous-sequences, tasks--task-groups, unstructured-concurrency, strict-concurrency-checking, arc, memory-safety, swiftui-with-asyncawait

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
