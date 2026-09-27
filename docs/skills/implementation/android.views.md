---
title: "Android Views・Fragment"
description: "Android Views・Fragmentの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# Android Views・Fragment

**スキルID：** `android.views`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** Android  
**主な前提：** Kotlin

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

Activity、Fragment、XMLレイアウトの役割とライフサイクルを説明できず、単純な画面の変更にも手順ごとの指示が必要である。

## Lv1

例や支援に沿ってレイアウトを作成し、Viewの参照、クリック処理、一覧の表示、Intentによる画面の起動を実装できる。指定された端末と操作で表示を確認できる。

## Lv2

要件が明確な画面をActivityとFragmentに分け、制約レイアウト、一覧のAdapter、ダイアログ、画面遷移を実装できる。ライフサイクルと構成変更を考慮し、表示崩れや操作の不具合を自分で検証・修正できる。

## Lv3

FragmentとそのViewの寿命のずれ、一覧の差分更新、参照の保持によるリークなどに起因する不具合を分析できる。画面構成と遷移を設計し、段階的な移行を含めて他者の実装をレビューできる。

## Lv4

共通レイアウト、View部品、画面構成の方針、レイアウト検証の基準を整備できる。他者の利用と保守を支援し、表示不具合や改修工数の改善を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| Android | Activity、Fragment、XMLレイアウト、ConstraintLayout、RecyclerView／Adapter、ViewBinding、Navigation Component、Intent（明示的・暗黙的）、Dialog、BottomSheet、Drawer、Material Components |

roadmap.sh の参照トピック：android: activity, fragments, constraintlayout, recycleview, navigation-components, intent, explicit-intents, implicit-intents, dialog, bottomsheet, drawer, imageview, textview, interface--navigation

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
