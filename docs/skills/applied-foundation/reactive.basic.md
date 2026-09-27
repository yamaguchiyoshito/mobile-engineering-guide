---
title: "リアクティブプログラミング"
description: "リアクティブプログラミングの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# リアクティブプログラミング

**要素技術ID：** `reactive.basic`  
**技術領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** Swift並行処理またはKotlinコルーチン

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

値が変わったときに知らせを受け取り、その知らせをきっかけに画面などを自動で更新する書き方（リアクティブプログラミング）を扱う技術です。表計算ソフトで別のセルを参照する式を入れておくと、元のセルの値を書き換えるだけで結果が自動で変わるように、値を送る側と、値の変化を受け取る側（購読する側）をあらかじめつないでおく考え方です。モバイルアプリでは、通信の結果、利用者の入力、通信の切断などがいつ起きるか分からないため、変化を待ち受けて画面に反映するこの方式がよく使われます。最初に押さえるのは、雑誌の定期購読と同じく、不要になったら購読を解除しないと値が届き続けるという点と、届いた値を変換・絞り込む演算子の役割です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

値の流れを購読するという考え方、発行側と購読側、演算子の役割を説明できず、データの変化を画面に反映するには手順ごとの指示が必要である。

## Lv1

例に沿って値の流れを購読し、変換や絞り込みの演算子を使って画面に反映できる。支援を受けて購読の解除を記述し、値が届く順序をログで確認できる。

## Lv2

入力やデータ変更の流れを演算子で結合・変換し、実行スレッドの指定、エラー処理、購読の解除まで実装できる。値の発行順序と購読のライフサイクルをテストで検証し、多重購読や解除漏れを修正できる。

## Lv3

複数のデータ源を組み合わせる流れを、ホットとコールドの違い、背圧、共有と再購読の影響を踏まえて設計できる。購読によるメモリリーク、古い値の表示、過剰な再計算を分析し、リアクティブな方式と非同期関数による方式を比較してレビューできる。

## Lv4

状態の公開と購読の規約、共通の演算子や変換部品、値の流れを検証するテスト手順を整備できる。他者の利用結果を基に、購読に起因する不具合と習得の負担の改善を確認し、方式の選択基準を更新できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | テキスト入力欄の内容を購読し、入力された文字数を画面に表示するサンプルを作る。画面を閉じるときに購読を解除し、値が届く順序と、解除後に値が届かないことをログで確認する | [Combine](https://developer.apple.com/documentation/combine)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html) |
| Lv2 | 検索欄の入力を購読し、入力が一定時間止まってから検索して結果を一覧に表示する機能を作る。通信エラー時の表示と、画面を閉じたときの購読の解除を実装し、値が発行される順序をテストで確認する | [Combine](https://developer.apple.com/documentation/combine)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture) |
| Lv3 | ログイン状態、通信状態、設定値など複数のデータ源を組み合わせて1つの画面の状態を作る流れを設計する。既存コードの購読箇所を洗い出して多重購読や解除漏れを調べ、同じ処理を非同期関数で書いた場合と比較する | [Combine](https://developer.apple.com/documentation/combine)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 値の流れの購読 | Combine（Publisher／Subscriber、Subject）、RxSwift | RxJava／RxKotlin、Flow、Observerパターン | RxJS、イベント購読とクリーンアップ |
| 値の変換と実行スレッドの指定 | Combine（Operator、Scheduler） | Flowの演算子 | RxJSの演算子 |
| 画面の状態の監視 | Observation（@Observable） | LiveData | 状態購読 |

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（Reactive Programming、Combine、RxSwift、Publishers & Subscribers、Operators & Pipelines、Schedulers、Subjects）／[SwiftUI](https://roadmap.sh/swift-ui)（Observers）／[Android](https://roadmap.sh/android)（RxJava、RxKotlin、LiveData、Observer Pattern）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
