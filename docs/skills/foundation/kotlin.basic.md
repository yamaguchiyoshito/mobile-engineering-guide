---
title: "Kotlin"
description: "Kotlinの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# Kotlin

**要素技術ID：** `kotlin.basic`  
**技術領域：** [基礎領域](index.md)  
**対象プラットフォーム：** Android  
**評価対象：** 構文、Null安全、クラス・データクラス、コレクション、拡張関数

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

Androidアプリを作るための主要なプログラミング言語であるKotlinの文法と、型の使い方を扱います。モバイルアプリの不具合は利用者の端末上で起こり、修正版を届けるにもストアでの公開手続きを経る必要があるため、nullの扱いを誤ってアプリが強制終了（クラッシュ）すると、影響が長く残ります。Kotlinは値がnullになりうるかどうかを型で区別し（null許容型）、コンパイル時に安全な扱いを求めることで、この種の誤りを減らします。最初に押さえるのは、再代入できないvalと再代入できるvarの違いと、null許容型の値を安全呼び出し（?.）やエルビス演算子（?:）で扱う方法です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

valとvar、null許容型、クラスとデータクラスの違いを説明できず、短い処理でも手順ごとの指示が必要である。

## Lv1

例を参考に関数やラムダ、データクラスのプロパティを変更し、null許容型の値を安全呼び出しやエルビス演算子で扱える。指定された入力に対する結果を実行結果やテストで確認できる。

## Lv2

要件をクラスと関数に分解し、コレクション操作、拡張関数、sealed classによる分岐を用いて実装できる。nullや境界値、例外発生時の振る舞いを確認し、デバッガーで誤りを修正できる。

## Lv3

Javaとの相互運用によるnullの混入、可変コレクションの共有、スコープ関数の乱用などが原因の不具合を分析できる。高階関数やsealed classを使った設計案を比較し、責務を整理して、他者のコードをレビューできる。

## Lv4

チームで繰り返す型設計やnullの扱いの方針、共通の拡張関数、レビュー観点、演習を整備できる。他者への展開を通じて、null起因のクラッシュや重複実装の減少を確認し、方針を更新できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Kotlinドキュメントの基本構文の例をAndroid Studioで実行し、関数、ラムダ、データクラスのプロパティを書き換えて結果の変化を確かめる。null許容型の値を ?.と ?: で扱う短い関数を書く | [Kotlinドキュメント](https://kotlinlang.org/docs/home.html)・[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) |
| Lv2 | 買い物リストの合計金額を計算する処理を、データクラス、コレクション操作、拡張関数、sealed classによる結果の分岐で実装し、空のリストや不正な数量を与えたときの振る舞いを単体テストで確認する | [Kotlinドキュメント](https://kotlinlang.org/docs/home.html)・[テスト](https://developer.android.com/training/testing) |
| Lv3 | Javaで書かれたライブラリの戻り値や、複数の箇所で共有している可変コレクションを扱う既存のコードを調べ、nullの混入や意図しない変更が起きる箇所を洗い出す。スコープ関数を重ねた処理を読みやすい形に書き直す案を比べる | [Kotlinドキュメント](https://kotlinlang.org/docs/home.html)・[AndroidのKotlin](https://developer.android.com/kotlin) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 変数と型 | val／var、Null安全 |
| データの表現 | data class、sealed class |
| 関数と処理の受け渡し | 高階関数・ラムダ、拡張関数、スコープ関数 |
| データの集まりの操作 | コレクション操作 |
| Javaとの連携 | Java相互運用 |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="kotlin-basic-syntax, kotlin-null-safety, kotlin-data-classes, kotlin-sealed-classes, kotlin-lambdas, kotlin-extensions, kotlin-scope-functions, kotlin-collection-operations, kotlin-java-interop, kotlin-docs, android-kotlin, android-basics-compose" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Kotlinドキュメント：基本構文（Android）](https://kotlinlang.org/docs/basic-syntax.html) | Android | val・var、関数、制御構文など基本の書き方を示す |
| 公式リファレンス | [Kotlinドキュメント：Null安全（Android）](https://kotlinlang.org/docs/null-safety.html) | Android | null許容型と安全呼び出し、エルビス演算子を説明 |
| 公式リファレンス | [Kotlinドキュメント：データクラス（Android）](https://kotlinlang.org/docs/data-classes.html) | Android | データを保持するクラスと自動生成される関数を説明 |
| 公式リファレンス | [Kotlinドキュメント：sealed class（Android）](https://kotlinlang.org/docs/sealed-classes.html) | Android | 継承先を限定したクラス階層とwhenでの分岐を説明 |
| 公式リファレンス | [Kotlinドキュメント：高階関数とラムダ（Android）](https://kotlinlang.org/docs/lambdas.html) | Android | 関数を引数や戻り値として扱う方法とラムダ式を説明 |
| 公式リファレンス | [Kotlinドキュメント：拡張関数（Android）](https://kotlinlang.org/docs/extensions.html) | Android | 既存のクラスに関数やプロパティを追加する方法を説明 |
| 公式リファレンス | [Kotlinドキュメント：スコープ関数（Android）](https://kotlinlang.org/docs/scope-functions.html) | Android | let・apply・runなどのスコープ関数の違いを説明 |
| 公式リファレンス | [Kotlinドキュメント：コレクション操作（Android）](https://kotlinlang.org/docs/collection-operations.html) | Android | 変換・絞り込み・集計などコレクション操作の一覧 |
| 公式リファレンス | [Kotlinドキュメント：Java相互運用（Android）](https://kotlinlang.org/docs/java-interop.html) | Android | KotlinからJavaのコードを呼び出す際の規則を説明 |
| 学習資料 | [Kotlinドキュメント（Android）](https://kotlinlang.org/docs/home.html) | Android | Kotlin言語の入門から応用までをまとめた公式文書 |
| 学習資料 | [AndroidでのKotlin（Android）](https://developer.android.com/kotlin) | Android | Android開発でKotlinを学ぶための資料をまとめたページ |
| 学習資料 | [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) | Android | KotlinとComposeでアプリを作りながら学ぶ公式コース |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
