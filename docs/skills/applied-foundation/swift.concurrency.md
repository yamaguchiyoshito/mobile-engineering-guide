---
title: "Swift並行処理とメモリ管理"
description: "Swift並行処理とメモリ管理の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# Swift並行処理とメモリ管理

**要素技術ID：** `swift.concurrency`  
**技術領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** iOS  
**主な前提：** Swift

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

通信やファイルの読み込みのように時間のかかる処理を、画面の操作を止めずに実行する方法と、使い終わったデータをメモリから正しく片付ける仕組みを扱う技術です。モバイル端末はメモリが限られており、使用量が増えすぎるとOSがアプリを終了させることがあります。また、画面の描画を担うメインスレッドが止まるとアプリが固まったように見えるため、処理の実行場所とメモリの解放は利用者の体験に直結します。最初に押さえるのは、画面の更新はメインスレッドで行うという原則と、Swiftが参照の数を数えて不要になったデータを解放する仕組み（ARC）です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 例に沿って、ボタンを押すとasync関数で数秒待ってから結果を画面に表示するサンプルを作り、デバッガで画面の更新がメインスレッドで行われていることを確認する | [Swift言語ガイド](https://docs.swift.org/swift-book/)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency) |
| Lv2 | 複数の画像を並列にダウンロードして一覧に表示する画面を作り、画面を閉じたときにダウンロードがキャンセルされること、画面のインスタンスが解放されることをXcodeのメモリグラフで確認する | [Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[Xcode](https://developer.apple.com/documentation/xcode) |
| Lv3 | コールバック型の既存APIをasync／awaitで呼べるように包み、複数の画面から使うキャッシュをactorで保護する。既存コードで厳格な並行性検査を有効にし、出た警告を分類して段階的な移行計画を立てる | [Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 非同期処理の記述 | async／await、Task・TaskGroup、AsyncSequence |
| 共有状態の保護 | actor、MainActor、Strict Concurrency Checking |
| 従来の並行処理 | GCD（DispatchQueue）、OperationQueue |
| メモリ管理 | ARC、weak／unowned、循環参照 |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="swift-concurrency, swift-book-concurrency, swift-book-arc, swift-task, swift-taskgroup, swift-asyncsequence, swift-actor, swift-mainactor, swift-6-migration, dispatchqueue, operationqueue, xcode-memory-use" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency) | iOS | async/await、Task、actorなど並行処理のAPIをまとめたページ |
| 公式リファレンス | [Concurrency（The Swift Programming Language）](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) | iOS | 非同期関数、タスク、actorの書き方を説明する言語ガイドの章 |
| 公式リファレンス | [Automatic Reference Counting（The Swift Programming Language）](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/) | iOS | ARCの仕組みとweak・unownedによる循環参照の回避を説明する章 |
| 公式リファレンス | [Task](https://developer.apple.com/documentation/swift/task) | iOS | 非同期処理の単位を作成し、キャンセルや結果の取得を行う型 |
| 公式リファレンス | [TaskGroup](https://developer.apple.com/documentation/swift/taskgroup) | iOS | 動的な数の子タスクを並列に実行して結果を集める型 |
| 公式リファレンス | [AsyncSequence](https://developer.apple.com/documentation/swift/asyncsequence) | iOS | 非同期に届く値をfor-await-inで順に取り出すためのプロトコル |
| 公式リファレンス | [Actor](https://developer.apple.com/documentation/swift/actor) | iOS | 共有状態へのアクセスを直列化して保護するactor型のプロトコル |
| 公式リファレンス | [MainActor](https://developer.apple.com/documentation/swift/mainactor) | iOS | 処理をメインスレッドで実行させるグローバルアクター |
| 公式リファレンス | [DispatchQueue](https://developer.apple.com/documentation/dispatch/dispatchqueue) | iOS | GCDで処理をキューに入れてメインや別スレッドで実行する型 |
| 公式リファレンス | [OperationQueue](https://developer.apple.com/documentation/foundation/operationqueue) | iOS | Operationの実行順序、依存関係、同時実行数を管理するキュー |
| 学習資料 | [Migrating to Swift 6](https://www.swift.org/migration/documentation/migrationguide/) | iOS | 厳格な並行性検査を段階的に有効にしていく移行手順のガイド |
| 学習資料 | [Gathering information about memory use](https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use) | iOS | メモリグラフなどでアプリのメモリ使用量とリークを調べる方法 |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
