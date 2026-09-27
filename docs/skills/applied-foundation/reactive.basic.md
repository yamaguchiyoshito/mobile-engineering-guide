---
title: "リアクティブプログラミング"
description: "リアクティブプログラミングの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# リアクティブプログラミング

**スキルID：** `reactive.basic`  
**スキル領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** Swift並行処理またはKotlinコルーチン

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | Combine（Publisher／Subscriber、Operator、Scheduler、Subject）、RxSwift、Observation（@Observable） |
| Android | RxJava／RxKotlin、LiveData、Flow の演算子、Observerパターン |
| React Native | RxJS、状態購読（イベント購読とクリーンアップ） |

roadmap.sh の参照トピック：ios: reactive-programming, combine, rxswift, publishers--subscribers, operators--pipelines, schedulers, subjects, observables--observers, data-binding / android: rxjava, rxkotlin, livedata, observer-pattern / swift-ui: observers

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
