---
title: "Kotlin"
description: "Kotlinの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# Kotlin

**スキルID：** `kotlin.basic`  
**スキル領域：** [基礎領域](index.md)  
**対象プラットフォーム：** Android  
**評価対象：** 構文、Null安全、クラス・データクラス、コレクション、拡張関数

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| Android | val／var、Null安全、data class、sealed class、拡張関数、高階関数・ラムダ、コレクション操作、スコープ関数、Java相互運用 |

roadmap.sh の参照トピック：android: basics-of-kotlin, basics-of-oop, data-structures-and-algorithms, java, pick-a-language

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
