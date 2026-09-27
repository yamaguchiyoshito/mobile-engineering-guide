---
title: "Swift"
description: "Swiftの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# Swift

**要素技術ID：** `swift.basic`  
**技術領域：** [基礎領域](index.md)  
**対象プラットフォーム：** iOS  
**評価対象：** 構文、Optional、クロージャ、構造体・クラス、プロトコル、エラー処理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

iPhoneやiPadのアプリを作るための主要なプログラミング言語であるSwiftの文法と、型の使い方を扱います。モバイルアプリの不具合は利用者の端末上で起こり、修正版を届けるにもストアの審査を経る必要があるため、値が存在しない場合の扱いを誤ってアプリが強制終了（クラッシュ）すると、影響が長く残ります。Swiftは「値がないかもしれない」ことを型（Optional）で表し、コンパイル時に安全な扱いを求めることで、この種の誤りを減らします。最初に押さえるのは、Optionalの値を安全に取り出す方法と、代入するとコピーされる値型（構造体）と同じものを共有する参照型（クラス）の違いです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

定数と変数、Optional、構造体とクラスの違いを説明できず、短い処理でも手順ごとの指示が必要である。

## Lv1

例を参考に関数やクロージャ、構造体のプロパティを変更し、Optionalの値を安全に取り出せる。指定された入力に対する結果を実行結果やテストで確認できる。

## Lv2

要件を型と関数に分解し、値型と参照型を使い分けて、プロトコル、extension、エラー処理を用いて実装できる。nilや境界値、エラー発生時の振る舞いを確認し、デバッガーで誤りを修正できる。

## Lv3

値の共有、クロージャによる参照の保持、強制アンラップ、型推論の誤解などが原因の不具合を分析できる。プロトコルとジェネリクスを使った設計案を比較し、アクセス制御で責務の境界を整理して、他者のコードをレビューできる。

## Lv4

チームで繰り返す型設計やエラー処理の方針、共通の型とextension、レビュー観点、演習を整備できる。他者への展開を通じて、nil起因のクラッシュや重複実装の減少を確認し、方針を更新できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Swift言語ガイドの基本の章にある例をXcodeのプレイグラウンドで実行し、関数、クロージャ、構造体のプロパティを書き換えて結果の変化を確かめる。Optionalの値をif letとguard letで取り出す短い関数を書く | [Swift言語ガイド](https://docs.swift.org/swift-book/) |
| Lv2 | 買い物リストの合計金額を計算する型を、構造体、プロトコル、extension、throwsを使って実装し、空のリストや不正な数量を与えたときの振る舞いを単体テストで確認する | [Swift言語ガイド](https://docs.swift.org/swift-book/)・[Swift Testing](https://developer.apple.com/documentation/testing) |
| Lv3 | 既存のコードから強制アンラップ（!）と、クロージャ内でselfを強く参照している箇所を洗い出し、クラッシュやメモリの解放漏れにつながるものを分析する。ジェネリクスを使う案と使わない案を比べ、アクセス制御で公開範囲を整理する | [Swift言語ガイド](https://docs.swift.org/swift-book/)・[Xcode](https://developer.apple.com/documentation/xcode) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 値と型 | 値型と参照型、Optional、enum |
| 処理の受け渡し | クロージャ |
| 抽象化と再利用 | プロトコルとextension、ジェネリクス |
| エラー処理 | throws／Result |
| 記述を簡潔にする言語機能 | プロパティラッパー、result builder、マクロ |
| 公開範囲と他言語との連携 | アクセス制御、Objective-C相互運用 |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="swift-the-basics, swift-classes-structures, swift-enumerations, swift-closures, swift-protocols, swift-generics, swift-error-handling, swift-result, swift-properties, swift-macros, swift-access-control, swift-objc-import" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Swift言語ガイド：基本（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/thebasics/) | iOS | 定数・変数、基本の型、Optionalの扱いを説明する章 |
| 公式リファレンス | [Swift言語ガイド：構造体とクラス（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/classesandstructures/) | iOS | 構造体とクラスの違いと値型・参照型の振る舞いを説明 |
| 公式リファレンス | [Swift言語ガイド：列挙型（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/enumerations/) | iOS | enumの定義、関連値、パターンマッチを説明する章 |
| 公式リファレンス | [Swift言語ガイド：クロージャ（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/closures/) | iOS | クロージャの書き方と値のキャプチャを説明する章 |
| 公式リファレンス | [Swift言語ガイド：プロトコル（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/protocols/) | iOS | プロトコルの定義とextensionによる準拠を説明する章 |
| 公式リファレンス | [Swift言語ガイド：ジェネリクス（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/generics/) | iOS | 型に依存しない関数や型を定義する方法を説明する章 |
| 公式リファレンス | [Swift言語ガイド：エラー処理（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/errorhandling/) | iOS | throwsとdo-catchによるエラーの送出と処理を説明 |
| 公式リファレンス | [Result](https://developer.apple.com/documentation/swift/result) | iOS | 処理の成功値または失敗のエラーを表す列挙型 |
| 公式リファレンス | [Swift言語ガイド：プロパティ（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/properties/) | iOS | 格納・計算プロパティとプロパティラッパーを説明する章 |
| 公式リファレンス | [Swift言語ガイド：マクロ（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/macros/) | iOS | コンパイル時にコードを生成するマクロの使い方を説明 |
| 公式リファレンス | [Swift言語ガイド：アクセス制御（iOS）](https://docs.swift.org/latest/documentation/the-swift-programming-language/accesscontrol/) | iOS | モジュールやファイル単位で公開範囲を制御する方法 |
| 公式リファレンス | [Objective-CのコードをSwiftから使う（iOS）](https://developer.apple.com/documentation/swift/importing-objective-c-into-swift) | iOS | 同じターゲット内のObjective-CコードをSwiftで使う方法 |

<!-- references:end -->

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（Swift Basics、Closures、Error Handling、OOP、Functional Programming、Objective-C Basics、Interoperability with Swift）／[SwiftUI](https://roadmap.sh/swift-ui)（Optionals & Nil、Structures & Classes、Protocols、Generics、Error Handling、Extensions、Result Builders、Access Control）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
