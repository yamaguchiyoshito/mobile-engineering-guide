---
title: "Kotlinコルーチン・Flow"
description: "Kotlinコルーチン・Flowの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# Kotlinコルーチン・Flow

**要素技術ID：** `kotlin.coroutines`  
**技術領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** Android  
**主な前提：** Kotlin

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

通信やデータベースへのアクセスのように時間のかかる処理を、画面の操作を止めずに実行するためのKotlinの仕組み（コルーチン）と、時間とともに変わる値を流れとして扱う仕組み（Flow）を扱う技術です。Androidではメインスレッドを長く止めると、OSが「アプリが応答していません」という表示（ANR）を出します。また、画面は回転や切り替えのたびに作り直されるため、実行中の処理を画面の寿命に合わせて止める必要があります。最初に押さえるのは、途中で一時停止できる関数（suspend関数）と、処理の寿命を決めるスコープの考え方です。

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
| Lv1 | 公式コースやガイドの例に沿って、ボタンを押すと数秒待ってから結果を表示するアプリを作り、ログで実行スレッドと処理の完了順序を確認する | [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html) |
| Lv2 | ViewModelからStateFlowで「読み込み中・成功・失敗」の状態を公開し、画面で収集して表示する一覧画面を作る。2つのAPIを並列に呼んで結果をまとめる処理を加え、テスト用ディスパッチャを使ったテストで結果を確認する | [Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[テスト](https://developer.android.com/training/testing) |
| Lv3 | 検索欄の入力をFlowで受け取り、入力が止まってから検索する処理にタイムアウトと再試行を加える。画面が非表示の間は収集を止めることを確認し、既存コードのスコープの使い方を見直してキャンセル漏れを洗い出す | [Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Android vitals](https://developer.android.com/topic/performance/vitals) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 非同期処理の記述 | コルーチン（suspend、CoroutineScope、Dispatchers、structured concurrency） |
| 値の流れ | Flow／StateFlow／SharedFlow |
| ライフサイクルとの連携 | lifecycleScope／viewModelScope |
| 中断とエラー | キャンセルと例外 |
| 従来のスレッド処理 | Thread／Handler |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="kotlin-coroutines-guide, kotlin-coroutine-context, kotlin-flow, kotlin-cancellation, kotlin-exception-handling, android-coroutines, android-flow, android-stateflow, android-lifecycle-coroutines, android-coroutines-best-practices, android-coroutines-test, android-handler" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Coroutines guide](https://kotlinlang.org/docs/coroutines-guide.html) | Android | コルーチンの主要な機能を章ごとに説明するKotlinのガイド |
| 公式リファレンス | [Coroutine context and dispatchers](https://kotlinlang.org/docs/coroutine-context-and-dispatchers.html) | Android | コルーチンの実行スレッドを決めるディスパッチャとコンテキスト |
| 公式リファレンス | [Asynchronous Flow](https://kotlinlang.org/docs/flow.html) | Android | 複数の値を非同期に順に返すFlowの作成、変換、収集の方法 |
| 公式リファレンス | [Cancellation and timeouts](https://kotlinlang.org/docs/cancellation-and-timeouts.html) | Android | コルーチンのキャンセルの仕組みとタイムアウトの指定方法 |
| 公式リファレンス | [Coroutine exceptions handling](https://kotlinlang.org/docs/exception-handling.html) | Android | コルーチンでの例外の伝播と、ハンドラによる処理の方法 |
| 公式リファレンス | [Handler](https://developer.android.com/reference/android/os/Handler) | Android | スレッドのメッセージキューへ処理やメッセージを送るクラス |
| 学習資料 | [Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines) | Android | Androidアプリでコルーチンを使い、メインスレッドを止めない方法 |
| 学習資料 | [Kotlin flows on Android](https://developer.android.com/kotlin/flow) | Android | AndroidでFlowを作成し、変換して画面で収集する方法 |
| 学習資料 | [StateFlow and SharedFlow](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow) | Android | 状態やイベントを公開するStateFlowとSharedFlowの使い方 |
| 学習資料 | [Use Kotlin coroutines with lifecycle-aware components](https://developer.android.com/topic/libraries/architecture/coroutines) | Android | lifecycleScopeなどで処理の寿命を画面の寿命に合わせる方法 |
| 学習資料 | [Best practices for coroutines in Android](https://developer.android.com/kotlin/coroutines/coroutines-best-practices) | Android | ディスパッチャの注入やスコープの選び方など実装上の指針 |
| 学習資料 | [Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test) | Android | テスト用ディスパッチャを使ってコルーチンの処理を検証する方法 |

<!-- references:end -->

roadmap.shで学ぶ：[Android](https://roadmap.sh/android)（Threads、Coroutines、Flow、Asynchronism）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
