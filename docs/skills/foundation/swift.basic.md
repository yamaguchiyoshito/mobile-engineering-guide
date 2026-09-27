---
title: "Swift"
description: "Swiftの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# Swift

**スキルID：** `swift.basic`  
**スキル領域：** [基礎領域](index.md)  
**対象プラットフォーム：** iOS  
**評価対象：** 構文、Optional、クロージャ、構造体・クラス、プロトコル、エラー処理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | 値型と参照型、Optional、クロージャ、enum、プロトコルとextension、ジェネリクス、throws／Result、プロパティラッパー、result builder、マクロ、アクセス制御、Objective-C相互運用 |

roadmap.sh の参照トピック：ios: swift-basics, closures, error-handling, oop, functional-programming, objective-c-basics, interoperability-with-swift / swift-ui: optionals--nil, closures, structures--classes, protocols, generics, enumerations, error-handling, extensions, wrappers, result-builders, macros, access-control, type-safety

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
