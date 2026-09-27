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

## このスキルについて

通信やデータベースへのアクセスのように時間のかかる処理を、画面の操作を止めずに実行するための Kotlin の仕組み（コルーチン）と、時間とともに変わる値を流れとして扱う仕組み（Flow）を扱うスキルです。Android ではメインスレッドを長く止めると、OS が「アプリが応答していません」という表示（ANR）を出します。また、画面は回転や切り替えのたびに作り直されるため、実行中の処理を画面の寿命に合わせて止める必要があります。最初に押さえるのは、途中で一時停止できる関数（suspend 関数）と、処理の寿命を決めるスコープの考え方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式コースやガイドの例に沿って、ボタンを押すと数秒待ってから結果を表示するアプリを作り、ログで実行スレッドと処理の完了順序を確認する | [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)・[Kotlin コルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html) |
| Lv2 | ViewModel から StateFlow で「読み込み中・成功・失敗」の状態を公開し、画面で収集して表示する一覧画面を作る。2つの API を並列に呼んで結果をまとめる処理を加え、テスト用ディスパッチャを使ったテストで結果を確認する | [Kotlin コルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[テスト](https://developer.android.com/training/testing) |
| Lv3 | 検索欄の入力を Flow で受け取り、入力が止まってから検索する処理にタイムアウトと再試行を加える。画面が非表示の間は収集を止めることを確認し、既存コードのスコープの使い方を見直してキャンセル漏れを洗い出す | [Kotlin コルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Android vitals](https://developer.android.com/topic/performance/vitals) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 非同期処理の記述 | コルーチン（suspend、CoroutineScope、Dispatchers、structured concurrency） |
| 値の流れ | Flow／StateFlow／SharedFlow |
| ライフサイクルとの連携 | lifecycleScope／viewModelScope |
| 中断とエラー | キャンセルと例外 |
| 従来のスレッド処理 | Thread／Handler |

roadmap.sh で学ぶ：[Android](https://roadmap.sh/android)（Threads、Coroutines、Flow、Asynchronism）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
